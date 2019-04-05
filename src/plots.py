#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Written by Nicholas Karlsen
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import os


def parseFile(filename):
    inFile = open(filename, 'r')
    year = int(inFile.readline())  # First line should be the year, which is an integer
    field = []  # i.e law, science.
    N = []  # number of applicants

    for line in inFile:
        line = line.split(",")
        field.append(line[0].strip())
        N.append(int(line[1]))

    return year, field, N


def parseFolder(path):
    filenames = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            filenames.append(filename)

    return filenames


def initData(path):
    filenames = parseFolder(path)

    numFiles = len(filenames)
    data = {}
    # Set up dictionary using first file
    y, f, N = parseFile(path + filenames[0])

    for entry in f:
        data.update({entry: [[], []]})
    # Populate dict
    filenames = sorted(filenames)
    for fn in filenames:
        year, field, N = parseFile(path + fn)
        for i, entry in enumerate(f):
            data[entry][0].append(year)
            data[entry][1].append(N[i])

    return data, f


data_applicants, fields_applicants = initData(path="../data/soekere_pr_omraade/")

for f in fields_applicants:
    plt.plot(data_applicants[f][0], data_applicants[f][1], "o--", label=f)

plt.xlabel("Year")
plt.ylabel("Number of applicants")
plt.legend()

plt.show()


data_capacity, fields_capacity = initData(path="../data/studieplasser_pr_omraade/")

for f in fields_capacity:
    plt.plot(data_capacity[f][0], data_capacity[f][1], "o--", label=f)

plt.xlabel("Year")
plt.ylabel("Number of applicants")
plt.legend()

plt.show()


for f in fields_applicants:
    plt.plot(data_applicants[f][0], np.array(data_applicants[f][1]) / np.array(data_capacity[f][1]), "o--", label=f)

plt.xlabel("Year")
plt.ylabel("Applicants / Capacity")
plt.legend()
plt.show()

# TODO Divite num applicants per field by number of applicants THAT year
