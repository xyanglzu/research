#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 11:27
# @Author  : yang xin
# @File    : save_plot.py
# @Software: PyCharm
import sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import pyplot as plt
import pickle


def rectangle(ax, width, length, height, point_x, point_y, point_z, color=[0.5, 0.5, 1]):
    x = [point_x, point_x, point_x + width, point_x + width, point_x, point_x, point_x + width, point_x + width]
    y = [point_y, point_y, point_y, point_y, point_y + length, point_y + length, point_y + length, point_y + length]
    z = [point_z, point_z + height, point_z + height, point_z, point_z, point_z + height, point_z + height, point_z]

    vertices = [[0, 1, 2, 3], [2, 3, 7, 6], [4, 5, 6, 7], [0, 1, 5, 4], [1, 2, 6, 5], [0, 3, 7, 4]]
    tupleList = list(zip(x, y, z))

    poly3d = [[tupleList[vertices[ix][iy]] for iy in range(len(vertices[0]))] for ix in range(len(vertices))]
    ax.scatter(x, y, z)
    collection = Poly3DCollection(poly3d, edgecolors='black', linewidths=1, alpha=0.2)
    collection.set_facecolor(color)
    ax.add_collection3d(collection)


def read(filename):
    return np.loadtxt(filename)


def create3D(width, length, height):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_ylabel("Length")
    ax.set_xlabel("Width")
    ax.set_zlabel("Height")

    ax.set_xlim(0, width)
    ax.set_zlim(0, height)
    ax.invert_yaxis()
    return ax


if len(sys.argv) >= 1:
    # data = read(sys.argv[1])

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_ylabel("Length")
    ax.set_xlabel("Width")
    ax.set_zlabel("Height")

    filename = sys.argv[1]
    container_width, container_length, container_height = sys.argv[2].split(",")

    ax.set_xlim(0, float(container_width))
    ax.set_zlim(0, float(container_height))
    ax.invert_yaxis()

    for i in range(3, len(sys.argv)):
        item_info = sys.argv[i].split(",")
        if len(item_info) == 6:
            item_width, item_length, item_height, item_x, item_y, item_z = map(float, item_info)
            rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z)
        elif len(item_info) == 9:
            item_width, item_length, item_height, item_x, item_y, item_z, r, g, b = map(float, item_info)
            rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z, [r, g, b])
        else:
            raise RuntimeError("item信息为width, length, height, x, y, z [r, g, b]")

    path = "/Users/xiny/IdeaProjects/vrlp/src/main/java/edu/scut/emos/vrlp/output/fig/" + filename
    print("save start and path = " + path)
    with open(path, 'wb') as f:
        pickle.dump(fig, f)
    print("save finished.")
else:
    raise RuntimeError("缺少命令行参数.")
