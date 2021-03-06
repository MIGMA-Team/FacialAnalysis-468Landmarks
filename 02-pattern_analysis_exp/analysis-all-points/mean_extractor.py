import pandas as pd
import numpy as np
from tqdm import tqdm
import math
from multiprocessing import Process


from distances_module import MaskDistances
from MaskStats_module import MaskStats
from inspect import getsourcefile
import os.path
import sys
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)
from definitions import *



if __name__ == "__main__":
    
    users = os.listdir(PATTERN_TEST_PATH)
    saves = []
    for i in range(8):
        for j in range(2):
            saves.append(MaskStats(i,j))
    
    for user in tqdm(users):
        arqs = os.listdir(PATTERN_TEST_PATH+"/"+user)
        for arq in arqs:
            if(arq.split(".")[1] != "csv"):
                continue

            df = pd.read_csv(PATTERN_TEST_PATH+"/"+user+"/"+arq)
            for i in range(len(saves)):
                if(saves[i].verify_mask_type(arq)):
                    saves[i].add_distances(df)
                    break
    for i in range(len(saves)):
        saves[i].calculate_dist_means()
        saves[i].save_dataframe()