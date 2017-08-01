# !/Users/fabianwidmann/anaconda/envs/copernicus/bin/python python
from pprint import pprint

from fwidm.copernicus import Parser, Retrieve
from datetime import datetime, timedelta
from fwidm.copernicus.data import Enums
import json

from fwidm.copernicus.data.CopernicusData import CopernicusData





r = Retrieve.Retrieve()
latestRetrievalDate = datetime.today() - timedelta(days=5)
dateString = latestRetrievalDate.strftime(Retrieve.DATEFORMAT)

# print "retrievalDate={}; type={}".format(dateString, type(dateString))
# times=Parameters.Time.ZERO
param_list = Enums.ParameterCAMS.all()
# print Enums.Parameter.combine_to_string(param_list)
#file=r.retrieve_file(dateString,date=latestRetrievalDate)

points = [[48.4391, 9.9823]]#,[48.301669,9.900532],[48.777106,9.180769]]
# result = Parser.Parser.nearest("2017-07-06.grib", points)
parser = Parser.Parser()
for point in points:
    result = parser.get_nearest_values("2017-07-20.grib", point, parameters=[Enums.ParameterCAMS.TWO_METRE_TEMPERATURE])
    # print result
    print(json.dumps(result, default=CopernicusData.json_serial, indent=2))

# Prints all the params inside the grib file.
# resultList = parser.get_parameters("2017-07-14-fc.grib")
# print  "\n".join(resultList)

