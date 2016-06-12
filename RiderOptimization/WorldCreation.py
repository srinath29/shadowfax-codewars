'''
World creation and rider path allocation optimization technique.
'''

import pants
import pandas as pd
from utils.utils import Helper
from time import time


class RiderOptimization:

    def __init__(self, source, client):
        self.helperObj = Helper()
        start = time()
        self.timeDf = self.getTimeDf(self.get_time_dict(source, client))
        end = time()
        print("Network IO's time is {}".format(end - start))

    def findOptimalSolutions(self):
        nodes = list(self.timeDf.columns)
        world = pants.World(nodes, self.calculateLength)
        solver = pants.Solver()
        sol = solver.solve(world)
        sols = solver.solutions(world)
        print("****************")
        print(sol.distance)
        print("****************")
        print(self.beautifyLatLon(sol.tour))
        print("****************")
        print(sol.path)
        print("***********\n**********\n########")
        for s in sols:
            print(s.distance)


    def beautifyLatLon(self, stringLatLonList):
        trail = []
        for stringLatLon in stringLatLonList:
            lat_lon_group = self.helperObj.decode_lat_lon_string(stringLatLon)
            source = (lat_lon_group.group("lat1"), lat_lon_group.group("lon1"))
            destination = (lat_lon_group.group("lat2"), lat_lon_group.group("lon2"))
            trail.append(source)
            trail.append(destination)

        return trail

    def get_time_dict(self, source, client):
        time_dict = {}
        for s in range(len(source)):
            key = self.helperObj.prepare_lat_lon_string(source[s], client[s])
            value = self.helperObj.getTimeGmaps(source[s], client[s])
            time_dict[key] = value
        return time_dict

    def getTimeDf(self, timeDict):
        '''
        Cretaes a data frame matrix which aids in finding length of a path.
        :param timeDict:
        :return:
        '''
        timeDf = pd.DataFrame()
        indLi = []
        for key in timeDict:
            indLi.append(key)
            subLi = []
            for geohash, time_val in timeDict.items():
                if key == geohash:
                    total_time = 0
                else:
                    newSource = (self.helperObj.decode_lat_lon_string(key).group("lat2"), self.helperObj.decode_lat_lon_string(key).group("lon2"))
                    newDestination = (self.helperObj.decode_lat_lon_string(geohash).group("lat1"), self.helperObj.decode_lat_lon_string(geohash).group("lon1"))
                    time = self.helperObj.getTimeGmaps(newSource, newDestination)
                    total_time  = timeDict[key] + time_val + time
                subLi.append(total_time)
            timeDf[key] = pd.Series(subLi)
        timeDf.index = indLi
        return timeDf

    def calculateLength(self, n1, n2):
        return self.timeDf.ix[n1,n2]



if __name__ == '__main__':
    start = time()
    destination = [(12.931280000000001, 77.686239999999998),
                     (12.9337, 77.662199999999999),
                     (12.9353, 77.690899999999999)]
    source = [(12.925975583315498, 77.675335407257094),
             (12.925975583315498, 77.675335407257094),
             (12.925975583315498, 77.675335407257094)]
    riderOptimization = RiderOptimization(source, destination)
    riderOptimization.findOptimalSolutions()
    end = time()
    print("Time taken for total is {}".format(end-start))
