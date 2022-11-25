# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:30:15 2022

@author: xBubblex
"""

import numpy as np
import re
import time

def load_files():
    fContent = []
    with open("input6.txt") as f:
            for (lineIndex, line) in enumerate(f):  #loading the file into an np.array
                if bool(line.strip("\n").split()):
                    fContent.append(re.split(",", line.strip("\n")))  #splitting each entry into coordinates
    fContent = (np.array(fContent).astype(int))[0]  #an array of coordinates: x1, y1, x2, y2; values are strings
    return(fContent, fContent.shape)

def n_new_fish(tab):
    num_new_fish = sum((tab == 0).astype(np.ushort))
    # print("No. of new fish2: ", num_new_fish)
    return num_new_fish

def add_new_fish(tab):
    new_fish_cyc = np.ushort(8)
    num_new_fish = n_new_fish(tab)
    # print(len(tab))
    tab = np.append(tab, [new_fish_cyc for index in range(num_new_fish)]).astype(np.ushort)
    # print(len(tab))
    # print("No. of new fish3: ", .cclen([new_fish_cyc for index in range(num_new_fish)]))
    return tab

def age_fish(tab, maxage = 81):
    newage = maxage - 1
    notParents = np.where(tab != 0)
    # print(notParents) if newage == 80 else 0
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
    tabs.sort()
    tabs = np.array(tabs, dtype = np.ushort)
    for age in range(maxage):
        t1 = time.time()
        print("age: ", age)
        age = maxage - 1

        tabs = tabs - 1
        safety = True
        try: 
            (tabs.tolist().index(0))
        except ValueError:
            safety = False
        if safety:
            lim = tabs.tolist().index(0)
            tabs = np.delete(tabs, range(lim))
            # tabs = tabs + np.array([6 for i in range(lim)], dtype = np.ushort)
            # tabs = tabs + np.array([8 for i in range(lim)], dtype = np.ushort)
            tabs = np.concatenate((tabs, np.array([6 for i in range(lim)], dtype = np.ushort)))
            tabs = np.concatenate((tabs, np.array([8 for i in range(lim)], dtype = np.ushort)))
        # print(lim)
        
        # print(tabs)
        
        t2 = time.time()
        print("runtime: ", (t2 - t1))
            
    return tabs

def age_fish3(tabs, maxage = 81):
    tabs.sort()
    tabs = np.array(tabs, dtype = np.ushort)
    tabsD = {"0": sum((tabs == 0).astype(float)),
             "1": sum((tabs == 1).astype(float)),
             "2": sum((tabs == 2).astype(float)),
             "3": sum((tabs == 3).astype(float)),
             "4": sum((tabs == 4).astype(float)),
             "5": sum((tabs == 5).astype(float)),
             "6": 0,
             "7": 0,
             "8": 0}
    print(tabsD)
    # print(maxage)
    for age in range(maxage):
        t1 = time.time()
        print("age: ", age) if not age%50 else 0
        age = maxage - 1
        tempKeyVal = 0
        for key in tabsD.keys():
            if key == "0":
                # print(key)
                tempKeyVal = tabsD[key]
                tabsD[key] = tabsD[str(int(key) + 1)]
            elif key == "8":
                tabsD[key] = tempKeyVal
                tabsD["6"] = tabsD["6"] + tempKeyVal
            else:
                tabsD[key] = tabsD[str(int(key) + 1)]
        # print(tabsD)
        # print(lim)
        
        # print(tabs)
        
        t2 = time.time()
        # print("runtime: ", (t2 - t1))
            
    return tabsD

def run1(age):
    fContent = np.array(load_files()[0]).astype(np.ushort())
    # print(np.where(fContent != 0))
    # print(fContent, load_files()[1])
    fin_popul = age_fish(tab = fContent, maxage = age)
    # print(fin_popul)
    fin_pop_size = len(fin_popul)
    print("Population size after " + str(age - 1) + " days: ")
    return fin_pop_size

def run2(age):
    fContent = np.array(load_files()[0]).astype(np.ushort).tolist()
    # print(np.where(fContent != 0))
    # print(fContent, load_files()[1])
    fin_popul = age_fish3(tabs = fContent, maxage = age)
    # print(fin_popul)
    fin_pop_size = 0
    for key in fin_popul.keys(): 
        fin_pop_size = fin_pop_size + fin_popul[key]
    print("Population size after " + str(age - 1) + " days: ")
    return fin_pop_size


print(run1(81))
print(run2(256))