#-------------------------------------------------------------------------------
# Name:        Find the sum of all the primes below two million
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

def is_prime(x):
    i = 2
    while i < x**.5:
        if x%i == 0:
            return False
        i += 1
    return True

primeSet = [1]
#globalCount = 0

##def count(x):
##    return x+1

def calculate():
    count = 1
    while primeSet[-1] <2000000:
        for i in range(len(primeSet)):
            if count%primeSet[i] != 0:
                count += 1
            #print "inside while loop"
            elif count%2 == 0:
                count += 1
            elif is_prime(count) == True:
                print "inside if statement"
                primeSet.append(count)
                count += 1
            else:
                print "inside else statement and count is", count
                count += 1
    primeSet.sort()
    print primeSet[-1]


calculate()