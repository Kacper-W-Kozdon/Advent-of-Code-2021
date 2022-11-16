# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 12:39:08 2022

@author: xBubblex
"""

import numpy as np

def load_files():
    fContent = []
    with open("D:\Dokumenty\Python\Advent of Code 2021\input4.txt") as f:
            randomNumbers = f.readline().strip().split(",")  #loading the first line of the file into a separate list
            for (lineIndex, line) in enumerate(f):  #loading the file into an np.array
                if bool(line.strip("\n").split()):
                    fContent.append(line.strip("\n").split())  #splitting each entry into digits
    fContent = (np.array(fContent))  #an array of bingo tables (merged together); values are strings
    return(randomNumbers, fContent, fContent.shape)

def create_masks(value = -1, fContent = load_files()[1], oldMask1 = np.zeros(load_files()[2]), oldMask2 = np.zeros(load_files()[2])):
    value = str(value)
    newMask1 = np.array(fContent == value).astype(int) + oldMask1
    newMask2 = np.array([newMask1.flatten()[index * newMask1.shape[1]**2 : (index + 1) * newMask1.shape[1]**2].reshape((newMask1.shape[1], newMask1.shape[1])).transpose() for index in range(int(newMask1.shape[0]/5))]).reshape(newMask1.shape) + oldMask2
    return (newMask1, newMask2)

def winning_condition(mask = create_masks()):
    (mask1, mask2) = mask
    winTable = -1
    winMask = [-1]
    winCond = [1, 1, 1, 1, 1]
    if winCond in mask1.tolist():
        winTable = mask1.tolist().index(winCond) // 5
        winMask = mask1[winTable * 5 : (winTable + 1) * 5]
        return (winTable, winMask)
    elif winCond in mask2.tolist():
        winTable = mask2.tolist().index(winCond) // 5
        winMask = mask1[winTable * 5 : (winTable + 1) * 5]
        return (winTable, winMask)
    else:
        winTable
    return (winTable, winMask)

def find_win_table(winTable = 0, fContent = load_files()[1]):
    bingo = fContent[(winTable) * 5 : (winTable + 1) * 5]
    print("bingo")
    return bingo

def play_bingo():
    (randomNumbers, fContent, _) = load_files()
    newMasks = create_masks()
    winTable = -1
    winValue = -1
    for value in randomNumbers:
        newMasks = create_masks(value, fContent, newMasks[0], newMasks[1])
        if winning_condition(newMasks)[0] != -1:
            print("winning value: " + str(value))
            winTable = winning_condition(newMasks)[0]
            winValue = int(value)
            bingo = find_win_table(winTable, fContent)
            winningMask = winning_condition(newMasks)[1]
            taskCondition = sum(sum((1 - winningMask) * bingo.astype(int))) * winValue
            return (winValue, winTable, bingo, winningMask, taskCondition)
    return(winValue, winTable, bingo, winningMask)

def lose_bingo():
    (randomNumbers, fContent, _) = load_files()
    fContent2 = np.copy(fContent)
    newMasks = create_masks()
    winTable = -1
    winValue = -1
    bingo = [-1]
    winningMask = [-1]
    print(fContent2[0])
    for value in randomNumbers:
        if len(fContent2) != 0:
            newMasks = create_masks(value, fContent2, newMasks[0], newMasks[1])
            while winning_condition(newMasks)[0] != -1:
                print("winning value: " + str(value))
                winTable = winning_condition(newMasks)[0]
                winValue = int(value)
                bingo = find_win_table(winTable, fContent2)
                fContent2 = np.delete(fContent2, [winTable * 5 + index for index in range(5)], 0)
                newMasks0 = np.delete(newMasks[0], [winTable * 5 + index for index in range(5)], 0)
                newMasks1 = np.delete(newMasks[1], [winTable * 5 + index for index in range(5)], 0)
                winningMask = winning_condition(newMasks)[1]
                newMasks = (newMasks0, newMasks1)
                taskCondition = sum(sum((1 - winningMask) * bingo.astype(int))) * winValue
    return(winValue, winTable, bingo, winningMask, taskCondition)

print(play_bingo())
print(lose_bingo())
