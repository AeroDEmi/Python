#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 09:45:53 2019

@author: emiliano
"""
import scipy.optimize as opt
#help(opt.linprog) 
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
sym.init_printing(use_latex='mathjax')

#%%
C = np.array([-1, -1])
A = np.array([[50, 24], [30, 33], [-1, 0], [0,-1]])
B = np.array([2400, 2100, -45, -5])
A,B,C
x1_bound = (45, None)
x2_bound = (5, None)
#%%
res = opt.linprog(C, A_ub=A, b_ub=B, bounds=(x1_bound, x2_bound),options={'disp':True})
res
res.x
#%% Podemos definir las funciones de otra manera
def res1(x1):
    return (2400-50*x1)/24
def res2(x1):
    return (2100-30*x1)/33

x1 = np.linspace(40, 50)
r1 = res1(x1)
r2 = res2(x1)
#%% Graficar
plt.figure(figsize = (8,6))
plt.plot(x1, res1(x1), 'b--', label = 'res1')
plt.plot(x1, res2(x1), 'r--', label = 'res2')
plt.plot([45, 45], [0, 25], 'k', label = 'res3')
plt.plot([40, 50], [5, 5], 'm', label = 'res4')
plt.fill_between(np.array([45.0, 45.6]), res1(np.array([45.0, 45.6])), 5*np.ones(2))
plt.text(44,4,'$(45,5)$',fontsize=10)
plt.text(45.1,6.35,'$(45,6.25)$',fontsize=10)
plt.text(45.6,4,'$(45.6,5)$',fontsize=10)
plt.legend(loc = 'best')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.axis([44, 46, 4, 7])
plt.show()