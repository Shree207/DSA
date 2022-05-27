from os import *
from sys import *
from collections import *
from math import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
    arr=[None]*(m+n)
    for i in range(m):
        arr[i]=arr1[i]
    for i in range(n):
        arr[m+i]=arr2[i]
    arr1=arr
    return sorted(arr1)
    pass
