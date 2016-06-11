import googlemaps
import datetime
import json
import pandas as pd



class Helper :

    def getDistanceMatrix(self, origins, destinations):
        gmaps = googlemaps.Client(key="AIzaSyCTVcmF2m7PGO1UgEEv9Mfn-Vo0XbA5XYY")
        return gmaps.distance_matrix(origins, destinations,
                                     mode="driving",
                                     departure_time=datetime.datetime.now())

    def distance_dataFrame(self, json_obj):
        all_distance = []
        for elements_list in json_obj['rows']:
            distance_list = []
            for element in elements_list['elements']:
                distance_list.append(element['distance']['value'])
            all_distance.append(distance_list)

        return pd.DataFrame(all_distance)

    def getDistanceDataFrame(self, origins, destinations):
        k = self.getDistanceMatrix(origins, destinations)
        return self.distance_dataFrame(k)