# !/Users/fabianwidmann/anaconda/envs/copernicus/bin/python python
import os
from pprint import pprint

from fwidm.copernicus import Parser, Retrieve
from datetime import datetime, timedelta
from fwidm.copernicus.data import Enums
import json

from fwidm.copernicus.data.CopernicusData import CopernicusData

r = Retrieve.Retrieve()
latestRetrievalDate = datetime.today() - timedelta(days=5)
dateString = latestRetrievalDate.strftime(Retrieve.Retrieve.DATEFORMAT)

# print "retrievalDate={}; type={}".format(dateString, type(dateString))
# times=Parameters.Time.ZERO
param_list = Enums.ParameterCAMS.all()
# print Enums.Parameter.combine_to_string(param_list)
#retrieve forecast with steps 0/3/6/9/12
#file=r.retrieve_file("data/ecmwf/fc-"+dateString,date=latestRetrievalDate,dataType=Enums.DataType.FORECAST, steps=Retrieve.Retrieve.calcSteps(5))
file=r.retrieve_file_with_setup("ezpz",{
    "class": "mc",
    "dataset": "cams_nrealtime",
    "date": "2017-08-03",
    "expver": "0001",
    "levtype": "sfc",
    "param": "2.214",
    "step": "0",
    "stream": "oper",
    "time": "00:00:00/12:00:00",
    "type": "fc",
    "target": "output",
})
points = [[48.4391, 9.9823]]  # ,[48.301669,9.900532],[48.777106,9.180769]]
# result = Parser.Parser.nearest("data/ecmwf/2017-07-06.grib", points)
parser = Parser.Parser()
for point in points:
    # result = parser.get_nearest_values("2017-07-20.grib", point, parameters=[Enums.ParameterCAMS.TWO_METRE_TEMPERATURE])
    result = parser.get_nearest_values(file, point)
    print(json.dumps(result, default=CopernicusData.json_serial, indent=2))


    # result = parser.get_nearest_values("data/dwd/dwd.grib2", point)
    # print(json.dumps(result, default=CopernicusData.json_serial, indent=2))

# Prints all the params inside the grib file.
# resultList = parser.get_parameters("dwd.grib2",csv=True)
# print  "\n".join(resultList)
