##
## EPITECH PROJECT, 2019
## Weird.py
## File description:
## Weird
##
from math import *
import sys

def getWeird(list, weirdValue, weirdGap)
{
    int i = -1;
    int y;
    float tmp1;
    float tmp2;
    float val1;
    float val2;
    gap = list[-1] - list[-2];
    if (weirdValue.length < 5 && weirdValue.length > 1) {
        list.append(list.last);
    }
    else {
        while (weirdGap[++i]) {
            if (weirdGap[i] < gap) {
                tmp1 = weirdGap[i];
                val1 = weirdValue[i];
                weirdGap[i] = gap;
                weirdValue[i] = list[-1];
                y = i;
                while (y != 4) {
                    if (tmp1 != weirdGap[y] && y < 4) {
                        tmp2 = weirdGap[y];
                        val2 = weirdValue[y];
                        weirdGap[y] = tmp1;
                        weirdValue[y] = val1;
                        tmp1 = tmp2;
                        val1 = val2;
                    }
                    if (y = 4 && tmp1 != weirdGap[y]) {
                        weirdGap[y] = tmp1;
                        weirdValue[y] = val1;
                    }
                y++;
                }
            }
        }
    }
}

main()
{
    list = [1 , 2 , 3];
    weirdValue = [list[1]];
    weirdGap = [0, 0, 0, 0, 0];
    getWeird(list);
}