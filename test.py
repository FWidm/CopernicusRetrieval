# !/Users/fabianwidmann/anaconda/envs/copernicus/bin/python python
from pprint import pprint
from datetime import date, datetime

from fwidm.copernicus import Parser, Retrieve
from datetime import datetime, timedelta
from fwidm.copernicus.data import Parameters
import json


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        serial = obj.isoformat()
        return serial
    raise TypeError("Type %s not serializable" % type(obj))


r = Retrieve.Retrieve()
latestRetrievalDate = datetime.today() - timedelta(days=5)
dateString = latestRetrievalDate.strftime("%Y-%m-%d")

print "retrievalDate={}; type={}".format(dateString, type(dateString))
# times=Parameters.Time.ZERO
param_list = Parameters.Parameter.all()
# print Parameters.Parameter.combine_to_string(param_list)
r = Retrieve.Retrieve()
# r.retrieveFile(dateString,param_list,dateString)


points = (48.4391, 9.9823)
# result = Parser.Parser.nearest("2017-07-06.grib", points)
parser = Parser.Parser()
result = parser.get_nearest_values("2017-07-08.grib", points, parameters=[Parameters.Parameter.MEAN_SEA_LEVEL_PRESSURE],
                                   times=[Parameters.Time.SIX])
# parser.iterate_keys("2017-07-08.grib")#parser.iterate_keys("2017-07-08.grib")
print(json.dumps(result, default=json_serial, indent=2))



# param_list=[param for param in Parameters.Parameter]
# print Parameters.Parameter.combine_to_string(param_list)
