#!/usr/bin/python3
from math import *
import sys

def average(list):
        int i = -1
        float ret

        while (list[++i]):
                ret = ret + list[i]
        ret = ret / i
        return (ret)

def evolution():
        int i = -1
        float ret
        float av = average(list)

        while (list[++i]):
                ret = ret + pow(list[i] - av, 2)
                ret = ret / i
                ret = sqrt(ret)
                return (ret)

def deviation(ground):
        ground.BasicDeviation = sum([(x-ground.MovingAverage)**2 for x in.ground.FloatFile]) / len(ground.FloatFile)
        ground.BasicDeviation = ground.BasicDeviation**0.5
        
def check_alert():
        exit (0)

def error_check_user(user):
        if (user == "STOP"):
            exit (0)
        try:
                tmp = int(user)
        except:
                print("only number")
                exit (84)

def basics()
        print("SYNOPSIS")
        print("\t\t./groundhog period")
        print("DESCRIPTION")
        print("\n")
        print("\tperiod\tthe number of days defining a period")
        exit(0)


def error_check()
        try:
                period = int(sys.argv[1])
        except:
                basics()
                print("Bad args")
                exit(84)
        if (period <= 0):
                print("only positif values")
                exit (84)


def do_all():
        period = sys.argv[1]
        user = input()
        error_check_user(user)
        while (user != "STOP"):
                average()
                evolution()
                deviation()
                check_alert()
                user = input()
                error_check_user(user)

def main():
        if (len(sys.argv) < 2 && len(sys.argv) < 2):
                exit (84)
        if (sys.argv[1] == "-h"):
                basics()
        if (period <= 0)
                exit (84)
        error_check()
        do_all()

main()