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

def findP(a,b,c):
    if a**2+b**2 == c**2:
        if a+b+c == 1000:
            return a*b*c
        else:
            return findP(a+1,b+1,c+1)

findP(0,1,2)