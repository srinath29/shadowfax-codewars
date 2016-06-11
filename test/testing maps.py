import googlemaps
import datetime
import json

gmaps = googlemaps.Client(key = "AIzaSyCTVcmF2m7PGO1UgEEv9Mfn-Vo0XbA5XYY")

now = datetime.datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
# directions_result = gmaps.directions((12.985805, 77.737007),(12.992220,77.715910),
#                                      mode="driving",
#                                      departure_time=now)

directions_result = gmaps.distance_matrix([(12.985805, 77.737007),(12.985805,77.737007)],[(12.992220,77.715910),(12.970853,77.715910)],
                                     mode="driving",
                                     departure_time=now)

print(directions_result)