#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxSum = -63
    
    for i in range(4):
        for j in range(4):
            
            #sum top 3 elements
            top = sum (arr[i][j:j+3])
            
            #sum the mid elemnts
            mid = arr[i+1][j+1]
            
            #sum the 3 bottom elemnts
            bottom = sum (arr[i+2][j:j+3])
            
            time= top + mid+ bottom
            
            if time > maxSum:
                maxSum = time
                
    return maxSum
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
