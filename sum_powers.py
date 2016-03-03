# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:55:21 2016
File: sum_powers.py

Copyright (c) 2016 Eddie Wadors

License: MIT

Running an equation asking for numbers and running the sum of powers of these numbers using a while loop.
"""
b_ask = raw_input ("Please enter a floating point number:")
b = float (b_ask)
n_ask = raw_input ("Please enter a natural number:")
n = int (n_ask)

i = 0
sum = 0
while i<=n:
    sum += b**i*1.0
    i += 1   
print sum

eq_2 = (b**(n+1)-1)/(b-1) #fixed second equation
print eq_2
