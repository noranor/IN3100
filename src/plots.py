#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Written by Nicholas Karlsen
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


def initData(path="../data/soekere_pr_omraade/"):
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

data, fields = initData()

for f in fields:
    plt.plot(data[f][0], data[f][1], "o--", label=f)

plt.xlabel("Year")
plt.ylabel("Number of applicants")
plt.legend()

plt.show()