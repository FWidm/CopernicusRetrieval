# !/usr/bin/env python
from pprint import pprint

from fwidm.copernicus import Parser, Retrieve
from datetime import datetime, timedelta
from fwidm.copernicus.data import Parameters


r = Retrieve.Retrieve()
latestRetrievalDate = datetime.today() - timedelta(days=5)
dateString=latestRetrievalDate.strftime("%Y-%m-%d")

print "retrievalDate={}; type={}".format(dateString,type(dateString))

#r.retrieveFile(dateString,None,dateString)


points = [(48.4391, 9.9823)]
#result = Parser.Parser.nearest("2017-07-06.grib", points)
result = Parser.Parser.get_keys("2017-07-06.grib",points[0])
# value
pprint(result)

