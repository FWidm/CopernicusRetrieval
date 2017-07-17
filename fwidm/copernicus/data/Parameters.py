from enum import Enum


# Availeble times for the analysis
class Time(Enum):
    ZERO = '00:00:00'
    SIX = '06:00:00'
    TWELVE = '12:00:00'
    EIGHTTEEN = '18:00:00'

    @staticmethod
    def all():
        # noinspection PyTypeChecker
        return [param for param in Time]

    @staticmethod
    def lookup_time(time):
        """
        Retrieves an enum entry by id.
        :param paramId:
        :return: Enum else None
        """
        # noinspection PyTypeChecker
        ret=None
        if time == 0:
            ret= Time.ZERO
        if time == 600:
            ret = Time.SIX
        if time == 1200:
            ret = Time.TWELVE
        if time == 1800:
            ret = Time.EIGHTTEEN
        # print "looking up time={} (type={}) - result={}".format(time,type(time),ret)
        return ret

    @staticmethod
    def combine_to_string(times):
        """
        Combine the given times (either a Time obj or list of Times to a valid string repr in the form of:
        s=time[0]/.../time[n]
        :param times: list or Times or Time obj
        :return: string s=time[0]/.../time[n]
        """
        retval = ""
        if isinstance(times, Enum):
            retval = times.value
        else:
            for i in xrange(0, len(times)):
                retval += times[i].value
                retval += '/' if i < (len(times) - 1) else ''

        return retval


# see here: http://apps.ecmwf.int/codes/grib/param-db
# https://rda.ucar.edu/docs/formats/grib/gribdoc/ecmwf_params.html v128?
# all parameters: Add all of the .210 ones
# "4.218/6.218/13.218/16.218/27.218/30.218/34.128/45.218/47.218/52.210/53.210/125.210/
# 126.210/127.210/128.210/129.128/137.128/151.128/164.128/165.128/166.128/167.128/
# 168.128/172.128/174.128/186.128/187.128/188.128/206.210",
# --> http://apps.ecmwf.int/datasets/data/cams-nrealtime/levtype=sfc/?date_date_range=2017-07-01&time=00:00:'00.128',12:00:00&step=0&param=143.128
class Parameter(Enum):

    @staticmethod
    def all():
        # noinspection PyTypeChecker
        return [param for param in Parameter]

    @staticmethod
    def lookup_id(paramId):
        """
        Retrieves an enum entry by id.
        :param paramId:
        :return: Enum else None
        """
        # noinspection PyTypeChecker
        for p in Parameter:
            if p.value['id'] == paramId or int(p.value['eraId'].split('.')[0]) == paramId:
                return p
        return None

    @staticmethod
    def combine_to_string(times):
        """
        Combine the given parameters (either an obj or list  to a valid string repr in the form of:
        s=id[0]/.../id[n]
        :param times: list or Times or Time obj
        :return: string s=id[0]/.../id[n]
        """
        retval = ""
        if isinstance(times, Enum):
            retval = times.value['eraId']
        else:
            for i in xrange(0, len(times)):
                retval += times[i].value['eraId']
                retval += '/' if i < (len(times) - 1) else ''
        return retval

    SEA_SURFACE_TEMPERATURE = {'eraId': '34.128', 'shortName': 'SSTK', 'id': 34, 'unit': 'K',
                               'description': 'Sea surface temperature'}
    GEOPOTENTIAL = {'eraId': '129.128', 'shortName': 'Z', 'id': 129, 'unit': 'm2 s^-2', 'description': 'Geopotential'}
    TOTAL_COLUMN_WATER_VAPOUR = {'eraId': '137.128', 'shortName': 'TCWV', 'id': 137, 'unit': 'kg m^-2',
                                 'description': 'Total column water vapour'}
    MEAN_SEA_LEVEL_PRESSURE = {'eraId': '151.128', 'shortName': 'MSL', 'id': 151, 'unit': 'Pa',
                               'description': 'Mean sea-level pressure'}
    TOTAL_CLOUD_COVER = {'eraId': '164.128', 'shortName': 'TCC', 'id': 164, 'unit': '',
                         'description': 'Total cloud cover'}
    TEN_METRE_U_WIND_COMPONENT = {'eraId': '165.128', 'shortName': '10U', 'id': 165, 'unit': 'm s^-1',
                                  'description': '10 metre U wind component'}
    TEN_METRE_V_WIND_COMPONENT = {'eraId': '166.128', 'shortName': '10V', 'id': 166, 'unit': 'm s^-1',
                                  'description': '10 metre V wind component'}
    TWO_METRE_TEMPERATURE = {'eraId': '167.128', 'shortName': '2T', 'id': 167, 'unit': 'K',
                             'description': '2 metre temperature'}
    TWO_METRE_DEWPOINT_TEMPERATURE = {'eraId': '168.128', 'shortName': '2D', 'id': 168, 'unit': 'K',
                                      'description': '2 metre dewpoint temperature'}
    LAND_SEA_MASK = {'eraId': '172.128', 'shortName': 'LSM', 'id': 172, 'unit': '', 'description': 'Land/sea mask'}
    ALBEDO = {'eraId': '174.128', 'shortName': 'AL', 'id': 174, 'unit': '', 'description': 'Albedo'}
    LOW_CLOUD_COVER = {'eraId': '186.128', 'shortName': 'LCC', 'id': 186, 'unit': '', 'description': 'Low cloud cover'}
    MEDIUM_CLOUD_COVER = {'eraId': '187.128', 'shortName': 'MCC', 'id': 187, 'unit': '',
                          'description': 'Medium cloud cover'}
    HIGH_CLOUD_COVER = {'eraId': '188.128', 'shortName': 'HCC', 'id': 188, 'unit': '',
                        'description': 'High cloud cover'}
