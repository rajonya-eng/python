# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:37:43 2020

@author: User
"""

import numpy as np 
import random
a=np.random.rand(50,50)*10
b=a.tolist()

def determinant(A):
    
    n = len(A)
    k = A
 
    for j in range(n): 
        for i in range(j+1,n): 
            if k[j][j] == 0:
                k[j][j] == 1.0e-18
            
            crScaler = k[i][j] / k[j][j] 
            
            for p in range(n): 
                k[i][p] = k[i][p] - crScaler * k[j][p]
     
   
    product = 1.0
    for i in range(n):

        product *= k[i][i] 
 
    return product
v=determinant(b) 
x=np.linalg.det(a)
 
print(v)