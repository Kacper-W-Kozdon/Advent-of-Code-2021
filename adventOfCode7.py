# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 01:05:48 2022

@author: xBubblex
"""

import numpy as np
import re
import time

def load_files():
    fContent = []
    with open("input7.txt") as f:
            for (lineIndex, line) in enumerate(f):  #loading the file into an np.array
                if bool(line.strip("\n").split()):
                    fContent.append(re.split(",", line.strip("\n")))  #splitting each entry into coordinates
    fContentSet = set(np.array(fContent[0]).astype(int))
    fContent = np.array(fContent).astype(int)[0]  #an array of coordinates: x1, y1, x2, y2; values are strings
     
    return(fContent, fContentSet, fContent.shape)

def fuel_cost2(crabs, position):
    crabs = np.array(crabs)
    # positionChangeCost = sum([index for index in range(position + 1)])
    # print(position, positionChangeCost)
    cost = sum(sum([cost for cost in range(crabCost + 1)]) for crabCost in np.absolute(crabs - position))
    # print("Method 2")
    return cost

def fuel_cost(crabs, position):
    crabs = np.array(crabs)
    cost = sum(np.absolute(crabs - position))
    # print("Method 1")
    # print(cost)
    return cost

def total_fuel_costs(crabs, positions, method = 1):
    total_fuel_costs = np.zeros(len(positions))
    if method == 1:
        for (index, position) in enumerate(positions):
            # print("Method 1")
            total_fuel_costs[index] = fuel_cost(crabs, int(position))
    else:
            # print("Method 2")
        for (index, position) in enumerate(positions):
            total_fuel_costs[index] = fuel_cost2(crabs, int(position))
    return total_fuel_costs
    
def run(method = 1):
    meth = method
    crabs = load_files()[0]
    positions = load_files()[1]
    # print(positions)
    costs = total_fuel_costs(crabs, positions, method = meth)
    # print(costs)
    min_cost = min(costs)
    return min_cost
    
# print(np.zeros(6))
# print(len(set([1, 1, 2])))
# print([index for index in range(9)])
print(run())
print(run(method = 2))
print(sum([index for index in range(4)]))