from ecmwfapi import *


class Retrieve(object):

    def __init__(self):
        print("init")
        self.file=None

    def retrieveFile(self):
            server = ECMWFDataServer()
            server.retrieve({
                "class": "mc",
                "dataset": "cams_nrealtime",
                "date": "2017-07-01",
                "expver": "0001",
                "levtype": "sfc",
                "param": "167.128",
                "step": "3/6/9",
                "stream": "oper",
                "time": "00:00:00/12:00:00",
                "type": "fc",
                "target": "output.grib",
            })