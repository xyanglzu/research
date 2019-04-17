#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 16:42
# @Author  : yang xin
# @File    : show_plot.py
# @Software: PyCharm

import numpy as np
from matplotlib import pyplot as plt

datapath = "/Users/xiny/Desktop/data/crossover/"
fitness = []
for i in range(1, 101):
    filename = str(i) + "_" + "1_50/" + "1.txt"
    filename = datapath + filename

    with open(filename, "r") as f:
        file_data = f.readlines()
    fitness.append(float(file_data[-1].split("\t")[1]))

fitness = np.array(fitness)
print fitness.argmin(), fitness.min()

mutate = np.arange(0.01, 1.01, 0.01)
plt.figure()
plt.plot(mutate, fitness)
plt.xlabel("crossover_probability")
plt.ylabel("fitness")
plt.show()
