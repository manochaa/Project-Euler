#-------------------------------------------------------------------------------
# Name:        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#               Find the product abc.
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

def findPyth():
    for c in range(1,1000):
        for b in range(1,1000):
            for a in range(1,1000):
                if (a*a)+(b*b) == (c*c):
                    if a+b+c == 1000:
                        return a*b*c
print findPyth()