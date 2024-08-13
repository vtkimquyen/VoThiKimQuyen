# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:55:16 2024

@author: Võ Thị Kim Quyên

a= float(input("Nhập hệ số a="))
b= float(input("Nhập hệ số b="))
if a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
elif a == 0 and b != 0:
    print("Phương trình vô nghiệm")
else:
    print("Phương trình có nghiệm x=",-b/a)
    
    ---------------------
    import math

a=float(input("Nhập hệ số a:"))
b=float(input("Nhập hệ số b:"))
c=float(input("Nhập hệ số c:"))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = ((-b + (delta**1/2))/(2*a));
    x2 = ((-b - (delta**1/2))/(2*a));
    print("Phương trình có 2 nghiệm phân biệt x=",x1,"x=",x2)
elif delta==0:
    print("Phương trình có 1 nghiệm kép","x=",(-b/2*a))
else:
    print("Phương trình vô nghiệm")
    ------------------------
    
    a=float(input("Nhập hệ số a:"))
b=float(input("Nhập hệ số b:"))
c=float(input("Nhập hệ số c:"))

if (a+b)>c and (b+c)>a and (c+a)>b:
    print("Là 3 cạnh  tam giác")
if c**2==a**2+b**2 or a**2==b**2+c**2 or b**2==a**2+c**2:
    print("Là 3 cạnh tam giác vuông")
elif a==b !=c or a==c !=b or b==c !=a:
    print("Là 3 cạnh tam giác cân")
elif a==b==c:
    print("Là 3 cạnh tam giác đều")
else:
    print("Là 3 cạnh tam giác thường")
    --------------------------
    
    S=float(input("Nhập quãng đường(km):"))
if S<=1:
    print("Số tiền là 20000.")
elif 1<S<4:
    print("Số tiền là",(S*13000))
elif 4<=S<8:
    print("Số tiền là",((S-3)*12000)+39000)
else:
    if ((S-8)*10000 + 39000 + 60000)<100000:
       print("Số tiền là",((S-8)*10000+39000+60000))
    else:
       print("Số tiền là",((S-8)*10000+39000+60000)*0.92)
"""





