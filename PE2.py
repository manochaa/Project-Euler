#-------------------------------------------------------------------------------
# Name:        Fibonacci
# Purpose:      By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
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

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else: return fib(n-1) + fib(n-2)

sumT = 0
i = 0

while fib(i) < 4000000:
    if fib(i)%2 == 0:
        sumT += fib(i)
        i += 1
    else:
        i +=1

print 'The sum of even fibonacci numbers below the value of 4 million is', sumT