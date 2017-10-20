from datetime import date, datetime

from copernicus_retrieval.data.copernicus_enums import Classification


class CopernicusData:
    """
    A simple wrapper class for the resulting parameters that are returned by the Copernicus Service.
    """

    def __init__(self, dict,type):
        self.index = dict["index"]
        self.type = type
        self.latitude = dict["lat"]
        self.longitude = dict["lon"]
        self.date = dict["date"]
        self.description = dict["description"]
        self.distance = dict["distance"]
        self.value = dict['value']
        self.classification = Classification.classify(type)

    def __repr__(self):

        return "CopernicusData: {}".format(self.__dict__)

    @staticmethod
    def json_serial(obj):
        """
        Serializer for objects of this class
        :param obj: the currently used object
        :return: serialized object
        """
        if isinstance(obj, (datetime, date)):
            serial = obj.isoformat()
            return serial

        if isinstance(obj, CopernicusData):
            return obj.__dict__

        raise TypeError("Type %s not serializable" % type(obj))