#-------------------------------------------------------------------------------
# Name:        What is the 10 001st prime number?
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
    while i <= int(x**.5):
        if x%i == 0:
            return False
        i += 1
    return True

def count():
    cnt = 2
    primes = []
    found = False
    while not found:
        if len(primes)==10001:
            found = True
            print primes[-1]
        else:
            if is_prime(cnt) == True:
                primes.append(cnt)
                cnt += 1
            else:
                cnt += 1

count()