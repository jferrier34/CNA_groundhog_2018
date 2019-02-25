##
## EPITECH PROJECT, 2019
## Weird.py
## File description:
## Weird
##
#!/usr/bin/python3
from math import *
import sys

def getWeird(list):
    i = 0
    weirdValues = []
    while (i < len(list) + 1):
        if (abs(list[i] - list[i + 1]) >= 12):
            weirdValues.append(list[i])
    i = 1
    print("%2f%% weirdest values are [%2f%%" % (len(weirdValues)))
    print("%2f%%" % weirdValues[0])
    while (i < len(weirdValues)):
        print(", ")
        print("%2f%%" % weirdValues[i])
    print("]\n")