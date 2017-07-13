from enum import Enum


# Availeble times for the analysis
class Time(Enum):
    ZERO = '00:00:00'
    SIX = '06:00:00'
    TWELVE = '12:00:00'
    EIGHTTEEN = '18:00:00'
    ALL = ZERO + '/' + SIX + '/' + TWELVE + '/' + EIGHTTEEN

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
    def lookup_id(paramId):
        """
        Retrieves an enum entry by id.
        :param paramId:
        :return: Enum else None
        """
        # noinspection PyTypeChecker
        for p in Parameter:
            if p.value['id'] == paramId:
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
            retval = times.value['id']
        else:
            for i in xrange(0, len(times)):
                retval += times[i].value['id']
                retval += '/' if i < (len(times) - 1) else ''
        return retval

    # add .128 suffix to all entries via: regex find: 'id': \d*, replace: '$1.128',
    SEA_SURFACE_TEMPERATURE = {'shortName': 'SSTK', 'id': '34.128', 'unit': 'K',
                               'description': 'Sea surface temperature'}

    TWO_METRE_DEWPOINT_TEMPERATURE = {'shortName': '2D', 'id': '168.128', 'unit': 'K',
                                      'description': '2 metre dewpoint temperature'}
    TWO_METRE_TEMPERATURE = {'shortName': '2T', 'id': '167.128', 'unit': 'K', 'description': '2 metre temperature'}
    TEN_METRE_U_WIND_COMPONENT = {'shortName': '10U', 'id': '165.128', 'unit': 'm s^-1',
                                  'description': '10 metre U wind component'}
    TEN_METRE_V_WIND_COMPONENT = {'shortName': '10V', 'id': '166.128', 'unit': 'm s^-1',
                                  'description': '10 metre V wind component'}

    # Missing:  UV biologically effective dose = {'shortName': '??', 'id': 2.'214.128', 'unit': '??', 'description': 'UV biologically effective dose'}

    # Missing:  UV biologically effective dose clear-sky  = {'shortName': '??', 'id': 3.'214.128', 'unit': '??', 'description': 'UV biologically effective dose clear-sky'}

    ALBEDO = {'shortName': 'AL', 'id': '174.128', 'unit': '', 'description': 'Albedo'}

    CONVECTIVE_PRECIPITATION = {'shortName': 'CP', 'id': '143.128', 'unit': 'm',
                                'description': 'Convective precipitation'}

    FORECAST_ALBEDO = {'shortName': 'FAL', 'id': '243.128', 'unit': '', 'description': 'Forecast albedo'}

    GEOPOTENTIAL = {'shortName': 'Z', 'id': '129.128', 'unit': 'm2 s^-2', 'description': 'Geopotential'}

    MEAN_SEA_LEVEL_PRESSURE = {'shortName': 'MSL', 'id': '151.128', 'unit': 'Pa',
                               'description': 'Mean sea-level pressure'}

    TOTAL_COLUMN_WATER_VAPOUR = {'shortName': 'TCWV', 'id': '137.128', 'unit': 'kg m^-2',
                                 'description': 'Total column water vapour'}

    TOTAL_CLOUD_COVER = {'shortName': 'TCC', 'id': '164.128', 'unit': '', 'description': 'Total cloud cover'}

    LAND_SEA_MASK = {'shortName': 'LSM', 'id': '172.128', 'unit': '', 'description': 'Land/sea mask'}

    LOW_CLOUD_COVER = {'shortName': 'LCC', 'id': '186.128', 'unit': '', 'description': 'Low cloud cover'}

    MEDIUM_CLOUD_COVER = {'shortName': 'MCC', 'id': '187.128', 'unit': '', 'description': 'Medium cloud cover'}

    HIGH_CLOUD_COVER = {'shortName': 'HCC', 'id': '188.128', 'unit': '', 'description': 'High cloud cover'}
