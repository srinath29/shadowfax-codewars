'''
World creation for rider optimization.
'''

import pants
import math
import pandas as pd
from utils.utils import Helper


class RiderOptimization:
    def get_time_dict(self, source, client):
        time_dict = {}
        for s in range(len(source)):
            key = Helper.prepare_lat_lon_string(source[s], client[s])
            value = Helper.getTimeGmaps(source[s], client[s])
            time_dict[key] = value
        return time_dict

    def getTimeDf(self, timeDict):
        timeDf = pd.DataFrame()
        indLi = []
        for key in timeDict:
            indLi.append(key)
            subLi = []
            for subKey in timeDict:
                if key == subKey:
                    val = 0
                else:
                    newSource = (Helper.decode_lat_lon_string(key).group("lat2"), Helper.decode_lat_lon_string(key).group("lon2"))
                    newDestination = (Helper.decode_lat_lon_string(subKey).group("lat1"), Helper.decode_lat_lon_string(subKey).group("lon1"))
                    time = Helper.getTimeGmaps(newSource, newDestination)
                    val  = timeDict[key] + timeDict[subKey] + time
                subLi.append(val)
            timeDf[key] = pd.Series(subLi)
        timeDf.index = indLi
        return timeDf


if __name__ == '__main__':
    riderOptimization = RiderOptimization()
    source_lat_lon_list=[]
    client_lat_lon_list=[]

    riderOptimization.get_time(source_lat_lon_list, client_lat_lon_list)