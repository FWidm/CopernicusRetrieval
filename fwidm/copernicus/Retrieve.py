from ecmwfapi import *
from datetime import datetime, timedelta


class Retrieve(object):
    @staticmethod
    def retrieveFile(fileName, parameters, dateString, filterEurope=True):
        server = ECMWFDataServer()
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
            "param": "151.128/167.128",  # temperature and mean sea level pressure
            "step": "0",
            "stream": "oper",
            "time": "00:00:00/06:00:00/12:00:00/18:00:00",
            # see http://apps.ecmwf.int/codes/grib/format/mars/type/ - fc: forecast, an:analysis
            "type": "an",
            "target": fileName + ".grib",
        }
        if filterEurope:
            # europe
            setup["area"] = "75/-20/10/60"
        print "setup={}".format(setup)
        server.retrieve(setup)
