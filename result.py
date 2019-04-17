#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 16:42
# @Author  : yang xin
# @File    : show_plot.py
# @Software: PyCharm

import os

import numpy as np

datapath = "/Users/xiny/IdeaProjects/vrlp/src/main/java/edu/scut/emos/vrlp/output/"
result = []
for i in range(1, 9):
    for j in range(50, 250, 50):
        for k in range(1, 11):
            filename = str(i) + "_" + str(j) + "/" + str(k) + ".txt"
            filename = datapath + filename

            if not os.path.exists(filename):
                continue
            fitness = []
            with open(filename, "r") as f:
                file_data = f.readlines()
            fitness.append(float(file_data[-1].split("\t")[2]))
        fitness = np.array(fitness)
        result.append(fitness.mean())

print result
