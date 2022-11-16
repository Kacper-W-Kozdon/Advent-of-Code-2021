# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:15:55 2022

@author: xBubblex
"""

import numpy as np

fContent = []
with open("input2.txt") as f:
    for line in f:  #loading the file into a np.array
        fContent.append(str(line).split())  #separating the keywords from the values
fContent = np.array(fContent)  #table of horizontal and vertical measurements
sumHorizontal = sum((fContent[:, 0] == "forward").astype(int) * fContent[:, 1].astype(int))  #selecting horizontal movement from the table and summing the values
sumDown = sum((fContent[:, 0] == "down").astype(int) * fContent[:, 1].astype(int))  #same as horizontal, but for down and up
sumUp = sum((fContent[:, 0] == "up").astype(int) * fContent[:, 1].astype(int))  
sumVertical = sumDown - sumUp 
print(sumHorizontal * sumVertical)
aim = ((fContent[:, 0] == "down").astype(int) * 2 - 1) * (fContent[:, 0] != "forward").astype(int) * fContent[:, 1].astype(int)  #simplifying aim to have +/- for down/up
forward = (fContent[:, 0] == "forward").astype(int) * fContent[:, 1].astype(int)  #choosing forward values
#for (idx, value) in enumerate(aim):  #rewriting aim to have a sum of all previous entries for each entry (total aim at that point)
#    if idx != 0:
#        aim[idx] = aim[idx] + aim[idx - 1]
#totalAim = [sum(aim[:idx]) for idx in range(aim.shape[0])]
totalAim = np.cumsum(aim)
sumHorizontal2 = sum(forward)
sumVertical2 = sum(forward * totalAim)
print(sumVertical2 * sumHorizontal2)

#1488311643