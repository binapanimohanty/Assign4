# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:38:34 2020

@author: user
"""

l1=input('Enter the list:')
print(l1)
length=len(l1)
print(length)
for i in range(-1,(-length-1),-1):
    print(l1[i],end='')