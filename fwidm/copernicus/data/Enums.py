from enum import Enum


# Available times for the analysis
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
        ret = None
        if time == 0:
            ret = Time.ZERO
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
class ParameterCAMS(Enum):
    @staticmethod
    def all():
        # noinspection PyTypeChecker
        return [param for param in ParameterCAMS]

    @staticmethod
    def lookup_id(paramId):
        """
        Retrieves an enum entry by id.
        :param paramId:
        :return: Enum else None
        """
        # noinspection PyTypeChecker
        for p in ParameterCAMS:
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
    GEOPOTENTIAL = {'eraId': '129.128', 'shortName': 'Z', 'id': 129, 'unit': 'm2 s**-2', 'description': 'Geopotential'}
    TOTAL_COLUMN_WATER_VAPOUR = {'eraId': '137.128', 'shortName': 'TCWV', 'id': 137, 'unit': 'kg m**-2',
                                 'description': 'Total column water vapour'}
    MEAN_SEA_LEVEL_PRESSURE = {'eraId': '151.128', 'shortName': 'MSL', 'id': 151, 'unit': 'Pa',
                               'description': 'Mean sea-level pressure'}
    TOTAL_CLOUD_COVER = {'eraId': '164.128', 'shortName': 'TCC', 'id': 164, 'unit': '',
                         'description': 'Total cloud cover'}
    TEN_METRE_U_WIND_COMPONENT = {'eraId': '165.128', 'shortName': '10U', 'id': 165, 'unit': 'm s**-1',
                                  'description': '10 metre U wind component'}
    TEN_METRE_V_WIND_COMPONENT = {'eraId': '166.128', 'shortName': '10V', 'id': 166, 'unit': 'm s**-1',
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

    # NON standard ones - directly imported from ERA.
    TOTAL_COLUMN_METHANE = {'eraId': '4.218', 'shortName': 'tc_ch4', 'id': 218004, 'unit': 'kg m**-2',
                            'description': 'Total column methane'}
    TOTAL_COLUMN_NITRIC_ACID = {'eraId': '6.218', 'shortName': 'tc_hno3', 'id': 218006, 'unit': 'kg m**-2',
                                'description': 'Total column nitric acid'}
    TOTAL_COLUMN__PEROXYACETYL_NITRATE = {'eraId': '13.218', 'shortName': 'tc_pan', 'id': 218013, 'unit': 'kg m**-2',
                                          'description': 'Total column  peroxyacetyl nitrate'}
    TOTAL_COLUMN__ISOPRENE = {'eraId': '16.218', 'shortName': 'tc_c5h8', 'id': 218016, 'unit': 'kg m**-2',
                              'description': 'Total column  isoprene'}
    TOTAL_COLUMN_NITROGEN_MONOXIDE = {'eraId': '27.218', 'shortName': 'tc_no', 'id': 218027, 'unit': 'kg m**-2',
                                      'description': 'Total column nitrogen monoxide'}
    TOTAL_COLUMN_HYDROXYL_RADICAL = {'eraId': '3.218', 'shortName': 'tc_oh', 'id': 218030, 'unit': 'kg m**-2',
                                     'description': 'Total column hydroxyl radical'}
    TOTAL_COLUMN__ETHANE = {'eraId': '45.218', 'shortName': 'tc_c2h6', 'id': 218045, 'unit': 'kg m**-2',
                            'description': 'Total column  ethane'}
    TOTAL_COLUMN_PROPANE = {'eraId': '47.218', 'shortName': 'tc_c3h8', 'id': 218047, 'unit': 'kg m**-2',
                            'description': 'Total column propane'}
    DUST_EMISSION_POTENTIAL = {'eraId': '52.210', 'shortName': 'aerdep', 'id': 210052, 'unit': 'kg s**2 m**-5',
                               'description': 'Dust emission potential'}
    LIFTING_THRESHOLD_SPEED = {'eraId': '53.210', 'shortName': 'aerlts', 'id': 210053, 'unit': 'm s**-1',
                               'description': 'Lifting threshold speed'}
    TOTAL_COLUMN_NITROGEN_DIOXIDE = {'eraId': '125.210', 'shortName': 'tcno2', 'id': 210125, 'unit': 'kg m**-2',
                                     'description': 'Total column Nitrogen dioxide'}
    TOTAL_COLUMN_SULPHUR_DIOXIDE = {'eraId': '126.210', 'shortName': 'tcso2', 'id': 210126, 'unit': 'kg m**-2',
                                    'description': 'Total column Sulphur dioxide'}
    TOTAL_COLUMN_CARBON_MONOXIDE = {'eraId': '127.210', 'shortName': 'tcco', 'id': 210127, 'unit': 'kg m**-2',
                                    'description': 'Total column Carbon monoxide'}
    TOTAL_COLUMN_FORMALDEHYDE = {'eraId': '128.210', 'shortName': 'tchcho', 'id': 210128, 'unit': 'kg m**-2',
                                 'description': 'Total column Formaldehyde'}
    GEMS_TOTAL_COLUMN_OZONE = {'eraId': '206.210', 'shortName': 'gtco3', 'id': 210206, 'unit': 'kg m**-2',
                               'description': 'GEMS Total column ozone'}
    # Forecast specific?
    UV_BIOLOGICALLY_EFFECTIVE_DOSE = {'eraId': '214002.128', 'shortName': 'uvbed', 'id': 214002, 'unit': '~',
                                      'description': ' UV biologically effective dose'}
    UV_BIOLOGICALLY_EFFECTIVE_DOSE_CLEAR_SKY = {'eraId': '214003.128', 'shortName': 'uvbedcs', 'id': 214003,
                                                'unit': '~', 'description': ' UV biologically effective dose clear-sky'}
    PARTICULATE_MATTER_D_SMALLER_1_UM = {'eraId': '72.210', 'shortName': 'pm1', 'id': 210072, 'unit': 'kg m**-3',
                                         'description': 'Particulate matter d < 1 um'}
    PARTICULATE_MATTER_D_SMALLER_2_5_UM = {'eraId': '73.210', 'shortName': 'pm2p5', 'id': 210073, 'unit': 'kg m**-3',
                                           'description': 'Particulate matter d < 2.5 um'}
    PARTICULATE_MATTER_D_SMALLER_T10_UM = {'eraId': '74.210', 'shortName': 'pm10', 'id': 210074, 'unit': 'kg m**-3',
                                           'description': 'Particulate matter d < 10 um'}
    LARGE_SCALE_PRECIPITATION = {'eraId': '142.128', 'shortName': 'lsp', 'id': 142, 'unit': 'm',
                                 'description': 'Large-scale precipitation'}
    CONVECTIVE_PRECIPITATION = {'eraId': '143.128', 'shortName': 'cp', 'id': 143, 'unit': 'm',
                                'description': 'Convective precipitation'}
    SNOWFALL = {'eraId': '144.128', 'shortName': 'sf', 'id': 144, 'unit': 'm of water equivalent',
                'description': 'Snowfall'}
    TOTAL_AEROSOL_OPTICAL_DEPTH_AT_550NM = {'eraId': '207.210', 'shortName': 'aod550', 'id': 210207, 'unit': '~',
                                            'description': 'Total Aerosol Optical Depth at 550nm'}
    SEA_SALT_AEROSOL_OPTICAL_DEPTH_AT_550NM = {'eraId': '208.210', 'shortName': 'ssaod550', 'id': 210208, 'unit': '~',
                                               'description': 'Sea Salt Aerosol Optical Depth at 550nm'}
    DUST_AEROSOL_OPTICAL_DEPTH_AT_550NM = {'eraId': '209.210', 'shortName': 'duaod550', 'id': 210209, 'unit': '~',
                                           'description': 'Dust Aerosol Optical Depth at 550nm'}
    ORGANIC_MATTER_AEROSOL_OPTICAL_DEPTH_AT_550NM = {'eraId': '21.210', 'shortName': 'omaod550', 'id': 210210,
                                                     'unit': '~',
                                                     'description': 'Organic Matter Aerosol Optical Depth at 550nm'}
    BLACK_CARBON_AEROSOL_OPTICAL_DEPTH_AT_550NM = {'eraId': '211.210', 'shortName': 'bcaod550', 'id': 210211,
                                                   'unit': '~',
                                                   'description': 'Black Carbon Aerosol Optical Depth at 550nm'}
    SULPHATE_AEROSOL_OPTICAL_DEPTH_AT_550NM = {'eraId': '212.210', 'shortName': 'suaod550', 'id': 210212, 'unit': '~',
                                               'description': 'Sulphate Aerosol Optical Depth at 550nm'}
    TOTAL_AEROSOL_OPTICAL_DEPTH_AT_469NM = {'eraId': '213.210', 'shortName': 'aod469', 'id': 210213, 'unit': '~',
                                            'description': 'Total Aerosol Optical Depth at 469nm'}
    TOTAL_AEROSOL_OPTICAL_DEPTH_AT_670NM = {'eraId': '214.210', 'shortName': 'aod670', 'id': 210214, 'unit': '~',
                                            'description': 'Total Aerosol Optical Depth at 670nm'}
    TOTAL_AEROSOL_OPTICAL_DEPTH_AT_865NM = {'eraId': '215.210', 'shortName': 'aod865', 'id': 210215, 'unit': '~',
                                            'description': 'Total Aerosol Optical Depth at 865nm'}
    TOTAL_AEROSOL_OPTICAL_DEPTH_AT_1TWO40NM = {'eraId': '216.210', 'shortName': 'aod1240', 'id': 210216, 'unit': '~',
                                               'description': 'Total Aerosol Optical Depth at 1240nm'}
    FORECAST_ALBEDO = {'eraId': '243.128', 'shortName': 'fal', 'id': 243, 'unit': '(0 - 1)',
                       'description': 'Forecast albedo'}


class ParameterERA5(Enum):
    # todo: implement params
    @staticmethod
    def all():
        # noinspection PyTypeChecker
        return [param for param in ParameterERA5]


class DataSets(Enum):
    # ERA5 = {'name': 'era5', 'class': 'ea', 'delayDays': None 'dateFormat': None}
    CAMS = {'name': 'cams_nrealtime', 'class': 'mc', 'delayDays': 5, 'dateFormat': '%Y-%m-%d'}
