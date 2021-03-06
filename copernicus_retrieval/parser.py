from datetime import datetime

import eccodes
import pytz
from copernicus_retrieval import util

from copernicus_retrieval.data import copernicus_data
from copernicus_retrieval.data.copernicus_enums import Time, ParameterCAMS


class Parser(object):
    def retrieve_metadata(self, gid):
        """
        Retrieves specific metadata keys from the currently loaded grib file
        more information: https://software.ecmwf.int/wiki/display/ECC/GRIB%3A+Keys
        :param gid: grib file
        :return: dictionary containing the keys
        """
        keys = [
            #todo: add more params if needed.
            'dataTime',
            'paramId',  # parameter works as well
            'units',
            'shortName',
            'name',
            'date',
            'step'
        ]
        dict = {}
        for key in keys:
            try:
                dict[key] = eccodes.codes_get(gid, key)
            except eccodes.CodesInternalError as err:
                print 'Error with key="%s" : %s' % (key, err.msg)
        return dict


    def convert_to_alternative_unit(self, value, unit):
        """
        Converts the retrieved value from thee existing Unit into another one if supported.
        :param value: to convert from
        :param unit: to convert from
        :return: touple of value and unit
        """
        #print value,unit
        if "K" in unit:
            return value-273.15,"C"
        return None,None



    def format_data(self, eccData, metadata):
        """
        reformat the data
        :param eccData: contains lat, lon, index, value, distance (from target in km)
        :param metadata: contains dataTime, paramId, units, shortName, name
        :return:
        """
        ret_dict = {}
        data = {}
        for i in range(0, len(eccData)):
            data = dict(eccData[i])
            #data['paramId'] = metadata['paramId']
            data['date'] = datetime.strptime(str(metadata['date']), '%Y%m%d').replace(hour=metadata['dataTime'] / 100,
                                                                                      tzinfo=pytz.UTC)
            converted_val, target_unit = self.convert_to_alternative_unit(data['value'],metadata['units'])
            data['description'] = metadata

            if converted_val:
                data['convertedValue']=converted_val
            if target_unit:
                data['description']['convertedUnit'] = target_unit

        param = ParameterCAMS.lookup_id(metadata['paramId'])
        #todo: adjust type here.
        ret_dict[param.name] = copernicus_data.CopernicusData(data,metadata['name'])
        return ret_dict

    def get_nearest_values(self, filePath, point, n=1, parameters=ParameterCAMS.all(),
                           times=Time.all(), regroup=True):
        """
         Retrieves data from the given filePath - retrieves 1 or 4 values near the given point
        :param filePath: path to the retrieved grib file
        :param point: (latitude,longitude)
        :param n: 1 or 4 points to retrieve
        :param parameters: list of parameters (Enums.Parameter)
        :param times: list of times (Enums.Time)
        :return: dict containing all expected values
        """
        f = open(filePath)
        if n != 1 and n != 4:
            raise Exception("Parameter 'n' describes the number of requested data points and must be either 1 or 4.")
        if type(point[0]) is not float:
            raise Exception("Point should be a list of two coordinates in the form of [lat:float,lon:float] ")
        results = {}
        list = []
        # loop through all the parameters
        while 1:
            gid = eccodes.codes_grib_new_from_file(f)
            if gid is None:
                break

            metadata = self.retrieve_metadata(gid)

            if ParameterCAMS.lookup_id(metadata['paramId']) not in parameters:  # skip unused/unsupported params
                #print "skipping... metadata={}".format(metadata)
                continue

            if Time.lookup_time(metadata['dataTime']) not in times:  # skip unused/unsupported times
                continue

            nearest = eccodes.codes_grib_find_nearest(gid, point[0], point[1], is_lsm=False, npoints=n)
            data = self.format_data(nearest, metadata)
            list.append(data)
            eccodes.codes_release(gid)

        f.close()
        results['values'] = list
        if regroup:
            results = self.group_dict_by_param(results)

        return results

    def group_dict_by_param(self, dict):
        """
        groups all values of a specific type inside the same dict e.g. if 4 values for "mean sea level pressure" exist,
        all values are now in a list under the same key.
        :param dict: resulting dict after parsing
        :return: grouped up dictionary by parameter-type
        """
        new = {}
        for item in dict['values']:
            for key, val in item.iteritems():
                if key not in new:
                    new[key] = []
                new[key].append(val)

        return new

    def get_parameters(self, filePath,csv=False):
        """
        Retrieves parameters for all parameters that are currently available at time 00:00:00 and returns them as a list of strings for
        Enums.Parameter.py
        :param filePath:
        :return:
        """
        f = open(filePath)
        metadata_list = []
        # loop through all the parameters and retrieve the metadata
        while 1:

            gid = eccodes.codes_grib_new_from_file(f)
            if gid is None:
                break
            metadata = self.retrieve_metadata(gid)
            if (Time.lookup_time(metadata['dataTime']) == Time.ZERO):
                metadata_list.append(metadata)
        return  util.parameter_to_string(metadata_list, csv=csv)

    def test_dwd_grib(self, filePath, point, n=1, parameters=ParameterCAMS.all(),
                      times=Time.all(), regroup=False):
        """
         Retrieves data from the given filePath - retrieves 1 or 4 values near the given point
        :param filePath: path to the retrieved grib file
        :param point: (latitude,longitude)
        :param n: 1 or 4 points to retrieve
        :param parameters: list of parameters (Enums.Parameter)
        :param times: list of times (Enums.Time)
        :return: dict containing all expected values
        """
        f = open(filePath)
        if n != 1 and n != 4:
            raise Exception("Parameter 'n' describes the number of requested data points and must be either 1 or 4.")
        if type(point[0]) is not float:
            raise Exception("Point should be a list of two coordinates in the form of [lat:float,lon:float] ")
        results = {}
        list = []
        # loop through all the parameters
        while 1:
            gid = eccodes.codes_grib_new_from_file(f)
            if gid is None:
                break
            metadata = self.retrieve_metadata(gid)
            print metadata
            nearest = eccodes.codes_grib_find_nearest(gid, point[0], point[1], is_lsm=False, npoints=n)
            list.append(nearest)
            eccodes.codes_release(gid)

        f.close()
        results['values'] = list
        if regroup:
            results = self.group_dict_by_param(results)

        return results