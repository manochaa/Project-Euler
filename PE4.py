#-------------------------------------------------------------------------------
# Name:        Find the largest palindrome made from the product of two 3-digit numbers.w
# Purpose:
#
# Author:      cain297
#
# Created:     06/04/2012
# Copyright:   (c) cain297 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

def isPalindrome(s):
    if len(s) <= 1: return True
    else: return s[0] == s[-1] and isPalindrome(s[1:-1])

pdtPalindrome = []

def palinCheck():
    for i in range(100,1000):
        for j in range(100,1000):
            if isPalindrome(str(i*j)) == True:
                pdtPalindrome.append(i*j)
    pdtPalindrome.sort()
    print pdtPalindrome[-1]

palinCheck()