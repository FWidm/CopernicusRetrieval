# !/usr/bin/env python
from pprint import pprint

from fwidm.copernicus import Parser, Retrieve
from datetime import datetime, timedelta
from fwidm.copernicus.data import Parameters


r = Retrieve.Retrieve()
latestRetrievalDate = datetime.today() - timedelta(days=5)
dateString=latestRetrievalDate.strftime("%Y-%m-%d")

print "retrievalDate={}; type={}".format(dateString,type(dateString))
# times=Parameters.Time.ZERO
params=[Parameters.Parameter.TWO_METRE_TEMPERATURE,Parameters.Parameter.MEAN_SEA_LEVEL_PRESSURE]
r=Retrieve.Retrieve()
r.retrieveFile(dateString,params,dateString)


points = [(48.4391, 9.9823)]
#result = Parser.Parser.nearest("2017-07-06.grib", points)
parser = Parser.Parser()
result=parser.get_nearest_values("2017-07-08.grib", points[0])

pprint(result)

