#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:28:50 2019



@author: emiliano
"""

import scipy.optimize as opt
import numpy as np
import sympy as sym
sym.init_printing(use_latex='mathjax')
#%% Definimos nuestra función a maximizar
f = np.array([0.0865, 0.0950, 0.10, 0.0875, 0.0925, 0.09])
f
#%% Buscamos nuestras funciones sujetas a la función a maximizar
A = np.array([[1, 1, 1, 1, 1, 1], [-1, -1, 0, -1, 0, -1], [0, 1, 1, 0, 1, 0]])
B = np.array([750000, -375000, 262500])

A,B
#%%Ponemos los límites
x1 = (0,187500)
x2 = (0,187500)
x3 = (0,187500)
x4 = (0,187500)
x5 = (0,187500)
x6 = (0,187500)
#%%Y maximizamos
inversion = opt.linprog(f, A, B, bounds = (x1, x2, x3, x4, x5, x6), options={'disp':True})
inversion
inversion.x