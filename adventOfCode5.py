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
    boardCorner = np.max(boardCorner)
    board = np.zeros((boardCorner + 1, boardCorner + 1))
    boardShape = board.shape
    return board, boardShape

def subboard(board = def_board()[0], row = load_files()[0].astype(int), diagonal = False):
    size = 0
    subboard = np.array([0])
    size1 = 1
    size2 = 1
    if row[0] == row[2]:
        size1 = row[0]
        size2 = np.max([row[3], row[1]])
        subboard = np.zeros((size1 + 1, size2 + 1))
        subboard[row[0], np.min([row[3], row[1]]) : size2 + 1] =+ 1
    elif row[1] == row[3]:
        size2 = row[1]
        size1 = np.max([row[0], row[2]])
        subboard = np.zeros((size1 + 1, size2 + 1))
        subboard[np.min([row[0], row[2]]) : size1 + 1, row[1]] =+ 1
    else:
        pass
    if diagonal:
        size = np.absolute(row[3] - row[1]) + 1
    if row[0] == row[2] or row[1] == row[3]:
        board[0 : size1 + 1, 0 : size2 + 1] =+ subboard
    if diagonal and (row[0] != row[2] and row[1] != row[3]):
        if row[1] - row[3] == row[0] - row[2]:
            # print("size: ", bool(row[1] > row[3]), board[row[0] : row[2] + 1, row[1] : row[3] + 1].shape, row[0], row[2], row[1], row[3])
            board[min([row[0], row[2]]) : max([row[0], row[2]])  + 1, min([row[3], row[1]]) : max([row[3], row[1]]) + 1] = np.diag(np.ones(size))
            
        if row[1] - row[3] == row[2] - row[0]:
            board[min([row[0], row[2]]) : max([row[0], row[2]])  + 1, min([row[3], row[1]]) : max([row[3], row[1]]) + 1] = np.flipud(np.diag(np.ones(size)))
    return board, subboard

def locations(fContent = load_files()[0], board = def_board()[0], diagonal = False):
    diag = diagonal
    locations = np.apply_along_axis(lambda row: row.astype(int), 1, fContent)
    locations_board = np.sum([board + subboard(def_board()[0], location, diag)[0] for location in locations], axis = 0)
    # WARNING- THE LINE ABOVE IS VERY NOT OPTIMAL, PROBABLY EVEN LOOP WOULD BE BETTER BUT I INTEND TO SWITCH IT TO A MAP!
    solution = np.sum((locations_board >= 2).astype(int))
    return locations_board, solution
    
print('printing board')
print(locations(diagonal = False)[1], locations(diagonal = True)[1])
print('board printed')
