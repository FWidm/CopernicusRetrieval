from enum import Enum


# see here: http://apps.ecmwf.int/codes/grib/param-db
# https://rda.ucar.edu/docs/formats/grib/gribdoc/ecmwf_params.html v128?
class Parameter(Enum):
    STREAM_FUNCTION = {'shortName': 'STRF', 'id': 1, 'unit': 'm2 s^-1', 'description': 'Stream function'}
    VELOCITY_POTENTIAL = {'shortName': 'VPOT', 'id': 2, 'unit': 'm2 s^-1', 'description': 'Velocity potential'}
    POTENTIAL_TEMPERATURE = {'shortName': 'PT', 'id': 3, 'unit': 'K', 'description': 'Potential temperature'}
    EQUIVALENT_POTENTIAL_TEMPERATURE = {'shortName': 'EQPT', 'id': 4, 'unit': 'K',
                                        'description': 'Equivalent potential temperature'}
    SATURATED_EQUIVALENT_POTENTIAL_TEMPERATURE = {'shortName': 'SEPT', 'id': 5, 'unit': 'K',
                                                  'description': 'Saturated equivalent potential temperature'}
    SOIL_SAND_FRACTION = {'shortName': 'SSFR', 'id': 6, 'unit': '', 'description': 'Soil sand fraction'}
    SOIL_CLAY_FRACTION = {'shortName': 'SCFR', 'id': 7, 'unit': '', 'description': 'Soil clay fraction'}
    SURFACE_RUNOFF = {'shortName': 'SRO', 'id': 8, 'unit': 'm', 'description': 'Surface runoff'}
    SUB_SURFACE_RUNOFF = {'shortName': 'SSRO', 'id': 9, 'unit': 'm', 'description': 'Sub-surface runoff'}
    WIND_SPEED = {'shortName': 'WIND', 'id': 10, 'unit': 'm s^-1', 'description': 'Wind speed'}
    U_COMPONENT_OF_DIVERGENT_WIND = {'shortName': 'UDVW', 'id': 11, 'unit': 'm s^-1',
                                     'description': 'U component of divergent wind'}
    V_COMPONENT_OF_DIVERGENT_WIND = {'shortName': 'VDVW', 'id': 12, 'unit': 'm s^-1',
                                     'description': 'V component of divergent wind'}
    U_COMPONENT_OF_ROTATIONAL_WIND = {'shortName': 'URTW', 'id': 13, 'unit': 'm s^-1',
                                      'description': 'U component of rotational wind'}
    V_COMPONENT_OF_ROTATIONAL_WIND = {'shortName': 'VRTW', 'id': 14, 'unit': 'm s^-1',
                                      'description': 'V component of rotational wind'}
    UV_VISIBLE_ALBEDO_FOR_DIRECT_RADIATION = {'shortName': 'ALUVP', 'id': 15, 'unit': '',
                                              'description': 'UV visible albedo for direct radiation'}
    UV_VISIBLE_ALBEDO_FOR_DIFFUSE_RADIATION = {'shortName': 'ALUVD', 'id': 16, 'unit': '',
                                               'description': 'UV visible albedo for diffuse radiation'}
    NEAR_IR_ALBEDO_FOR_DIRECT_RADIATION = {'shortName': 'ALNIP', 'id': 17, 'unit': '',
                                           'description': 'Near IR albedo for direct radiation'}
    NEAR_IR_ALBEDO_FOR_DIFFUSE_RADIATION = {'shortName': 'ALNID', 'id': 18, 'unit': '',
                                            'description': 'Near IR albedo for diffuse radiation'}
    CLEAR_SKY_SURFACE_UV = {'shortName': 'UVCS', 'id': 19, 'unit': 'W m^-2 s', 'description': 'Clear sky surface UV'}
    CLEAR_SKY_SURFACE_PHOTOSYNTHETICALLY_ACTIVE_RADIATION = {'shortName': 'PARCS', 'id': 20, 'unit': 'W m^-2 s',
                                                             'description': 'Clear sky surface photosynthetically active radiation'}
    UNBALANCED_COMPONENT_OF_TEMPERATURE = {'shortName': 'UCTP', 'id': 21, 'unit': 'K',
                                           'description': 'Unbalanced component of temperature'}
    UNBALANCED_COMPONENT_OF_LOGARITHM_OF_SURFACE = {'shortName': 'UCLN', 'id': 22, 'unit': '',
                                                    'description': 'Unbalanced component of logarithm of surface'}
    UNBALANCED_COMPONENT_OF_DIVERGENCE = {'shortName': 'UCDV', 'id': 23, 'unit': 's^-1',
                                          'description': 'Unbalanced component of divergence'}
    LAKE_COVER = {'shortName': 'CL', 'id': 26, 'unit': '', 'description': 'Lake cover'}
    LOW_VEGETATION_COVER = {'shortName': 'CVL', 'id': 27, 'unit': '', 'description': 'Low vegetation cover'}
    HIGH_VEGETATION_COVER = {'shortName': 'CVH', 'id': 28, 'unit': '', 'description': 'High vegetation cover'}
    TYPE_OF_LOW_VEGETATION = {'shortName': 'TVL', 'id': 29, 'unit': '', 'description': 'Type of low vegetation'}
    TYPE_OF_HIGH_VEGETATION = {'shortName': 'TVH', 'id': 30, 'unit': '', 'description': 'Type of high vegetation'}
    SEA_ICE_COVER = {'shortName': 'CI', 'id': 31, 'unit': '', 'description': 'Sea-ice cover'}
    SNOW_ALBEDO = {'shortName': 'ASN', 'id': 32, 'unit': '', 'description': 'Snow albedo'}
    SNOW_DENSITY = {'shortName': 'RSN', 'id': 33, 'unit': 'kg m^-3', 'description': 'Snow density'}
    SEA_SURFACE_TEMPERATURE = {'shortName': 'SSTK', 'id': 34, 'unit': 'K', 'description': 'Sea surface temperature'}
    ICE_SURFACE_TEMPERATURE_LAYER_1 = {'shortName': 'ISTL1', 'id': 35, 'unit': 'K',
                                       'description': 'Ice surface temperature layer 1'}
    ICE_SURFACE_TEMPERATURE_LAYER_TWO = {'shortName': 'ISTL2', 'id': 36, 'unit': 'K',
                                         'description': 'Ice surface temperature layer 2'}
    ICE_SURFACE_TEMPERATURE_LAYER_3 = {'shortName': 'ISTL3', 'id': 37, 'unit': 'K',
                                       'description': 'Ice surface temperature layer 3'}
    ICE_SURFACE_TEMPERATURE_LAYER_4 = {'shortName': 'ISTL4', 'id': 38, 'unit': 'K',
                                       'description': 'Ice surface temperature layer 4'}
    VOLUMETRIC_SOIL_WATER_LAYER_1 = {'shortName': 'SWVL1', 'id': 39, 'unit': 'm3 m^-3',
                                     'description': 'Volumetric soil water layer 1'}
    VOLUMETRIC_SOIL_WATER_LAYER_TWO = {'shortName': 'SWVL2', 'id': 40, 'unit': 'm3 m^-3',
                                       'description': 'Volumetric soil water layer 2'}
    VOLUMETRIC_SOIL_WATER_LAYER_3 = {'shortName': 'SWVL3', 'id': 41, 'unit': 'm3 m^-3',
                                     'description': 'Volumetric soil water layer 3'}
    VOLUMETRIC_SOIL_WATER_LAYER_4 = {'shortName': 'SWVL4', 'id': 42, 'unit': 'm3 m^-3',
                                     'description': 'Volumetric soil water layer 4'}
    SOIL_TYPE = {'shortName': 'SLT', 'id': 43, 'unit': '', 'description': 'Soil type'}
    SNOW_EVAPORATION = {'shortName': 'ES', 'id': 44, 'unit': 'm', 'description': 'Snow evaporation'}
    SNOWMELT = {'shortName': 'SMLT', 'id': 45, 'unit': 'm', 'description': 'Snowmelt'}
    SOLAR_DURATION = {'shortName': 'SDUR', 'id': 46, 'unit': 's', 'description': 'Solar duration'}
    DIRECT_SOLAR_RADIATION = {'shortName': 'DSRP', 'id': 47, 'unit': 'W m^-2', 'description': 'Direct solar radiation'}
    MAGNITUDE_OF_SURFACE_STRESS = {'shortName': 'MAGSS', 'id': 48, 'unit': 'N m^-2 s',
                                   'description': 'Magnitude of surface stress'}
    WIND_GUST_AT_TEN_METRES = {'shortName': '10FG', 'id': 49, 'unit': 'm s^-1', 'description': 'Wind gust at 10 metres'}
    LARGE_SCALE_PRECIPITATION_FRACTION = {'shortName': 'LSPF', 'id': 50, 'unit': 's',
                                          'description': 'Large-scale precipitation fraction'}
    MAXIMUM_TWO_METRE_TEMPERATURE = {'shortName': 'MX2T24', 'id': 51, 'unit': 'K',
                                     'description': 'Maximum 2 metre temperature'}
    MINIMUM_TWO_METRE_TEMPERATURE = {'shortName': 'MN2T24', 'id': 52, 'unit': 'K',
                                     'description': 'Minimum 2 metre temperature'}
    MONTGOMERY_POTENTIAL = {'shortName': 'MONT', 'id': 53, 'unit': 'm2 s^-2', 'description': 'Montgomery potential'}
    PRESSURE = {'shortName': 'PRES', 'id': 54, 'unit': 'Pa', 'description': 'Pressure'}
    MEAN_TEMPERATURE_AT_TWO_METRES_SINCE_LAST_TWO4_HOURS = {'shortName': 'MEAN2T24', 'id': 55, 'unit': 'K',
                                                            'description': 'Mean temperature at 2 metres since last 24 hours'}
    MEAN_TWO_METRE_DEWPOINT_TEMPERATURE_IN_PAST_TWO4_HOURS = {'shortName': 'MN2D24', 'id': 56, 'unit': 'K',
                                                              'description': 'Mean 2 metre dewpoint temperature in past 24 hours'}
    DOWNWARD_UV_RADIATION_AT_THE_SURFACE = {'shortName': 'UVB', 'id': 57, 'unit': 'W m^-2',
                                            'description': 'Downward uv radiation at the surface'}
    PHOTOSYNTHETICALLY_ACTIVE_RADIATION_AT_THE_SURFACE = {'shortName': 'PAR', 'id': 58, 'unit': 'W m^-2',
                                                          'description': 'Photosynthetically active radiation at the surface'}
    CONVECTIVE_AVAILABLE_POTENTIAL_ENERGY = {'shortName': 'CAPE', 'id': 59, 'unit': 'J kg^-1',
                                             'description': 'Convective available potential energy'}
    POTENTIAL_VORTICITY = {'shortName': 'PV', 'id': 60, 'unit': 'K m2 kg^-1 s^-1', 'description': 'Potential vorticity'}
    TOTAL_PRECIPITATION_FROM_OBSERVATIONS = {'shortName': 'TPO', 'id': 61, 'unit': 'mm*100+number of stations',
                                             'description': 'Total precipitation from observations'}
    OBSERVATION_COUNT = {'shortName': 'OBCT', 'id': 62, 'unit': '', 'description': 'Observation count'}
    START_TIME_FOR_SKIN_TEMPERATURE_DIFFERENCE = {'shortName': '', 'id': 63, 'unit': 's',
                                                  'description': 'Start time for skin temperature difference'}
    FINISH_TIME_FOR_SKIN_TEMPERATURE_DIFFERENCE = {'shortName': '', 'id': 64, 'unit': 's',
                                                   'description': 'Finish time for skin temperature difference'}
    SKIN_TEMPERATURE_DIFFERENCE = {'shortName': '', 'id': 65, 'unit': 'K', 'description': 'Skin temperature difference'}
    LEAF_AREA_INDEX__LOW_VEGETATION = {'shortName': 'LAILV', 'id': 66, 'unit': 'm2 m^-2',
                                       'description': 'Leaf area index, low vegetation'}
    LEAF_AREA_INDEX__HIGH_VEGETATION = {'shortName': 'LAIHV', 'id': 67, 'unit': 'm2 m^-2',
                                        'description': 'Leaf area index, high vegetation'}
    MINIMUM_STOMATAL_RESISTANCE__LOW_VEGETATION = {'shortName': '', 'id': 68, 'unit': 's m^-1',
                                                   'description': 'Minimum stomatal resistance, low vegetation'}
    MINIMUM_STOMATAL_RESISTANCE__HIGH_VEGETATION = {'shortName': '', 'id': 69, 'unit': 's m^-1',
                                                    'description': 'Minimum stomatal resistance, high vegetation'}
    BIOME_COVER__LOW_VEGETATION = {'shortName': '', 'id': 70, 'unit': '', 'description': 'Biome cover, low vegetation'}
    BIOME_COVER__HIGH_VEGETATION = {'shortName': '', 'id': 71, 'unit': '',
                                    'description': 'Biome cover, high vegetation'}
    INSTANTANEOUS_SURFACE_SOLAR_RADIATION_DOWNWARDS = {'shortName': 'ISSRD', 'id': 72, 'unit': 'W m^-2',
                                                       'description': 'Instantaneous surface solar radiation downwards'}
    INSTANTANEOUS_SURFACE_THERMAL_RADIATION_DOWNWARDS = {'shortName': 'ISTRD', 'id': 73, 'unit': 'W m^-2',
                                                         'description': 'Instantaneous surface thermal radiation downwards'}
    STANDARD_DEVIATION_OF_FILTERED_SUBGRID_SURFACE_GEOPOTENTIAL = {'shortName': 'SDFOR', 'id': 74, 'unit': 'm',
                                                                   'description': 'Standard deviation of filtered subgrid surface geopotential'}
    SPECIFIC_RAIN_WATER_CONTENT = {'shortName': 'CRWC', 'id': 75, 'unit': 'kg kg^-1',
                                   'description': 'Specific rain water content'}
    SPECIFIC_SNOW_WATER_CONTENT = {'shortName': 'CSWC', 'id': 76, 'unit': 'kg kg^-1',
                                   'description': 'Specific snow water content'}
    TOTAL_COLUMN_LIQUID_WATER = {'shortName': 'TCLW', 'id': 78, 'unit': 'kg m^-2',
                                 'description': 'Total column liquid water'}
    TOTAL_COLUMN_ICE_WATER = {'shortName': 'TCIW', 'id': 79, 'unit': 'kg m^-2', 'description': 'Total column ice water'}
    GEOPOTENTIAL_HEIGHT = {'shortName': '', 'id': 100, 'unit': 'gpm', 'description': 'Geopotential height'}
    MAXIMUM_TEMPERATURE_AT_TWO_METRES_SINCE_LAST_6_HOURS = {'shortName': 'MX2T6', 'id': 121, 'unit': 'K',
                                                            'description': 'Maximum temperature at 2 metres since last 6 hours'}
    MINIMUM_TEMPERATURE_AT_TWO_METRES_SINCE_LAST_6_HOURS = {'shortName': 'MN2T6', 'id': 122, 'unit': 'K',
                                                            'description': 'Minimum temperature at 2 metres since last 6 hours'}
    TEN_METRE_WIND_GUST_IN_THE_PAST_6_HOURS = {'shortName': '10FG6', 'id': 123, 'unit': 'm s^-1',
                                               'description': '10 metre wind gust in the past 6 hours'}
    SURFACE_EMISSIVITY = {'shortName': 'EMIS', 'id': 124, 'unit': '', 'description': 'Surface emissivity'}
    VERTICALLY_INTEGRATED_TOTAL_ENERGY = {'shortName': '', 'id': 125, 'unit': 'J m^-2',
                                          'description': 'Vertically integrated total energy'}
    GENERIC_PARAMETER_FOR_SENSITIVE_AREA_PREDICTION = {'shortName': '', 'id': 126, 'unit': '',
                                                       'description': 'Generic parameter for sensitive area prediction'}
    ATMOSPHERIC_TIDE = {'shortName': 'AT', 'id': 127, 'unit': '', 'description': 'Atmospheric tide'}
    BUDGET_VALUES = {'shortName': 'BV', 'id': 128, 'unit': '', 'description': 'Budget values'}
    GEOPOTENTIAL = {'shortName': 'Z', 'id': 129, 'unit': 'm2 s^-2', 'description': 'Geopotential'}
    TEMPERATURE = {'shortName': 'T', 'id': 130, 'unit': 'K', 'description': 'Temperature'}
    U_VELOCITY = {'shortName': 'U', 'id': 131, 'unit': 'm s^-1', 'description': 'U velocity'}
    V_VELOCITY = {'shortName': 'V', 'id': 132, 'unit': 'm s^-1', 'description': 'V velocity'}
    SPECIFIC_HUMIDITY = {'shortName': 'Q', 'id': 133, 'unit': 'kg kg^-1', 'description': 'Specific humidity'}
    SURFACE_PRESSURE = {'shortName': 'SP', 'id': 134, 'unit': 'Pa', 'description': 'Surface pressure'}
    VERTICAL_VELOCITY = {'shortName': 'W', 'id': 135, 'unit': 'Pa s^-1', 'description': 'Vertical velocity'}
    TOTAL_COLUMN_WATER = {'shortName': 'TCW', 'id': 136, 'unit': 'kg m^-2', 'description': 'Total column water'}
    TOTAL_COLUMN_WATER_VAPOUR = {'shortName': 'TCWV', 'id': 137, 'unit': 'kg m^-2',
                                 'description': 'Total column water vapour'}
    VORTICITY_RELATIVE = {'shortName': 'VO', 'id': 138, 'unit': 's^-1', 'description': 'Vorticity (relative)'}
    SOIL_TEMPERATURE_LEVEL_1 = {'shortName': 'STL1', 'id': 139, 'unit': 'K', 'description': 'Soil temperature level 1'}
    SOIL_WETNESS_LEVEL_1 = {'shortName': 'SWL1', 'id': 140, 'unit': 'm of water', 'description': 'Soil wetness level 1'}
    SNOW_DEPTH = {'shortName': 'SD', 'id': 141, 'unit': 'm of water equivalent', 'description': 'Snow depth'}
    STRATIFORM_PRECIPITATION = {'shortName': 'LSP', 'id': 142, 'unit': 'm', 'description': 'Stratiform precipitation'}
    CONVECTIVE_PRECIPITATION = {'shortName': 'CP', 'id': 143, 'unit': 'm', 'description': 'Convective precipitation'}
    SNOWFALL_CONVECTIVE_STRATIFORM = {'shortName': 'SF', 'id': 144, 'unit': 'm of water equivalent',
                                      'description': 'Snowfall (convective + stratiform)'}
    BOUNDARY_LAYER_DISSIPATION = {'shortName': 'BLD', 'id': 145, 'unit': 'W m^-2 s',
                                  'description': 'Boundary layer dissipation'}
    SURFACE_SENSIBLE_HEAT_FLUX = {'shortName': 'SSHF', 'id': 146, 'unit': 'W m^-2 s',
                                  'description': 'Surface sensible heat flux'}
    SURFACE_LATENT_HEAT_FLUX = {'shortName': 'SLHF', 'id': 147, 'unit': 'W m^-2 s',
                                'description': 'Surface latent heat flux'}
    CHARNOCK = {'shortName': 'CHNK', 'id': 148, 'unit': '', 'description': 'Charnock'}
    SURFACE_NET_RADIATION = {'shortName': 'SNR', 'id': 149, 'unit': 'W m^-2 s', 'description': 'Surface net radiation'}
    TOP_NET_RADIATION = {'shortName': 'TNR', 'id': 150, 'unit': '', 'description': 'Top net radiation'}
    MEAN_SEA_LEVEL_PRESSURE = {'shortName': 'MSL', 'id': 151, 'unit': 'Pa', 'description': 'Mean sea-level pressure'}
    LOGARITHM_OF_SURFACE_PRESSURE = {'shortName': 'LNSP', 'id': 152, 'unit': '',
                                     'description': 'Logarithm of surface pressure'}
    SHORT_WAVE_HEATING_RATE = {'shortName': 'SWHR', 'id': 153, 'unit': 'K', 'description': 'Short-wave heating rate'}
    LONG_WAVE_HEATING_RATE = {'shortName': 'LWHR', 'id': 154, 'unit': 'K', 'description': 'Long-wave heating rate'}
    DIVERGENCE = {'shortName': 'D', 'id': 155, 'unit': 's^-1', 'description': 'Divergence'}
    HEIGHT = {'shortName': 'GH', 'id': 156, 'unit': 'm', 'description': 'Height'}
    RELATIVE_HUMIDITY = {'shortName': 'R', 'id': 157, 'unit': '%', 'description': 'Relative humidity'}
    TENDENCY_OF_SURFACE_PRESSURE = {'shortName': 'TSP', 'id': 158, 'unit': 'Pa s^-1',
                                    'description': 'Tendency of surface pressure'}
    BOUNDARY_LAYER_HEIGHT = {'shortName': 'BLH', 'id': 159, 'unit': 'm', 'description': 'Boundary layer height'}
    STANDARD_DEVIATION_OF_OROGRAPHY = {'shortName': 'SDOR', 'id': 160, 'unit': '',
                                       'description': 'Standard deviation of orography'}
    ANISOTROPY_OF_SUB_GRIDSCALE_OROGRAPHY = {'shortName': 'ISOR', 'id': 161, 'unit': '',
                                             'description': 'Anisotropy of sub-gridscale orography'}
    ANGLE_OF_SUB_GRIDSCALE_OROGRAPHY = {'shortName': 'ANOR', 'id': 162, 'unit': 'rad',
                                        'description': 'Angle of sub-gridscale orography'}
    SLOPE_OF_SUB_GRIDSCALE_OROGRAPHY = {'shortName': 'SLOR', 'id': 163, 'unit': '',
                                        'description': 'Slope of sub-gridscale orography'}
    TOTAL_CLOUD_COVER = {'shortName': 'TCC', 'id': 164, 'unit': '', 'description': 'Total cloud cover'}
    TEN_METRE_U_WIND_COMPONENT = {'shortName': '10U', 'id': 165, 'unit': 'm s^-1',
                                  'description': '10 metre U wind component'}
    TEN_METRE_V_WIND_COMPONENT = {'shortName': '10V', 'id': 166, 'unit': 'm s^-1',
                                  'description': '10 metre V wind component'}
    TWO_METRE_TEMPERATURE = {'shortName': '2T', 'id': 167, 'unit': 'K', 'description': '2 metre temperature'}
    TWO_METRE_DEWPOINT_TEMPERATURE = {'shortName': '2D', 'id': 168, 'unit': 'K',
                                      'description': '2 metre dewpoint temperature'}
    SURFACE_SOLAR_RADIATION_DOWNWARDS = {'shortName': 'SSRD', 'id': 169, 'unit': 'W m^-2 s',
                                         'description': 'Surface solar radiation downwards'}
    SOIL_TEMPERATURE_LEVEL_TWO = {'shortName': 'STL2', 'id': 170, 'unit': 'K',
                                  'description': 'Soil temperature level 2'}
    SOIL_WETNESS_LEVEL_TWO = {'shortName': 'SWL2', 'id': 171, 'unit': 'm of water',
                              'description': 'Soil wetness level 2'}
    LAND_SEA_MASK = {'shortName': 'LSM', 'id': 172, 'unit': '', 'description': 'Land/sea mask'}
    SURFACE_ROUGHNESS = {'shortName': 'SR', 'id': 173, 'unit': 'm', 'description': 'Surface roughness'}
    ALBEDO = {'shortName': 'AL', 'id': 174, 'unit': '', 'description': 'Albedo'}
    SURFACE_THERMAL_RADIATION_DOWNWARDS = {'shortName': 'STRD', 'id': 175, 'unit': 'W m^-2 s',
                                           'description': 'Surface thermal radiation downwards'}
    SURFACE_SOLAR_RADIATION = {'shortName': 'SSR', 'id': 176, 'unit': 'W m^-2 s',
                               'description': 'Surface solar radiation'}
    SURFACE_THERMAL_RADIATION = {'shortName': 'STR', 'id': 177, 'unit': 'W m^-2 s',
                                 'description': 'Surface thermal radiation'}
    TOP_SOLAR_RADIATION = {'shortName': 'TSR', 'id': 178, 'unit': 'W m^-2 s', 'description': 'Top solar radiation'}
    TOP_THERMAL_RADIATION = {'shortName': 'TTR', 'id': 179, 'unit': 'W m^-2 s', 'description': 'Top thermal radiation'}
    EAST_WEST_SURFACE_STRESS = {'shortName': 'EWSS', 'id': 180, 'unit': 'N m^-2 s',
                                'description': 'East/West surface stress'}
    NORTH_SOUTH_SURFACE_STRESS = {'shortName': 'NSSS', 'id': 181, 'unit': 'N m^-2 s',
                                  'description': 'North/South surface stress'}
    EVAPORATION = {'shortName': 'E', 'id': 182, 'unit': 'm of water', 'description': 'Evaporation'}
    SOIL_TEMPERATURE_LEVEL_3 = {'shortName': 'STL3', 'id': 183, 'unit': 'K', 'description': 'Soil temperature level 3'}
    SOIL_WETNESS_LEVEL_3 = {'shortName': 'SWL3', 'id': 184, 'unit': 'm of water', 'description': 'Soil wetness level 3'}
    CONVECTIVE_CLOUD_COVER = {'shortName': 'CCC', 'id': 185, 'unit': '', 'description': 'Convective cloud cover'}
    LOW_CLOUD_COVER = {'shortName': 'LCC', 'id': 186, 'unit': '', 'description': 'Low cloud cover'}
    MEDIUM_CLOUD_COVER = {'shortName': 'MCC', 'id': 187, 'unit': '', 'description': 'Medium cloud cover'}
    HIGH_CLOUD_COVER = {'shortName': 'HCC', 'id': 188, 'unit': '', 'description': 'High cloud cover'}
    SUNSHINE_DURATION = {'shortName': 'SUND', 'id': 189, 'unit': 's', 'description': 'Sunshine duration'}
    EW_COMPONENT_OF_SUBGRID_OROGRAPHIC_VARIANCE = {'shortName': 'EWOV', 'id': 190, 'unit': 'm2',
                                                   'description': 'EW component of subgrid orographic variance'}
    NS_COMPONENT_OF_SUBGRID_OROGRAPHIC_VARIANCE = {'shortName': 'NSOV', 'id': 191, 'unit': 'm2',
                                                   'description': 'NS component of subgrid orographic variance'}
    NWSE_COMPONENT_OF_SUBGRID_OROGRAPHIC_VARIANCE = {'shortName': 'NWOV', 'id': 192, 'unit': 'm2',
                                                     'description': 'NWSE component of subgrid orographic variance'}
    NESW_COMPONENT_OF_SUBGRID_OROGRAPHIC_VARIANCE = {'shortName': 'NEOV', 'id': 193, 'unit': 'm2',
                                                     'description': 'NESW component of subgrid orographic variance'}
    BRIGHTNESS_TEMPERATURE = {'shortName': 'BTMP', 'id': 194, 'unit': 'K', 'description': 'Brightness temperature'}
    LATITUDINAL_COMPONENT_OF_GRAVITY_WAVE_STRESS = {'shortName': 'LGWS', 'id': 195, 'unit': 'N m^-2 s',
                                                    'description': 'Latitudinal component of gravity wave stress'}
    MERIDIONAL_COMPONENT_OF_GRAVITY_WAVE_STRESS = {'shortName': 'MGWS', 'id': 196, 'unit': 'N m^-2 s',
                                                   'description': 'Meridional component of gravity wave stress'}
    GRAVITY_WAVE_DISSIPATION = {'shortName': 'GWD', 'id': 197, 'unit': 'W m^-2 s',
                                'description': 'Gravity wave dissipation'}
    SKIN_RESERVOIR_CONTENT = {'shortName': 'SRC', 'id': 198, 'unit': 'm of water',
                              'description': 'Skin reservoir content'}
    VEGETATION_FRACTION = {'shortName': 'VEG', 'id': 199, 'unit': '', 'description': 'Vegetation fraction'}
    VARIANCE_OF_SUB_GRIDSCALE_OROGRAPHY = {'shortName': 'VSO', 'id': 200, 'unit': 'm2',
                                           'description': 'Variance of sub-gridscale orography'}
    MAXIMUM_TWO_METRE_TEMPERATURE_SINCE_PREVIOUS_POST_PROCESSING = {'shortName': 'MX2T', 'id': 201, 'unit': 'K',
                                                                    'description': 'Maximum 2 metre temperature since previous post-processing'}
    MINIMUM_TWO_METRE_TEMPERATURE_SINCE_PREVIOUS_POST_PROCESSING = {'shortName': 'MN2T', 'id': 202, 'unit': 'K',
                                                                    'description': 'Minimum 2 metre temperature since previous post-processing'}
    OZONE_MASS_MIXING_RATIO = {'shortName': 'O3', 'id': 203, 'unit': 'kg kg^-1',
                               'description': 'Ozone mass mixing ratio'}
    PRECIPITATION_ANALYSIS_WEIGHTS = {'shortName': 'PAW', 'id': 204, 'unit': '',
                                      'description': 'Precipitation analysis weights'}
    RUNOFF = {'shortName': 'RO', 'id': 205, 'unit': 'm', 'description': 'Runoff'}
    TOTAL_COLUMN_OZONE = {'shortName': 'TCO3', 'id': 206, 'unit': 'kg m^-2', 'description': 'Total column ozone'}
    TEN_METRE_WINDSPEED = {'shortName': '10SI', 'id': 207, 'unit': 'm s^-1', 'description': '10 metre windspeed'}
    TOP_NET_SOLAR_RADIATION__CLEAR_SKY = {'shortName': 'TSRC', 'id': 208, 'unit': 'W m^-2 s',
                                          'description': 'Top net solar radiation, clear sky'}
    TOP_NET_THERMAL_RADIATION__CLEAR_SKY = {'shortName': 'TTRC', 'id': 209, 'unit': 'W m^-2 s',
                                            'description': 'Top net thermal radiation, clear sky'}
    SURFACE_NET_SOLAR_RADIATION__CLEAR_SKY = {'shortName': 'SSRC', 'id': 210, 'unit': 'W m^-2 s',
                                              'description': 'Surface net solar radiation, clear sky'}
    SURFACE_NET_THERMAL_RADIATION__CLEAR_SKY = {'shortName': 'STRC', 'id': 211, 'unit': 'W m^-2 s',
                                                'description': 'Surface net thermal radiation, clear sky'}
    SOLAR_INSOLATION = {'shortName': 'SI', 'id': 212, 'unit': 'W m^-2 s', 'description': 'Solar insolation'}
    VERTICALLY_INTEGRATED_MOISTURE_DIVERGENCE = {'shortName': 'VIMD', 'id': 213, 'unit': 'kg m^-2',
                                                 'description': 'Vertically integrated moisture divergence'}
    DIABATIC_HEATING_BY_RADIATION = {'shortName': 'DHR', 'id': 214, 'unit': 'K',
                                     'description': 'Diabatic heating by radiation'}
    DIABATIC_HEATING_BY_VERTICAL_DIFFUSION = {'shortName': 'DHVD', 'id': 215, 'unit': 'K',
                                              'description': 'Diabatic heating by vertical diffusion'}
    DIABATIC_HEATING_BY_CUMULUS_CONVECTION = {'shortName': 'DHCC', 'id': 216, 'unit': 'K',
                                              'description': 'Diabatic heating by cumulus convection'}
    DIABATIC_HEATING_BY_LARGE_SCALE_CONDENSATION = {'shortName': 'DHLC', 'id': 217, 'unit': 'K',
                                                    'description': 'Diabatic heating by large-scale condensation'}
    VERTICAL_DIFFUSION_OF_ZONAL_WIND = {'shortName': 'VDZW', 'id': 218, 'unit': 'm s^-1',
                                        'description': 'Vertical diffusion of zonal wind'}
    VERTICAL_DIFFUSION_OF_MERIDIONAL_WIND = {'shortName': 'VDMW', 'id': 219, 'unit': 'm s^-1',
                                             'description': 'Vertical diffusion of meridional wind'}
    EW_GRAVITY_WAVE_DRAG_TENDENCY = {'shortName': 'EWGD', 'id': 220, 'unit': 'm s^-1',
                                     'description': 'EW gravity wave drag tendency'}
    NS_GRAVITY_WAVE_DRAG_TENDENCY = {'shortName': 'NSGD', 'id': 221, 'unit': 'm s^-1',
                                     'description': 'NS gravity wave drag tendency'}
    CONVECTIVE_TENDENCY_OF_ZONAL_WIND = {'shortName': 'CTZW', 'id': 222, 'unit': 'm s^-1',
                                         'description': 'Convective tendency of zonal wind'}
    CONVECTIVE_TENDENCY_OF_MERIDIONAL_WIND = {'shortName': 'CTMW', 'id': 223, 'unit': 'm s^-1',
                                              'description': 'Convective tendency of meridional wind'}
    VERTICAL_DIFFUSION_OF_HUMIDITY = {'shortName': 'VDH', 'id': 224, 'unit': 'kg kg^-1',
                                      'description': 'Vertical diffusion of humidity'}
    HUMIDITY_TENDENCY_BY_CUMULUS_CONVECTION = {'shortName': 'HTCC', 'id': 225, 'unit': 'kg kg^-1',
                                               'description': 'Humidity tendency by cumulus convection'}
    HUMIDITY_TENDENCY_LARGE_SCALE_CONDENSATION = {'shortName': 'HTLC', 'id': 226, 'unit': 'kg kg^-1',
                                                  'description': 'Humidity tendency large-scale condensation'}
    CHANGE_FROM_REMOVING_NEGATIVE_HUMIDITY = {'shortName': 'CRNH', 'id': 227, 'unit': 'kg kg^-1',
                                              'description': 'Change from removing negative humidity'}
    TOTAL_PRECIPITATION = {'shortName': 'TP', 'id': 228, 'unit': 'm', 'description': 'Total precipitation'}
    INSTANTANEOUS_X_SURFACE_STRESS = {'shortName': 'IEWS', 'id': 229, 'unit': 'N m^-2',
                                      'description': 'Instantaneous X surface stress'}
    INSTANTANEOUS_Y_SURFACE_STRESS = {'shortName': 'INSS', 'id': 230, 'unit': 'N m^-2',
                                      'description': 'Instantaneous Y surface stress'}
    INSTANTANEOUS_SURFACE_HEAT_FLUX = {'shortName': 'ISHF', 'id': 231, 'unit': 'W m^-2',
                                       'description': 'Instantaneous surface heat flux'}
    INSTANTANEOUS_MOISTURE_FLUX = {'shortName': 'IE', 'id': 232, 'unit': 'kg m^-2 s',
                                   'description': 'Instantaneous moisture flux'}
    APPARENT_SURFACE_HUMIDITY = {'shortName': 'ASQ', 'id': 233, 'unit': 'kg kg^-1',
                                 'description': 'Apparent surface humidity'}
    LOGARITHM_OF_SURFACE_ROUGHNESS_LENGTH_FOR_HEAT = {'shortName': 'LSRH', 'id': 234, 'unit': '',
                                                      'description': 'Logarithm of surface roughness length for heat'}
    SKIN_TEMPERATURE = {'shortName': 'SKT', 'id': 235, 'unit': 'K', 'description': 'Skin temperature'}
    SOIL_TEMPERATURE_LEVEL_4 = {'shortName': 'STL4', 'id': 236, 'unit': 'K', 'description': 'Soil temperature level 4'}
    SOIL_WETNESS_LEVEL_4 = {'shortName': 'SWL4', 'id': 237, 'unit': 'm', 'description': 'Soil wetness level 4'}
    TEMPERATURE_OF_SNOW_LAYER = {'shortName': 'TSN', 'id': 238, 'unit': 'K', 'description': 'Temperature of snow layer'}
    CONVECTIVE_SNOWFALL = {'shortName': 'CSF', 'id': 239, 'unit': 'm of water equivalent',
                           'description': 'Convective snowfall'}
    LARGE_SCALE_SNOWFALL = {'shortName': 'LSF', 'id': 240, 'unit': 'm of water equivalent',
                            'description': 'Large-scale snowfall'}
    ACCUMULATED_CLOUD_FRACTION_TENDENCY = {'shortName': 'ACF', 'id': 241, 'unit': '',
                                           'description': 'Accumulated cloud fraction tendency'}
    ACCUMULATED_LIQUID_WATER_TENDENCY = {'shortName': 'ALW', 'id': 242, 'unit': '',
                                         'description': 'Accumulated liquid water tendency'}
    FORECAST_ALBEDO = {'shortName': 'FAL', 'id': 243, 'unit': '', 'description': 'Forecast albedo'}
    FORECAST_SURFACE_ROUGHNESS = {'shortName': 'FSR', 'id': 244, 'unit': 'm',
                                  'description': 'Forecast surface roughness'}
    FORECAST_LOG_OF_SURFACE_ROUGHNESS_FOR_HEAT = {'shortName': 'FLSR', 'id': 245, 'unit': '',
                                                  'description': 'Forecast log of surface roughness for heat'}
    CLOUD_LIQUID_WATER_CONTENT = {'shortName': 'CLWC', 'id': 246, 'unit': 'kg kg^-1',
                                  'description': 'Cloud liquid water content'}
    CLOUD_ICE_WATER_CONTENT = {'shortName': 'CIWC', 'id': 247, 'unit': 'kg kg^-1',
                               'description': 'Cloud ice water content'}
    CLOUD_COVER = {'shortName': 'CC', 'id': 248, 'unit': '', 'description': 'Cloud cover'}
    ACCUMULATED_ICE_WATER_TENDENCY = {'shortName': 'AIW', 'id': 249, 'unit': '',
                                      'description': 'Accumulated ice water tendency'}
    ICE_AGE = {'shortName': 'ICE', 'id': 250, 'unit': '', 'description': 'Ice age'}
    ADIABATIC_TENDENCY_OF_TEMPERATURE = {'shortName': 'ATTE', 'id': 251, 'unit': 'K',
                                         'description': 'Adiabatic tendency of temperature'}
    ADIABATIC_TENDENCY_OF_HUMIDITY = {'shortName': 'ATHE', 'id': 252, 'unit': 'kg kg^-1',
                                      'description': 'Adiabatic tendency of humidity'}
    ADIABATIC_TENDENCY_OF_ZONAL_WIND = {'shortName': 'ATZE', 'id': 253, 'unit': 'm s^-1',
                                        'description': 'Adiabatic tendency of zonal wind'}
    ADIABATIC_TENDENCY_OF_MERIDIONAL_WIND = {'shortName': 'ATMW', 'id': 254, 'unit': 'm s^-1',
                                             'description': 'Adiabatic tendency of meridional wind'}
