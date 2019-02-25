#!/usr/bin/python3
from math import *
import sys

def getWeird(list, listt):
    i = 0
    print("ok")
    weirdValues = []
    while (i < len(list) - 1):
        if (abs(list[i] - list[i + 1]) >= 12):
            weirdValues.append(listt[i])
        i += 1
    i = 1
    print("%d weirdest values are " % (len(weirdValues)), end = '')
    print(weirdValues)

def switch(evol1, evol2):
    if (evol2 != 0):
        if (evol1 >= 0 and evol2 < 0):
            print("\t a switch occurs", end = '')
        if (evol1 < 0 and evol2 >= 0):
            print("\t a switch occurs", end = '')
    print("")

def average(listt):
    i = 1
    nb2 = 0
    while (i < len(listt)):
        tmp = listt[i] - listt[i - 1]
        if (tmp > 0):
            nb2 = nb2 + tmp
        i = i + 1
    return (nb2 / (len(listt) - 1))

def evolution(listt):
    tmp = 0
    tmp = (100 * (listt[len(listt) - 1] - listt[0]) / listt[0])
    return (tmp)

def deviation(listt, nb):
    tmp = 0
    nb2 = 0
    tmp2 = nb
    tmp3 = nb
    while (tmp2 < len(listt)):
        tmp = tmp + listt[tmp2]
        tmp2 = tmp2 + 1
    tmp = tmp / (len(listt) - nb)
    while (nb < len(listt)):
        nb2 = nb2 + pow(listt[nb] - tmp, 2)
        nb = nb + 1
    nb2 = nb2 / (len(listt) - tmp3)
    return (float(sqrt(nb2)))
def check_alert():
    exit(0)

def error_check_user(user):
    if (user != "STOP"):
        try:
            float(user)
        except:
            print("only number")
            exit(84)

def disp_final(value, opt, retain):
    if (opt == 0):
        print("g=nan       r=nan%"+"       s=nan", end = '')
    elif (opt == 1):
        print("g=nan       r=nan%"+"       s=%.2f" % (value[2]), end = '')
    else:
        print("g=%.2f       r=%.2f%%       s=%.2f" % (value[0], value[1], value[2]), end = '')
    switch(value[1], retain)

def do_all():
    listt = []
    i = 0
    makeweird = []
    tmp = [-1, -1, -1]
    period = int(sys.argv[1])
    retain = 0
    while (1):
        if (len(listt) > period):
            listt.pop(0)
        user = input()
        if (user == "STOP"):
            print (listt)
            getWeird(makeweird, listt)
            exit(0)
        error_check_user(user)
        listt.append(float(user))
        if ((len(listt) == period)):
            tmp[2] = deviation(listt, 0)
            i = 1
        if (len(listt) > period):
            retain = tmp[1]
            tmp[1] = evolution(listt)
            tmp[0] = average(listt)
            tmp[2] = deviation(listt, 1)
            i = 2
            makeweird.append(tmp[1])
        disp_final(tmp, i, retain)

def error_check():
    try:
        period = float(sys.argv[1])
    except:
        help()
        print("Wrong arguments")
        exit(84)
    if (period <= 0):
        print("only positif number")
        exit(84)

def help():
    print("SYNOPSIS")
    print("\t\t./groundhog period")
    print("DESCRIPTION")
    print("\tperiod\tthe number of days defining a period")
    exit(0)

def main():
    if (len(sys.argv) < 2 and len(sys.argv) > 2):
        exit(84)
    if (sys.argv[1] == "-h"):
        help()
    error_check()
    do_all()

if __name__ == "__main__":
    main()