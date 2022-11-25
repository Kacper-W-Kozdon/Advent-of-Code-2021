# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:30:15 2022

@author: xBubblex
"""

import numpy as np
import re

def load_files():
    fContent = []
    with open("input6.txt") as f:
            for (lineIndex, line) in enumerate(f):  #loading the file into an np.array
                if bool(line.strip("\n").split()):
                    fContent.append(re.split(",", line.strip("\n")))  #splitting each entry into coordinates
    fContent = (np.array(fContent).astype(int))[0]  #an array of coordinates: x1, y1, x2, y2; values are strings
    return(fContent, fContent.shape)

def n_new_fish(tab):
    num_new_fish = sum((tab == 0).astype(int))
    # print("No. of new fish2: ", num_new_fish)
    return num_new_fish

def add_new_fish(tab):
    new_fish_cyc = 8
    num_new_fish = n_new_fish(tab)
    # print(len(tab))
    tab = np.append(tab, [new_fish_cyc for index in range(num_new_fish)])
    # print(len(tab))
    # print("No. of new fish3: ", len([new_fish_cyc for index in range(num_new_fish)]))
    return tab

def age_fish(tab, maxage = 81):
    newage = maxage - 1
    notParents = np.where(tab != 0)
    if newage == 0:
        # print(newage)
        return tab
    if 0 in tab:
        # print("No. of new fish1: ", sum((tab == 0).astype(int)))
        tab = add_new_fish(tab)
        # print(len(tab[np.where(tab == 0)]))
        tab[np.where(tab == 0)] = 6
        # print(len(tab[np.where(tab == 6)]))
    tab[notParents] = tab[notParents] - 1
    # tab = age_fish(tab, newage)
    # print(newage)
    return age_fish(tab, newage)

def flatten(l):
    return [item for sublist in l for item in sublist]

def age_fish2(tabs, maxage = 81):
    for age in range(maxage):
        print("age: ", age)
        age = maxage - 1
        maxsize = 512
        # print(tabs)
        tabsClone = np.copy(tabs)
        
        for (index, tab) in enumerate(tabsClone):
            tab = np.array(tab)
            # print(np.array(tab) != 0)
            notParents = np.where(tab != 0)
            # print(notParents)
            if 0 in tab:
                # print("0 in tab")
                # print("No. of new fish1: ", sum((tab == 0).astype(int)))
                tab = add_new_fish(tab)
                # print(tab)
                # print(len(tab[np.where(tab == 0)]))
                tab[np.where(tab == 0)] = 6
                # print(len(tab[np.where(tab == 6)]))
            # print("shape: ", tab.shape)
            tab[notParents] = tab[notParents] - 1
            # tabs = np.array(tabs)
            # print(tabs.shape)
            # print(tabs[0])
            # tabs = np.delete(tabs, [index], 0)
            tabs.pop(index)
            # print("Shape: ", tabs.shape)
            # tabs = np.append(tabs, np.array([tab]), 0)
            # tabs = tabs.append(tab)
            tabs.insert(index, tab)
            # print()
            # print(len(tab))
            if len(tab) > maxsize:
                # print("New batch")
                # tabs = np.append(tabs, [tab[maxsize:]])
                tabs.append(tab[maxsize:])
                tab = tab[:maxsize]
                # tabs = np.delete(tabs, index)
                tabs.pop(index)
                # tabs = np.append(tabs, np.array([tab]))
                tabs.insert(index, tab)
            # tab = age_fish(tab, newage)
            # print(newage)
            
    return tabs

def run1(age):
    fContent = np.array([load_files()[0]]).tolist()
    # print(np.where(fContent != 0))
    # print(fContent, load_files()[1])
    fin_popul = age_fish(tabs = fContent, maxage = age)
    # print(fin_popul)
    fin_pop_size = len(fin_popul)
    print("Population size after " + str(age - 1) + " days: ")
    return fin_pop_size

def run2(age):
    fContent = np.array([load_files()[0]]).tolist()
    # print(np.where(fContent != 0))
    # print(fContent, load_files()[1])
    fin_popul = age_fish2(tabs = fContent, maxage = age)
    # print(fin_popul)
    fin_pop_size = len(fin_popul)
    print("Population size after " + str(age - 1) + " days: ")
    return fin_pop_size

print(run1(81))
print(run2(257))