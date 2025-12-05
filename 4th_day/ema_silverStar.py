import numpy as np

import pandas as pd

 

with open('inputData.txt') as f:

    lines = [line.rstrip('\n') for line in f]

   

def sum_intorno(map2d,i,j):

    return int(map2d[i-1][j-1] + map2d[i-1][j] + map2d[i-1][j+1] + map2d[i+1][j-1] + map2d[i+1][j] + map2d[i+1][j+1] + map2d[i][j+1] + map2d[i][j-1])

 

def sum_intorno_top(map2d,i,j):

    return int(map2d[i+1][j-1] + map2d[i+1][j] + map2d[i+1][j+1] + map2d[i][j+1] + map2d[i][j-1])

 

def sum_intorno_bottom(map2d,i,j):

    return int(map2d[i-1][j-1] + map2d[i-1][j] + map2d[i-1][j+1] + map2d[i][j+1] + map2d[i][j-1])

 

def sum_intorno_r(map2d,i,j):

    return int(map2d[i-1][j-1] + map2d[i-1][j] + map2d[i+1][j-1] + map2d[i+1][j] + map2d[i][j-1])

 

def sum_intorno_l (map2d,i,j):

    return int(map2d[i-1][j] + map2d[i-1][j+1] + map2d[i+1][j] + map2d[i+1][j+1] + map2d[i][j+1])

 

    

length = len(lines)

map_tmp = np.zeros(shape=(length, length),dtype='int32')   

map_new = np.zeros(shape=(length, length),dtype='int32')   

 

for i in range(length):

    for j in range(length):

        if lines[i][j] == '@':

            map_tmp[i][j] = 1

           

print(map_tmp)

 

# dentro

for i in range(1,length-1):

    for j in range(1,length-1):

        if map_tmp[i][j] == 1:

            map_new[i][j] = sum_intorno(map_tmp,i,j)

           

# bordi

for j in range(1,length-1):

    if map_tmp[0][j] == 1:

        map_new[0][j] = sum_intorno_top(map_tmp,0,j)   

    if map_tmp[length-1][j] == 1:

        map_new[length-1][j] = sum_intorno_bottom(map_tmp,length-1,j)          

        

for i in range(1,length-1):

    if map_tmp[i][0] == 1:

        map_new[i][0] = sum_intorno_l(map_tmp,i,0)   

    if map_tmp[i][length-1] == 1:

        map_new[i][length-1] = sum_intorno_r(map_tmp,i,length-1)       

        

# spigoli

if map_tmp[0][0] == 1:

    map_new[0][0] = 1

if map_tmp[0][length-1] == 1:

    map_new[0][length-1] = 1

if map_tmp[length-1][0] == 1:

    map_new[length-1][0] = 1

if map_tmp[length-1][length-1] == 1:

    map_new[length-1][length-1] = 1

 

print(map_new)

counter = 0

for i in range(0,length):

    for j in range(0,length):

        if map_new[i][j] < 4 and map_new[i][j] > 0:

            counter = counter + 1

print(counter)