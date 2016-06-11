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


if __name__ == '__main__':
    riderOptimization = RiderOptimization()
    source_lat_lon_list=[]
    client_lat_lon_list=[]

    riderOptimization.get_time(source_lat_lon_list, client_lat_lon_list)