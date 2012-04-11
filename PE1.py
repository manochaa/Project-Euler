#-------------------------------------------------------------------------------
# Name:        Sum of multiples of 3 & 5 until 1000.
# Purpose:    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#           Find the sum of all the multiples of 3 or 5 below 1000.
#
# Author:      Ayush Manocha
#
# Created:     30/03/2012
# Copyright:   (c) cain297 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

sumT = 0

for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        sumT += i
print sumT