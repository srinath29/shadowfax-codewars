import googlemaps
import datetime
import json

gmaps = googlemaps.Client(key = "AIzaSyCTVcmF2m7PGO1UgEEv9Mfn-Vo0XbA5XYY")

now = datetime.datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

print(json.loads( directions_result))