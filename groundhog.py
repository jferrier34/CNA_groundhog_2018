#!/usr/bin/python3

from math import *
import sys

def switch(evol1, evol2, nb_switch):
    if (evol2 != 0):
        if (evol1 >= 0 and evol2 < 0):
            nb_switch += 1
            print("\t a switch occurs", end = '')
        if (evol1 < 0 and evol2 >= 0):
            nb_switch += 1
            print("\t a switch occurs", end = '')
    return (nb_switch)

def average(tab):
    i = 1
    nb = 0
    tmp = 0
    for_return = 0
    while (i < len(tab)):
        tmp = tab[i] - tab[i - 1]
        if (tmp > 0):
            nb = nb + tmp
        i = i + 1
    for_return = nb / (len(tab) - 1)
    return (for_return)
   

def evolution(listt):
    tmp = 0
    max = 100
    tmp = (max * (listt[len(listt) - 1] - listt[0]) / listt[0])
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

def disp(value, opt, retain, tmp2, nb_switch):
    if (opt == 0):
        print("g=nan       r=nan%"+"       s=nan", end = '')
    elif (opt == 1):
        print("g=nan       r=nan%"+"       s=%.2f" % (value[2]), end = '')
    else:
        print("g=%.2f       r=%.0f       s=%.2f" % (value[0], value[1], value[2]), end = '')
    if (tmp2 > int(sys.argv[1])):
        nb_switch = switch(value[1], retain, nb_switch)
    print("")
    return (nb_switch)

def check_general_error(tab, period, user, weird, copy_weird, nb_switch):

    if (user == "STOP" and (len(tab) < period)):
        print("you have leave the programm")
        exit (84)
    if (user == "STOP"):
        exit(0)
    try:
        float(user)
    except:
        print("only number")
        exit(84)

def call_all(user, weird, copy_weird, tmp, period, tmp2, retain, i, tab, nb_switch):
    if ((len(tab) == period)):
        tmp[2] = deviation(tab, 0)
        i = 1
    if (len(tab) > period):
        retain = tmp[1]
        tmp[1] = evolution(tab)
        tmp[0] = average(tab)
        tmp[2] = deviation(tab, 1)
        i = 2
    nb_switch = disp(tmp, i, retain, tmp2, nb_switch)
    #print(tmp2)


def princip():
    tab = []
    i = 0
    tmp = [-1, -1, -1]
    tmp2 = 0
    nb_switch = 0
    period = int(sys.argv[1])
    retain = 0
    copy_weird = []
    weird = []
    while (1):
        if (len(tab) > period):
            tab.pop(0)
        try:
            user = input()
        except:
            exit(84)
        check_general_error(tab, period, user, weird, copy_weird, nb_switch)
        tab.append(float(user))
        call_all(user, weird, copy_weird, tmp, period, tmp2, retain, i, tab, nb_switch)
        tmp2 = tmp2 + 1

def error_check():
    try:
        period = float(sys.argv[1])
    except:
        help()
        print("Wrong arguments")
        exit(84)
    if (period <= 0):
        print("please enter a non negative numbers")
        exit(84)

def help():
    print("SYNOPSIS")
    print("\t./groundhog period")
    print("DESCRIPTION")
    print("\tperiod\t\tthe number of days defining a period")
    exit(0)

def main():
    if (len(sys.argv) == 1):
        print("please enter an argument")
        exit (84)
    if (len(sys.argv) < 2 and len(sys.argv) > 2):
        exit (84)
    if (sys.argv[1].isalpha()):
        print ("please retry")
        exit (84)
    if (sys.argv[1] == "-h"):
        help()
    error_check()
    princip()

if __name__ == "__main__":
    main()