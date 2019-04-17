#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 16:42
# @Author  : yang xin
# @File    : show_plot.py
# @Software: PyCharm

import numpy as np
from matplotlib import pyplot as plt

p = np.arange(0.01, 1.01, 0.01)
# y = np.power(p, 2)
y = np.array([((i - 0.5) ** 2 + np.random.rand()) / 4 + 0.3 for i in p])

plt.figure()
plt.plot(p, y)
plt.xlabel("similarity_threshold")
plt.ylabel("objective")
plt.show()
