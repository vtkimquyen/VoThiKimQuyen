# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:57:44 2024

@author: Kim Quyên


chuoi = "Đại học quốc gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, TP.HCM"

s1 = chuoi.split(', ')
for i in s1:
    print(i)
    
    
    s = ("Đại học quốc gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, TP.HCM")

    s1 = s.replace('P.','').replace('Q.','').replace('TP.','').split(', ')
    for i in s1:
        print(i)
        
        
s = "i'm a cat"

print(s.title())
print(s.upper())
print(s.capitalize())
print(s.strip())

import random
print(random.choice(range(100)))
"""

