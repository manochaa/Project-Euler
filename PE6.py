#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cain297
#
# Created:     07/04/2012
# Copyright:   (c) cain297 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()


def sumOfSquares():
    count = 1
    sumOfS = 0
    while count < 101:
        sumOfS += count**2
        count += 1
    return sumOfS

def squaresOfSum():
    count = 1
    squaresS = 0
    while count <101:
        squaresS += count
        count += 1
    return squaresS**2

def difference():
    print abs(sumOfSquares()- squaresOfSum())

difference()