#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 11:33
# @Author  : yang xin
# @File    : load_plot.py
# @Software: PyCharm

import pickle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

if __name__ == "__main__":
    plt.ioff()
    filesname = os.listdir("/Users/xiny/IdeaProjects/vrlp/src/main/java/edu/scut/emos/vrlp/output/fig/")
    filesname.sort()

    if len(filesname) > 0:
        for name in filesname:
            # if name == "40.fig.pickle":
            with open('/Users/xiny/IdeaProjects/vrlp/src/main/java/edu/scut/emos/vrlp/output/fig/' + name, 'rb') as f:
                fig = pickle.load(f)
            plt.show()

