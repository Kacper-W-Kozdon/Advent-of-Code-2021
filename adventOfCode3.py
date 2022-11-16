# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 13:42:21 2022

@author: xBubblex
"""

import numpy as np

fContent = []
with open("D:\Dokumenty\Python\Advent of Code 2021\input3.txt") as f:
    for line in f:  #loading the file into a np.array
        fContent.append([digit for digit in str(line).strip()])  #splitting each entry into digits
fContent = (np.array(fContent)).transpose()  #table of digits- for ease of iteration (over rows) the table is transposed
mostCommonDigit = []
leastCommonDigit = []
for digit in fContent:  #finding most/least common digit by counting occurences of each possible value (from set) and picking max/min
    mostCommonDigit.append(max(set(digit), key = digit.tolist().count))
    leastCommonDigit.append(min(set(digit), key = digit.tolist().count))
gammaRate = ""
epsilonRate = ""
for (index, digit) in enumerate(mostCommonDigit):  #putting all digits together and converting them from str to binary to decimal
    gammaRate = gammaRate + digit
    epsilonRate = epsilonRate + leastCommonDigit[index]
gammaRate = int(gammaRate, 2)
epsilonRate = int(epsilonRate, 2)
print(gammaRate * epsilonRate)
fContent2 = np.copy(fContent.transpose())
digitNo = 0
while fContent2.shape[0] > 1:  #removing elements meeting the condition from the fContent2 array until there's only 1 element
    digit = fContent2[:, digitNo]
    condition = min({"0", "1"}, key = digit.tolist().count) if min({"0", "1"}, key = digit.tolist().count) != max({"0", "1"}, key = digit.tolist().count) else "0"
    fContent2 = np.delete(fContent2, [index for (index, _) in enumerate(fContent2) if fContent2[index, digitNo] == condition], 0)
    digitNo = (digitNo + 1) % fContent2.shape[1]
O2 = ""  #recombining digits from a list of strings to a decimal number- same for CO2
for digit in fContent2[0]:
    O2 = O2 + digit
O2 = int(O2, 2)
fContent2 = np.copy(fContent.transpose())
digitNo = 0
while fContent2.shape[0] > 1:
    digit = fContent2[:, digitNo]
    condition = max({"0", "1"}, key = digit.tolist().count) if min({"0", "1"}, key = digit.tolist().count) != max({"0", "1"}, key = digit.tolist().count) else "1"
    fContent2 = np.delete(fContent2, [index for (index, _) in enumerate(fContent2) if fContent2[index, digitNo] == condition], 0)
    digitNo = (digitNo + 1) % fContent2.shape[1]
CO2 = ""
for digit in fContent2[0]:
    CO2 = CO2 + digit
CO2 = int(CO2, 2)
print(O2 * CO2)