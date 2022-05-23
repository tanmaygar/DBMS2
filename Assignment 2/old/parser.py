import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math
import sys
import os
import time
import random
import csv
import pandas as pd
import time

start_time = time.time()
f = open("source.txt", "r", encoding="utf-8")
op = open("names.txt", "w", encoding="utf-8")
count = 0
while True:
    line = f.readline()
    count = count + 1
    if not line:
        break
    if line[0] == '#' and line[1] == '@':
        op.write(line[2:])
        #print("Line{}: {}".format(count, line.strip()))

print(time.time() - start_time)
    
