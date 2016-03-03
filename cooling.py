# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:55:21 2016

File: Cooling.py

Copyright (c) 2016 Eddie Wadors

License: MIT

running a while loop to determine the cooling rate of a cup of tea every minute for 20 minutes based on a given forumla.
"""
T = 0 #minutes
T_tea = 100
T_air = 20
while T<20:
    print (T,T_tea)
    T_tea -= (.055)*(T_tea-T_air)
    T += 1
print (T,T_tea)
