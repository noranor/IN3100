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
data_capacity, fields_capacity = initData(path="../data/studieplasser_pr_omraade/")

# Beware of spaghetti code.

# Fetch length of array from arbitrary list (all are same lenght anyway)
totApplicants = np.zeros(len(data_applicants["JUS"][1]))
# itterate through all lists
for f in fields_applicants:
    # for each one, ++ number of applicants to i-th year
    for i, val in enumerate(data_applicants[f][1]):
        totApplicants[i] += val

for f in fields_applicants:
    fig = plt.figure(figsize=(8, 8))

    plt.subplot(2, 2, 1)
    plt.plot(data_applicants[f][0], 100 * np.array(data_applicants[f][1]) / totApplicants, "o--")
    plt.xlabel("År")
    plt.ylabel("% Antall søkere [Antall søkere / Totalt antall søkere]")

    plt.subplot(2, 2, 2)
    plt.plot(data_applicants[f][0], np.array(data_applicants[f][1]) / np.array(data_capacity[f][1]), "o--")
    plt.xlabel("År")
    plt.ylabel("Antall søkere / Antall studieplasser")

    plt.subplot(2, 2, 3)
    plt.plot(data_capacity[f][0], data_capacity[f][1], "o--")
    plt.xlabel("År")
    plt.ylabel("Antall studieplasser")
    
    plt.subplot(2, 2, 4)
    plt.plot(data_applicants[f][0], data_applicants[f][1], "o--")
    plt.xlabel("År")
    plt.ylabel("Antall søkere")

    plt.suptitle(f)

    fig.tight_layout()


    plt.savefig("../figs/" + f + ".png")
    plt.close()
