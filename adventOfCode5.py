# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:20:26 2022

@author: xBubblex
"""

import numpy as np
import re

def load_files():
    fContent = []
    with open("input5.txt") as f:
            for (lineIndex, line) in enumerate(f):  #loading the file into an np.array
                if bool(line.strip("\n").split()):
                    fContent.append(re.split(",| -> ", line.strip("\n")))  #splitting each entry into coordinates
    fContent = (np.array(fContent))  #an array of coordinates: x1, y1, x2, y2; values are strings
    return(fContent, fContent.shape)


def corner(fContent = load_files()[0]):
    boardCorner = fContent.reshape((-1, 2)).astype(int).max(axis = 0, keepdims = 1)[0]
    return boardCorner

def def_board(boardCorner = corner(fContent = load_files()[0])):
    board = np.zeros((boardCorner[0], boardCorner[1]))
    boardShape = board.shape
    return board, boardShape

print(def_board()[1])

def locations(fContent = load_files()[0], board = def_board(fContent = load_files()[0])):
    
    pass