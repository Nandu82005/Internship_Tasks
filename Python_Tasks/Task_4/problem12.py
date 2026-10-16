# Problem 12: Introduction to Sets
# HackerRank Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def average(array):
    distinct = set(array)
    result = sum(distinct) / len(distinct)
    return round(result, 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
