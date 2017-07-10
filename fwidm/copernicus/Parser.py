from eccodes import *


class Parser(object):

    @staticmethod
    def parseFile(filePath):
        f = open(filePath)
        gid = codes_grib_new_from_file(f)

        values = codes_get_values(gid)
        print "values {}".format(values)
        # for i in xrange(len(values)):
        #     print "%d %.10e" % (i + 1, values[i])
        #
        # print '%d values found in %s' % (len(values), file)
        #
        # for key in ('max', 'min', 'average'):
        #     print '%s=%.10e' % (key, codes_get(gid, key))

        codes_release(gid)
        f.close()

    @staticmethod
    def nearest(filePath, points, n=1):
        # type: (str, tuple/tuple of tuples

        f = open(filePath)
        gid = codes_grib_new_from_file(f)
        data = []

        for lat, lon in points:
            results = codes_grib_find_nearest(gid, lat, lon, is_lsm=False, npoints=n)
            for i in range(len(results)):
                # lat, lng, value, distance (in km!), index of nearest station.
                # print nearest.lat, nearest.lon, nearest.value, nearest.distance, nearest.index
                data.append(results[i])
                print "- %d -" % i
                print results[i]

            print "-" * 100

        codes_release(gid)
        f.close()
        return data