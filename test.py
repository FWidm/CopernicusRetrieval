# !/Users/fabianwidmann/anaconda/envs/copernicus/bin/python python

import json
from datetime import datetime, timedelta

from copernicus_retrieval import parser
from copernicus_retrieval.data import copernicus_enums, copernicus_data

from copernicus_retrieval import retrieve

r = retrieve.Retrieve()
latestRetrievalDate = datetime.today() - timedelta(days=copernicus_enums.DataSets.CAMS.value['delayDays'])
dateString = latestRetrievalDate.strftime(retrieve.Retrieve.DATEFORMAT)

# print "retrievalDate={}; type={}".format(dateString, type(dateString))
# times=Parameters.Time.ZERO
param_list = copernicus_enums.ParameterCAMS.all()
# print Enums.Parameter.combine_to_string(param_list)
#retrieve forecast with steps 0/3/6/9/12
file=r.retrieve_file("data/ecmwf/an-" + dateString, date=latestRetrievalDate, dataType=copernicus_enums.DataType.ANALYSIS)
# file=r.retrieve_file_with_setup("ezpz",{
#     "class": "mc",
#     "dataset": "cams_nrealtime",
#     "date": "2017-08-03",
#     "expver": "0001",
#     "levtype": "sfc",
#     "param": "2.214",
#     "step": "0",
#     "stream": "oper",
#     "time": "00:00:00/12:00:00",
#     "type": "fc",
#     "target": "output",
# })
points = [[48.4391, 9.9823]]  # ,[48.301669,9.900532],[48.777106,9.180769]]
# result = Parser.Parser.nearest("data/ecmwf/2017-07-06.grib", points)
parser = parser.Parser()
for point in points:
    # result = parser.get_nearest_values("2017-07-20.grib", point, parameters=[Enums.ParameterCAMS.TWO_METRE_TEMPERATURE])
    result = parser.get_nearest_values(file, point, parameters=copernicus_enums.ParameterCAMS.all())
    print(json.dumps(result, default=copernicus_data.CopernicusData.json_serial, indent=2))


    # result = parser.get_nearest_values("data/dwd/dwd.grib2", point)
    # print(json.dumps(result, default=CopernicusData.json_serial, indent=2))

# Prints all the params inside the grib file.
# resultList = parser.get_parameters("dwd.grib2",csv=True)
# print  "\n".join(resultList)
