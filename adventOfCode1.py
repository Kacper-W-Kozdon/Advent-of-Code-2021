# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:49:35 2022

@author: xBubblex
"""

import numpy as np

fContent = []
with open("D:\Dokumenty\Python\Advent of Code 2021\input1.txt") as f:
    for line in f:  #loading the file into a np.array
        fContent.append(int(line))
fContent = np.array(fContent)  #table of measutements
numOfIncrs = sum((fContent[1:] - fContent[:-1] > 0).astype(int))  #number of measurements larger than the previous one
print(numOfIncrs)
triple1 = fContent[:-3] + fContent[1:-2] + fContent[2:-1]
triple2 = fContent[1:-2] + fContent[2:-1] + fContent[3:]
numOfIncrs2 = sum((triple2 - triple1 > 0).astype(int))  #number of 3-element sums of measurements larger than the previous triplet
print(numOfIncrs2)