#!/usr/bin/python3

from math import *
import sys

def switch(evol1, evol2, nb_switch): #this function permit to display "a switch occurs when you have a variances between 2 values of r"
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
        print("g=%.2f       r=%.0f%%       s=%.2f" % (value[0], value[1], value[2]), end = '')
    if (tmp2 > int(sys.argv[1])):
        nb_switch = switch(value[1], retain, nb_switch)
    print("")
    return (nb_switch)

def check_general_error(tab, period, user, weird, copy_weird, nb_switch):

    if (user == "STOP" and (len(tab) < period)): #if user write STOP and the numbers of values into the tab is inferior of the number of day in the period 
        print("you have leave the programm")
        exit (84)
    if (user == "STOP"): #if user write STOP we leave the program
        exit(0)
    try:
        float(user)
    except:
        print("only number") #if user write a value who is not a digit
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
        period = float(sys.argv[1]) #period check correspond a value to represent a interval of days experimentation
    except:
        help()
        print("Wrong arguments")
        exit(84)
    if (period <= 0): #the value of the period correspond obviously a positive number
        print("please enter a non negative numbers")
        exit(84)

def help(): #display of -h to explain the goal of project
    print("SYNOPSIS")
    print("\t./groundhog period")
    print("DESCRIPTION")
    print("\tperiod\t\tthe number of days defining a period")
    exit(0)

#this main manage errors of many possibilities arguments
def main():
    if (len(sys.argv) == 1): #if the the user enter any argument (only exec)
        print("please enter an argument")
        exit (84)
    if (len(sys.argv) < 2 and len(sys.argv) > 2): #if no argument or the user enter more of 2 arguments (ex ./groundhog 2 4)
        exit (84)
    if (sys.argv[1].isalpha()): #if the user enter a non digit argument
        print ("please retry")
        exit (84)
    if (sys.argv[1] == "-h"): #if user enter "-h" after the exec (ex ./groundhog -h)
        help()
    error_check() #call error_check function
    princip() #call de princip function

if __name__ == "__main__":
    main()