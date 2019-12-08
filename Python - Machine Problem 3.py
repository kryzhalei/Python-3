# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:17:14 2019

@author: Kryzha Lei Aguilar
"""

import numpy as np

def coefficients(q):
    
    for n in range(len(q)):
        
        w = np.polyfit(q[:,0],q[:,1],n)
        e = np.polyval(w, q[:,0])
        r = np.linalg.norm(q[:,1] - e)
        x = [n,r]

        if n==0:
            y = x

        elif y[1] >= x[1]:
            z = x[0]
            
    r = np.polyfit(q[:,0],q[:,1],z)

    print('Coefficients: ',r)    

print ("nx2 Matrix is required")
m = int(input("Enter number of rows:")) 
n = 2    

print("Enter the elements:")
elements = list(map(int, input().split()))  
M3 = np.array(elements).reshape(m,n)

coefficients (M3)