# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 05:41:19 2020

@author: user
"""

s=input('Enter the string:')
print(s)
count=0
for ch in s:
    if(ch=='a'or ch=='e' or ch=='i' or ch=='o' or ch=='u'or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
        count=count+1
print('Number of vowel is:',count)