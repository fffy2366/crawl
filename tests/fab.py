# -*- coding: utf-8 -*-
# def fab(max):
#    n, a, b =0, 0, 1
#    whi len < max:
#        printb
#        a, b =b, a +b
#        n =n +1

#斐波那契数列
# https://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97
fibs = [0, 1]
numZS = input('How many Fibonacci numbers do you want? ')
for i in range(numZS-2):
    fibs.append(fibs[-2] + fibs[-1])
print fibs