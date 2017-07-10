# !/usr/bin/env python
from gribapi import *
from eccodes import *
from fwidm.copernicus import Parser, Retrieve




r = Retrieve.Retrieve()
r.retrieveFile()


points = [(48.4391, 9.9823)]
result = Parser.Parser.nearest("output2.grib", points)

print "Result: {}".format(result)
