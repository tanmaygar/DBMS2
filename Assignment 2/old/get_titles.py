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
import collections

start_time = time.time()
f = open("source.txt", "r", encoding="utf-8")
op = open("names.txt", "w", encoding="utf-8")
rep_titles = open("rep_titles.txt", "w", encoding="utf-8")
list_titles = []
count = 0
while True:
    line = f.readline()
    count = count + 1
    if not line:
        break
    if line[0] == '#' and line[1] == '*':
        list_titles.append(line[2:])
        #print("Line{}: {}".format(count, line.strip()))

# print(len(list_titles))
# print(len(set(list_titles)))
freq = collections.Counter(list_titles)
freq_dict = dict(freq)
for key, value in freq_dict.items():
    if value > 1:
        rep_titles.write(key + '\n')
print(time.time() - start_time)
