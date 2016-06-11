import googlemaps
import datetime
import json

gmaps = googlemaps.Client(key = "AIzaSyCTVcmF2m7PGO1UgEEv9Mfn-Vo0XbA5XYY")


def getDistanceMatrix(origins, destinations):
    return gmaps.distance_matrix(origins, destinations,
                          mode="driving",
                          departure_time=now)