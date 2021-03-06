import googlemaps
import datetime
import json
import pandas as pd
from geopy.distance import vincenty, great_circle
import re


class Helper :

    def getDistanceMatrix(self, origins, destinations):
        '''
            Using google api method distance_matrix we get distances between lat/lon pairs
        '''
        gmaps = googlemaps.Client(key="AIzaSyCTVcmF2m7PGO1UgEEv9Mfn-Vo0XbA5XYY")
        return gmaps.distance_matrix(origins, destinations,
                                     mode="driving",
                                     departure_time=datetime.datetime.now())


    def distance_dataFrame(self, json_obj):
        '''
        get numpy 2d array of distances between lat lon combinations.
        :param json_obj:
        :return: array of array of distances.
        '''
        all_distance = []
        for elements_list in json_obj['rows']:
            distance_list = []
            for element in elements_list['elements']:
                distance_list.append(element['distance']['value'])
            all_distance.append(distance_list)

        return pd.DataFrame(all_distance)


    def getDistanceDataFrame(self, origins, destinations):
        '''
        It's a wrapper method to format distances.
        :param origins:
        :param destinations:
        :return:
        '''
        k = self.getDistanceMatrix(origins, destinations)
        return self.distance_dataFrame(k)


    def getDistanceGmaps(self, origin, destination):
        '''
        Another helper method to get distance between two nodes.
        :param origin:
        :param destination:
        :return:
        '''
        k = self.getDistanceMatrix(origin, destination)
        return self.distance_dataFrame(k)[0][0]


    def getGeopyVincenty(self, origin, destination):
        '''
        Direct Distance calculator between two nodes. Provided as alternative to using google api.
        :param origin:
        :param destination:
        :return:
        '''
        return vincenty(origin, destination).kilometers

    def getGeopyGreaterCircle(self, origin, destination):
        '''
        One more alternative to calculate distance between two nodes. Provided as alternative to using google api.
        :param origin:
        :param destination:
        :return:
        '''
        return great_circle(origin, destination).kilometers

    def timeDataFrame(self, json_obj):
        '''
        Helper method to extract time taken from gmaps json.
        :param json_obj:
        :return: time field
        '''
        all_time = []
        for elements_list in json_obj['rows']:
            time_list = []
            for element in elements_list['elements']:
                time_list.append(element['duration_in_traffic']['value'])
            all_time.append(time_list)

        return pd.DataFrame(all_time)

    def getTimeGmaps(self, origin, destination):
        '''
        Wrapper method to time field between two nodes.
        :param origin:
        :param destination:
        :return:
        '''
        k = self.getDistanceMatrix(origin, destination)
        return self.timeDataFrame(k)[0][0]

    def prepare_lat_lon_string(self, geohash1, geohash2):
        geohash = str(geohash1[0])+ ':' +str(geohash1[1])+ '~' + str(geohash2[0]) + ':' + str(geohash2[1])
        return geohash

    def decode_lat_lon_string(self, str_val):
        _geocoords = re.compile(r'(?P<lat1>.+?[0-9]):(?P<lon1>.+?[0-9])~(?P<lat2>.+?[0-9]):(?P<lon2>.+?.*)',
                              flags=re.UNICODE)
        val = _geocoords.search(str_val)

        return val


if __name__ == '__main__':
    """
    print(Helper().prepare_lat_lon_string(('12.345', '77.888'),('11.876','67.77')))
    obj = Helper().decode_lat_lon_string('12.345:77.888~11.876:67.77')
    print(obj.group('lon2'))
    print(obj.group('lon1'))
    print(obj.group('lat1'))
    print(obj.group('lat2'))
    """
    print(Helper().prepare_lat_lon_string((12.925975583315498, 77.6753354072571),(12.931280000000001, 77.68624)))