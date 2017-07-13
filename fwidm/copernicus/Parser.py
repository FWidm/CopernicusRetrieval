import os
import sys
import eccodes


class Parser(object):
    def retrieve_meta_data(self, gid):
        # more information: https://software.ecmwf.int/wiki/display/ECC/GRIB%3A+Keys
        keys = [
            'dataTime',
            'paramId',  # parameter works as well
            'units',
            'shortName',
            'name',
        ]
        dict = {}
        for key in keys:
            try:
                dict[key] = eccodes.codes_get(gid, key)
            except eccodes.CodesInternalError as err:
                print 'Error with key="%s" : %s' % (key, err.msg)
        return dict

    def get_nearest_values(self, filePath, point, n=1):
        results = []
        f = open(filePath)

        # loop through all the parameters
        while 1:
            gid = eccodes.codes_grib_new_from_file(f)

            if gid is None:
                break
            dict = {}

            nearest = eccodes.codes_grib_find_nearest(gid, point[0], point[1], is_lsm=False, npoints=n)
            dict['data'] = nearest
            dict['metadata'] = self.retrieve_meta_data(gid)
            results.append(dict)

            eccodes.codes_release(gid)

        f.close()

        return results
