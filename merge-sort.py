# Merge sort in python 
import math
# 1. create merge and mergeSort function
def merge(arr):
    # check if left and right are less than 1 
    if len(arr) < 2:
        return arr
    # recursively split the arr into left and right 
    # setting middle of array 
    middle = math.floor((len(arr)/2))
    leftArr = arr[0:middle]
    rightArr = arr[middle:]
    return mergeSort(merge(leftArr), merge(rightArr))

def mergeSort(leftArr, rightArr):
    # check if both array are not empty
    # while leftArr and rightArr:
    # sort the two input lists/ arrays by adding smaller to new list 
        pass
    # return the sorted and merged array

print(merge([1, 2, 3, 4]))