'''
World creation for rider optimization.
'''

import pants
import math
import pandas as pd
from utils.utils import Helper


class RiderOptimization:

    def __init__(self, source, client):
        self.helperObj = Helper()

        self.timeDf = self.getTimeDf(self.get_time_dict(source, client))
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
            k = self.helperObj.decode_lat_lon_string(stringLatLon)
            source = (k.group("lat1"), k.group("lon1"))
            destination = (k.group("lat2"), k.group("lon2"))
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
            for subKey in timeDict:
                if key == subKey:
                    val = 0
                else:
                    newSource = (self.helperObj.decode_lat_lon_string(key).group("lat2"), self.helperObj.decode_lat_lon_string(key).group("lon2"))
                    newDestination = (self.helperObj.decode_lat_lon_string(subKey).group("lat1"), self.helperObj.decode_lat_lon_string(subKey).group("lon1"))
                    time = self.helperObj.getTimeGmaps(newSource, newDestination)
                    val  = timeDict[key] + timeDict[subKey] + time
                subLi.append(val)
            timeDf[key] = pd.Series(subLi)
        timeDf.index = indLi
        return timeDf

    def calculateLength(self, n1, n2):
        return self.timeDf.ix[n1,n2]



if __name__ == '__main__':
    destination = [(12.931280000000001, 77.686239999999998),
                     (12.9337, 77.662199999999999),
                     (12.9337, 77.662199999999999),
                     (12.9337, 77.662199999999999),
                     (12.9337, 77.662199999999999),
                     (12.9353, 77.690899999999999),
                     (12.93561, 77.702280000000002),
                     (12.9337, 77.662199999999999),
                     (12.91029, 77.645020000000002),
                     (12.93561, 77.702280000000002),
                     (12.91042, 77.685140000000004),
                     (12.9353, 77.690899999999999),
                     (12.9337, 77.662199999999999),
                     (12.9337, 77.662199999999999),
                     (12.9337, 77.662199999999999)]
    source = [(12.925975583315498, 77.675335407257094),
             (12.925975583315498, 77.675335407257094),
             (12.925975583315498, 77.675335407257094),
             (12.925975583315498, 77.675335407257094),
             (12.925975583315498, 77.675335407257094),
             (12.925975583315498, 77.675335407257094),
             (12.925975583315498, 77.675335407257094),
             (12.925975583315498, 77.675335407257094),
             (12.92608819, 77.671467489999998),
             (12.92608819, 77.671467489999998),
             (12.92608819, 77.671467489999998),
             (12.92608819, 77.671467489999998),
             (12.925975583315498, 77.675335407257094),
             (12.925975583315498, 77.675335407257094),
             (12.925975583315498, 77.675335407257094)]
    riderOptimization = RiderOptimization(source, destination)
