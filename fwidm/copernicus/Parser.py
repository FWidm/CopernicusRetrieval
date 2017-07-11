import os
import sys
import eccodes


class Parser(object):
    @staticmethod
    def parseFile(filePath):
        f = open(filePath)
        gid = eccodes.codes_grib_new_from_file(f)

        values = eccodes.codes_get_values(gid)
        # print "values {}".format(values)
        # for i in xrange(len(values)):
        #     print "%d %.10e" % (i + 1, values[i])
        #
        # print '%d values found in %s' % (len(values), file)
        #
        # for key in ('max', 'min', 'average'):
        #     print '%s=%.10e' % (key, codes_get(gid, key))
        iterid = eccodes.codes_keys_iterator_new(gid, 'ls')

        # Different types of keys can be skipped
        # grib_skip_computed(iterid)
        # grib_skip_coded(iterid)
        # grib_skip_edition_specific(iterid)
        # grib_skip_duplicates(iterid)
        # grib_skip_read_only(iterid)
        # grib_skip_function(iterid)

        while eccodes.codes_keys_iterator_next(iterid):
            keyname = eccodes.codes_keys_iterator_get_name(iterid)
            keyval = eccodes.codes_get_string(iterid, keyname)
            print "%s = %s" % (keyname, keyval)

        eccodes.codes_keys_iterator_delete(iterid)
        eccodes.codes_release(gid)
        f.close()

    @staticmethod
    def getMetaData():
        return None

    @staticmethod
    def getKeys(filePath,point,n=1):
        results=[]
        f = open(filePath)

        # more information: https://software.ecmwf.int/wiki/display/ECC/GRIB%3A+Keys
        keys = [
            # 'Ni',
            # 'Nj',
            # 'latitudeOfFirstGridPointInDegrees',
            # 'longitudeOfFirstGridPointInDegrees',
            # 'latitudeOfLastGridPointInDegrees',
            # 'longitudeOfLastGridPointInDegrees',
             'dataTime',
            # 'time',
            'paramId',  # parameter works as well
            'units',
            'shortName',
            'name',
        ]
        # loop through all the parameters
        while 1:
            gid = eccodes.codes_grib_new_from_file(f)
            # try:
            #     time = eccodes.codes_get(gid, 'dataTime')
            #     name = eccodes.codes_get(gid, 'name')
            #     shortName = eccodes.codes_get(gid, 'shortName')
            # except eccodes.CodesInternalError as err:
            #     print 'Error: {}',format(err.msg)

            if gid is None:
                break
            dict={}
            dict['metadata']={}
            for key in keys:
                try:
                    print '  %s: %s' % (key, eccodes.codes_get(gid, key))
                    dict['metadata'][key]=eccodes.codes_get(gid, key)
                except eccodes.CodesInternalError as err:
                    print 'Error with key="%s" : %s' % (key, err.msg)

            print 'There are %d values, average is %f, min is %f, max is %f' % (
                eccodes.codes_get_size(gid, 'values'),
                eccodes.codes_get(gid, 'average'),
                eccodes.codes_get(gid, 'min'),
                eccodes.codes_get(gid, 'max')
            )

            nearest=eccodes.codes_grib_find_nearest(gid, point[0], point[1], is_lsm=False, npoints=n)
            dict['data']=nearest
            print "dict={}".format(dict)
            print "nearest={}".format(nearest)
            results.append(dict)

            eccodes.codes_release(gid)
            print "release"

        f.close()

        return results

    @staticmethod
    def nearest(filePath, points, n=4):
        # type: (str, tuple/tuple of tuples

        f = open(filePath)
        gid = eccodes.codes_grib_new_from_file(f)
        data = []

        for lat, lon in points:
            results = eccodes.codes_grib_find_nearest(gid, lat, lon, is_lsm=False, npoints=n)
            for i in range(len(results)):
                # lat, lng, value, distance (in km!), index of nearest station.
                # print nearest.lat, nearest.lon, nearest.value, nearest.distance, nearest.index
                data.append(results[i])
                print "- %d -" % i
                print results[i]

            print "-" * 100

        eccodes.codes_release(gid)
        f.close()
        return data
