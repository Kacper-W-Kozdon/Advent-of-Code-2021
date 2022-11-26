# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 13:50:42 2022

@author: xBubblex
"""

import numpy as np
import re
import time

def load_files():
    fContent = []
    with open("input8.txt") as f:
            for (lineIndex, line) in enumerate(f):  #loading the file into an np.array
                if bool(line.strip("\n").split()):
                    # print(line.strip("\n").split("|"))
                    fContent.append(line.strip("\n").split(" | "))  #splitting each entry into coordinates
    return(fContent)

def data_preprocessing1(tab):
    # print(tab)
    # print(tab)
    for (idx, el) in enumerate(tab):
        # print(el)
        tab[idx] = el.split(" ")
        # print(el)
    return tab

def count_uniques(data):
    unique_values = [2, 4, 3, 7]
    # unique_values_sum = {"1": 0, "4": 0, "7": 0, "8": 0}
    uniques = []
    num_lines = lambda x: len(x)
    for line in data:
        # print(list((map(num_lines, line))))
        uniques.append(list((map(num_lines, line))))
        # print(uniques)
    uniques = np.array(uniques)
    # print(uniques)
    for (index, el) in enumerate(unique_values):
        unique_values[index] = sum((uniques == el).astype(int))
    total_uniques = sum(unique_values)
    return total_uniques

def data_processing2(data):
    fContent = data
    for (index, line) in enumerate(fContent):
        # print(line)
        # print(data_preprocessing1(line))
        # if index == 10:
            # break
        fContent[index] = data_preprocessing1(line)
    fContent = np.array(fContent, dtype = object)
    return fContent

def run():
    fContent = load_files()
    processed_data = data_processing2(data = fContent)
    inputs = processed_data[:, 0]
    outputs = processed_data[:, 1]
    total_uniques = count_uniques(data = outputs)
    # print(len(outputs[0][1]))
    return total_uniques
# print(load_files()[0])
# print(data_preprocessing(load_files())[1])
print(run())