# Problem 8: What's Your Name?
# HackerRank Link: https://www.hackerrank.com/challenges/whats-your-name/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
