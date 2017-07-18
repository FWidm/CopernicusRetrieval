from datetime import datetime

import eccodes

import pytz

from fwidm.copernicus.data import Parameters


class Parser(object):
    def retrieve_metadata(self, gid):
        """
        Retrieves specific metadata keys from the currently loaded grib file
        more information: https://software.ecmwf.int/wiki/display/ECC/GRIB%3A+Keys
        :param gid: grib file
        :return: dictionary containing the keys
        """
        keys = [
            'dataTime',
            'paramId',  # parameter works as well
            'units',
            'shortName',
            'name',
            'date',
        ]
        dict = {}
        for key in keys:
            try:
                dict[key] = eccodes.codes_get(gid, key)
            except eccodes.CodesInternalError as err:
                print 'Error with key="%s" : %s' % (key, err.msg)
        return dict

    def format_data(self, ecc_data, meta_data):
        # ecc_data contains lat, lon, index, value, distance (from target in km)
        # meta data contains dataTime, paramId, units, shortName, name
        retDict = {}
        data = {}
        for i in range(0, len(ecc_data)):
            data = dict(ecc_data[i])
            data['paramId'] = meta_data['paramId']
            data['date'] = datetime.strptime(str(meta_data['date']), '%Y%m%d').replace(hour=meta_data['dataTime'] / 100,
                                                                                       tzinfo=pytz.UTC)
            data['description'] = meta_data
        param = Parameters.Parameter.lookup_id(meta_data['paramId'])
        retDict[param.name] = data
        return retDict

    def get_nearest_values(self, filePath, point, n=1, parameters=Parameters.Parameter.all(),
                           times=Parameters.Time.all(), regroup=True):
        """
         Retrieves data from the given filePath - retrieves 1 or 4 values near the given point
        :param filePath: path to the retrieved grib file
        :param point: (latitude,longitude)
        :param n: 1 or 4 points to retrieve
        :param parameters: list of parameters (Parameters.Parameter)
        :param times: list of times (Parameters.Time)
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

            if Parameters.Parameter.lookup_id(metadata['paramId']) not in parameters:  # skip unused/unsupported params
                continue

            if Parameters.Time.lookup_time(metadata['dataTime']) not in times:  # skip unused/unsupported times
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

    def iterate_keys(self, filePath):
        f = open(filePath)

        while 1:
            gid = eccodes.codes_grib_new_from_file(f)
            if gid is None:
                break

            iterid = eccodes.codes_keys_iterator_new(gid, 'ls')

            # Different types of keys can be skipped
            # codes_skip_computed(iterid)
            # codes_skip_coded(iterid)
            # codes_skip_edition_specific(iterid)
            # codes_skip_duplicates(iterid)
            # codes_skip_read_only(iterid)
            # codes_skip_function(iterid)

            while eccodes.codes_keys_iterator_next(iterid):
                keyname = eccodes.codes_keys_iterator_get_name(iterid)
                keyval = eccodes.codes_get_string(iterid, keyname)
                print "%s = %s" % (keyname, keyval)
            print "____" * 5

            eccodes.codes_keys_iterator_delete(iterid)
            eccodes.codes_release(gid)

        f.close()

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
