#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 16:42
# @Author  : yang xin
# @File    : show_plot.py
# @Software: PyCharm

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


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


def read(filename):
    return np.loadtxt(filename)


if __name__ == "__main__":
    # filename = "/Users/xiny/IdeaProjects/vrlp/ssdrc/main/java/edu/scut/emos/vrlp/output/vlrp/main.txt"
    # data = read(filename)
    # ax = create3D(data[0][0], data[0][1], data[0][2])
    # for i in range(1, len(data)):
    #     rectangle(ax, data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5])
    # plt.show()

    # ax = create3D(200, 400, 300)
    # rectangle(ax, 200, 400, 300, 0, 0, 0, [1, 1, 1])
    # rectangle(ax, 100, 200, 100, 0, 0, 0)
    # ax.set_ylim(0, 500)
    # ax.invert_yaxis()
    # xs = [100, 0, 0]
    # ys = [0, 200, 0]
    # zs = [0, 0, 100]
    # ax.scatter(xs, ys, zs, s=50, color='r', marker='o')

    # rectangle(ax, 100, 400, 300, 100, 0, 0, [0.1, 0.1, 0.1])
    # rectangle(ax, 200, 200, 300, 0, 200, 0, [0.1, 0.1, 0.1])
    # rectangle(ax, 100, 200, 200, 0, 0, 100, [0.1, 0.1, 0.1])
    # plt.show()

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_zlim(0, 3)

    # ax.set_ylabel("Length")
    # ax.set_xlabel("Width")
    # ax.set_zlabel("Height")
    #
    # container_length = 5
    # container_width = 4
    # container_height = 3
    #
    # ax.set_xlim(0, float(container_width))
    # ax.set_zlim(0, float(container_height))
    # ax.invert_yaxis()
    #
    # rectangle(ax, container_width, container_length, container_height, 0, 0, 0, color=[1, 1, 1])

    ax.invert_yaxis()
    ax.axis("off")
    rectangle(ax, 1, 1, 1, 0, 0, 0)
    rectangle(ax, 3, 3, 0.0001, -1, -1, 1, color=[0, 0, 0])
    rectangle(ax, 3, 3, 0.0001, -1, -1, 0, color=[0, 0, 0])

    # item_width, item_length, item_height = 1, 2, 1
    # item_x, item_y, item_z = 0, 0, 0
    # rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z)

    # item_width, item_length, item_height = 1, 2, 2
    # item_x, item_y, item_z = 0, 0, 1
    # rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z, color=[0,0,0])
    # #
    # item_width, item_length, item_height = 3, 3, 3
    # item_x, item_y, item_z = 1, 0, 0
    # rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z)
    # #
    # item_width, item_length, item_height = 4, 3, 3
    # item_x, item_y, item_z = 0, 2, 0
    # rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z, color=[0,0,0])

    # item_width, item_length, item_height = 3, 5, 3
    # item_x, item_y, item_z = 1, 0, 0
    # rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z, color=[0, 0, 0])

    # item_width, item_length, item_height = 1, 2, 1
    # item_x, item_y, item_z = 0, 0, 0
    # rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z)
    #
    # item_width, item_length, item_height = 1, 2, 1
    # item_x, item_y, item_z = 1, 0, 0
    # rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z)
    #
    # rectangle(ax, 1, 2, 2, 0, 0, 1, color=[0, 0, 0])
    # rectangle(ax, 1, 2, 2, 1, 0, 1, color=[0, 0, 0])
    # rectangle(ax, 3, 1, 3, 1, 3, 0, color=[1, 1, 0])

    # # 左
    # item_width, item_length, item_height = 1, 5, 3
    # item_x, item_y, item_z = 0, 0, 0
    # rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z, color=[0, 0, 0])
    #
    # # 右
    # item_width, item_length, item_height = 2, 5, 3
    # item_x, item_y, item_z = 2, 0, 0
    # rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z, color=[0, 0, 0])

    # # 前
    # item_width, item_length, item_height = 4, 2, 3
    # item_x, item_y, item_z = 0, 3, 0
    # rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z, color=[0, 0, 0])
    #
    # # 后
    # item_width, item_length, item_height = 4, 1, 3
    # item_x, item_y, item_z = 0, 0, 0
    # rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z, color=[0, 0, 0])

    # 上
    # item_width, item_length, item_height = 1, 2, 2
    # item_x, item_y, item_z = 1, 1, 1
    # rectangle(ax, item_width, item_length, item_height, item_x, item_y, item_z, color=[0, 0, 0])

    plt.show()
