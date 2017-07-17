from ecmwfapi import *
from fwidm.copernicus.data import Parameters
from datetime import datetime, timedelta


class Retrieve(object):

    def era5_retrieve(selfs):
        server = ECMWFDataServer()
        server.retrieve({
            "class": "ea",
            "dataset": "era5",
            "date": "2016-07-31",
            "expver": "1",
            "levelist": "2",
            "levtype": "pl",
            "number": "0/1/2/3/4/5/6/7/8/9",
            "param": "60.128/75.128/76.128/129.128/130.128/131.128/132.128/133.128/135.128/138.128/155.128/157.128/203.128/246.128/247.128/248.128",
            "stream": "enda",
            "time": "00:00:00/03:00:00/06:00:00/09:00:00/12:00:00/15:00:00/18:00:00/21:00:00",
            "type": "an",
            "target": "output",
        })

    def retrieve_file(self, fileName, parameters, dateString, times=Parameters.Time.all(), filterEurope=True):
        """
        Retrieves the file from the Copernicus Atmospheric Monitoring Service
        :param fileName: file name of the retrieved file
        :param parameters: list of wanted parameters see fwidm.copernicus.data.Parameters->Parameter
        :param dateString:
        :param times: list of wanted params, see fwidm.copernicus.data.Parameters->Time
        :param filterEurope:
        :return:
        """
        if parameters is None or times is None:
            raise ValueError("Parameter 'parameters' cannot be None. Please provice a valid list of Parameters.Parameter or a single Parameters.Parameter object.")
        timesString=Parameters.Time.combine_to_string(times)
        parametersString=Parameters.Parameter.combine_to_string(parameters)
        server = ECMWFDataServer()
        print "Retrieving with parameters... times={}; parameters={}".format(timesString,parametersString)
        # see keywords here:
        #        https://software.ecmwf.int/wiki/display/UDOC/Identification+keywords?src=contextnavpagetreemode
        setup = {
            "class": "mc",
            "dataset": "cams_nrealtime",
            "date": dateString,
            "expver": "0001",
            # levtype - denotes type of level. Its value has a direct implication on valid levelist values.
            # Common values are: model level (ml), pressure level (pl), surface (sfc), potential vorticity (pv),
            #   potential temperature (pt) and depth (dp).
            "levtype": "sfc",
            # specifies the meteorological parameter.
            "param": parametersString,#"151.128/167.128",  # temperature and mean sea level pressure
            "step": "0",
            "stream": "oper",
            "time": timesString,#"00:00:00/06:00:00/12:00:00/18:00:00",
            # see http://apps.ecmwf.int/codes/grib/format/mars/type/ - fc: forecast, an:analysis
            "type": "an",
            "target": fileName + ".grib",
        }
        if filterEurope:
            # europe
            setup["area"] = "75/-20/10/60"
        print "setup={}".format(setup)
        server.retrieve(setup)
