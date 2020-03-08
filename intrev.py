# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:49:02 2020

@author: user
"""

num=int(input('Enter the number:'))
print(num)
rev=0
while(num>0):
    rem=num% 10
    rev=(rev*10)+rem
    num=num//10
print('reverse number is:',rev)
    
  