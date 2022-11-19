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
    # print("corner: ", np.max(boardCorner))
    boardCorner = np.max(boardCorner)
    board = np.zeros((boardCorner + 1, boardCorner + 1))
    # print(board)
    boardShape = board.shape
    return board, boardShape

def subboard(board = def_board()[0], row = load_files()[0].astype(int), diagonal = False):
    size = 0
    subboard = np.array([0])
    size1 = 1
    size2 = 1
    # print(row)
    if row[0] == row[2]:
        # print("a")
        size1 = row[0]
        size2 = np.max([row[3], row[1]])
        # print(np.absolute(row[3] - row[1]))
        subboard = np.zeros((size1 + 1, size2 + 1))
        # print(row[0])
        subboard[row[0], np.min([row[3], row[1]]) : size2 + 1] =+ 1
        # print(row[0], np.min([row[3], row[1]]))
        # print(subboard[row[0], np.min([row[3], row[1]]) : size2])
    elif row[1] == row[3]:
        # print("b")
        size2 = row[1]
        size1 = np.max([row[0], row[2]])
        subboard = np.zeros((size1 + 1, size2 + 1))
        # print(subboard.shape)
        subboard[np.min([row[0], row[2]]) : size1 + 1, row[1]] =+ 1
        # print(subboard.shape)
    # elif row[1] < row[3]:   #dwa ostatnie- elif i else- wymagają przestawienia def subboard4
        # print("c")
        # if diagonal:
            # size = row[3] - row[1]
            # size1 = row[3]
            # size2 = row[3]
            # subboard = np.diag(np.ones(row[3] + 1))
            # subboard[:row[1], :row[1]] = 0
        # print("test: ", size, np.sum(subboard))
    else:
        pass
        # row[1] > row[3]
        # print("d")
        # print(np.diag(np.ones(row[1] - row[3])))
    if diagonal:
        size = np.absolute(row[3] - row[1]) + 1
        # print("diagonal size: ", size)
            # size = row[1] - row[3]
            # size1 = row[1]
            # size2 = row[1]
            # subboard = np.diag(np.ones(row[1] + 1))
            # subboard[:row[3], :row[3]] = 0
            # subboard
    # y = [row[0], row[2]]
    # x = [row[1], row[3]]
    # print("subboard shape: ", board.shape)
    # print(np.where(board == 1))
    # print("size: ", board[0 : size1 + 1, 0 : size2 + 1].shape)
    if row[0] == row[2] or row[1] == row[3]:
        board[0 : size1 + 1, 0 : size2 + 1] =+ subboard
    if diagonal and (row[0] != row[2] and row[1] != row[3]):
        if row[1] - row[3] == row[0] - row[2]:
            # print("size: ", bool(row[1] > row[3]), board[row[0] : row[2] + 1, row[1] : row[3] + 1].shape, row[0], row[2], row[1], row[3])
            board[min([row[0], row[2]]) : max([row[0], row[2]])  + 1, min([row[3], row[1]]) : max([row[3], row[1]]) + 1] = np.diag(np.ones(size))
            
        if row[1] - row[3] == row[2] - row[0]:
            board[min([row[0], row[2]]) : max([row[0], row[2]])  + 1, min([row[3], row[1]]) : max([row[3], row[1]]) + 1] = np.flipud(np.diag(np.ones(size)))
    # print(np.where(board == 1))
    return board, subboard

def locations(fContent = load_files()[0], board = def_board()[0], diagonal = False):
    # for row in fContent:
        # print(row.astype(int))
    # locations = np.apply_along_axis(lambda row: board[range(row.astype(int)[0], row.astype(int)[2]), range(row.astype(int)[1], row.astype(int)[3])] + 1, 1, fContent)
    diag = diagonal
    locations = np.apply_along_axis(lambda row: row.astype(int), 1, fContent)
    # print("board shape: ", board.shape)
    # board[locations[0, 0] : locations[0, 2], locations[0, 2] : locations[0, 3]] = 1
    # print(board[0, 0].astype(int))
    locations_board = np.sum([board + subboard(def_board()[0], location, diag)[0] for location in locations], axis = 0)
    solution = np.sum((locations_board >= 2).astype(int))
    # print(locations_board)
    return locations_board, solution
    
print('printing board')
print(locations(diagonal = True)[1])
print('board printed')

# print(np.diag(np.ones(3)))
# print(np.zeros((3, 3)))
# a = np.array([i for i in range(9)]).reshape((3, -1))
# print(a)
# print(a[1:3, 0])
# print(np.sum((a > 3).astype(int)))
# print(a[0:1, 0:3])
# l = [0, 3]
# print(a[np.min(l):np.max(l), np.min(l):np.max(l)])
# size = 3
# print(np.fliplr(np.diag(np.ones(size))))