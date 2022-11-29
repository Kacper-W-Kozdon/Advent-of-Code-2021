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
    uniqueValues = [2, 4, 3, 7]  #No. of lines in a digit
    uniqueValues2 = [1, 4, 7, 8]  #Digit's value
    # unique_values_sum = {"1": 0, "4": 0, "7": 0, "8": 0}
    uniques = []
    numLines = lambda x: len(x)
    for line in data:
        # print(list((map(num_lines, line))))
        uniques.append(list((map(numLines, line))))
        # print(uniques)
    uniques = np.array(uniques)
    # print(uniques)
    # print(uniques)
    uniqueValuesTab = np.zeros((data.shape[0], len(data[0])))
    # print(uniqueValuesTab)
    for (index, el) in enumerate(uniqueValues):
        # print(uniqueValuesTab[index])
        # print((uniques == el).astype(int) * el)
        uniqueValues[index] = sum((uniques == el).astype(int))
        uniqueValuesTab = uniqueValuesTab + (uniques == el).astype(int) * uniqueValues2[index]
        # print((uniques == el).astype(int) * el)
    # print(uniqueValuesTab)
    totalUniques = sum(uniqueValues)
    return totalUniques, uniqueValuesTab

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

def decoding(ins, outs):
    # print(sorted(ins[0][1]))
    
    for (index, line) in enumerate(ins):
        for (idx, elem) in enumerate(line):
            tempVal = "".join(sorted(elem))
            # print(tempVal)
            line[idx] = tempVal
            # print(line[idx])
    # print(ins)
            
    for (index, line) in enumerate(outs):
        for (idx, elem) in enumerate(line):
            tempVal = "".join(sorted(elem))
            line[idx] = tempVal
    
    listOfNum = []
    
    for (index, line) in enumerate(ins):
        decodedNumber = np.zeros(4)
        for (idx, elem) in enumerate(line):
            # print(np.array(outs[index]) == elem)
            decodedNumber = decodedNumber + np.array(elem == np.array(outs[index])).astype(int) * (9 - idx)
            # print(decodedNumber)
            # if index == 0:
                # print((9 - idx))
                # print(decodedNumber)
        listOfNum.append(decodedNumber)
            
    return listOfNum

def string_overlap(string1, string2):
    # string1Tup = (len(string1), string1)
    # string2Tup = (len(string2), string2)
    longerString = max([string1, string2], key = lambda string: len(string))
    shorterString = min([string1, string2], key = lambda string: len(string))
    overlap = 0
    for letter in shorterString:
        try:
            letter in longerString          
            overlap = overlap + 1 if letter in longerString else overlap
        except ValueError:
            overlap = overlap + 0
    return overlap
    

def is_069(uniInputs, nonUniInputs):
    
    pass

def run():
    fContent = load_files()
    processed_data = data_processing2(data = fContent)
    inputs = processed_data[:, 0]
    outputs = processed_data[:, 1]
    totalUniques = count_uniques(data = outputs)[0]
    uniques = count_uniques(data = outputs)[1]
    uniqueInputs = count_uniques(data = inputs)[1]  #unique inputs
    # print(np.array([row for row in outputs]))
    nonUni = (np.array(uniques == 0).astype(int))  #a mask to pick out non-unique values from outputs
    nonUniInputs = (np.array(uniqueInputs == 0).astype(int))  #a mask to pick out non-unique values from inputs
    # nonUni = np.where(np.array(uniques == 0))
    # print(nonUni)
    inputs2 = np.array([[len(el) for el in row] for row in inputs]).reshape(uniqueInputs.shape) * nonUniInputs
    outputs2 = np.array([[len(el) for el in row] for row in outputs]).reshape(uniques.shape) * nonUni
    print(inputs2)
    # print(len(outputs[0][1]))
    decoded = np.array(decoding(ins = inputs, outs = outputs))
    decoded2 = []
    for index, number in enumerate(decoded):
        tempVal = ""
        for digit in number:
            tempVal = tempVal + str(int(digit))
        decoded2.append(tempVal)
    # print(int("0226"))       
    # print(decoded2)
    # print(len(decoded2))
    # print(len(outputs))
    # sumN = 0
    # for el in decoded2:
        # sumN = sumN + float(el)
    # print(sumN)
    result = sum(np.array(decoded2).astype(float))
    return totalUniques, result
# print(load_files()[0])
# print(data_preprocessing(load_files())[1])
print(run())
print(string_overlap("adfg", "af"))


'''
Znaleźć cyfry o określonej liczbie kresek i wyznaczyć, która to która 
w oparciu o przekrycie z unikatowymi (1, 4, 7, 8). Przykładowo:
2, 5, 3 mają tyle samo kresek
3 z 8 ma 6, z 7 ma 3, z 4 ma 3, z 1 ma 2
5 z 8 ma 6, z 7 ma 2, z 4 ma 3, z 1 ma 1
2 z 8 ma 6, z 7 ma 2, z 4 ma 2, z 1 ma 1

5 w/ 4 has 3
2 w/ 4 has 2
6 w/ 7 has 2, w/ 3 has 5
9 w/ 7 has 3, w/ 3 has 5
0 w/ 7 has 3, w/ 3 has 4
'''