# Problem 19: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

#!/bin/python3

import math
import os
import random
import re
import sys


from collections import Counter


if __name__ == '__main__':
    X = int(input())
    shoes = Counter(map(int, input().split()))

    N = int(input())
    total = 0

    for _ in range(N):
        size, price = map(int, input().split())

        if shoes[size] > 0:
            total += price
            shoes[size] -= 1

    print(total)
