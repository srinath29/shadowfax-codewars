import googlemaps
import datetime
import json
from utils.utils import Helper
gmaps = googlemaps.Client(key = "AIzaSyCTVcmF2m7PGO1UgEEv9Mfn-Vo0XbA5XYY")

now = datetime.datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
# directions_result = gmaps.directions((12.985805, 77.737007),(12.992220,77.715910),
#                                      mode="driving",
#                                      departure_time=now)


h1 = Helper()
directions_result = h1.getDistanceDataFrame((12.985805, 77.737007),(12.992220,77.715910))

print(directions_result[0][0])