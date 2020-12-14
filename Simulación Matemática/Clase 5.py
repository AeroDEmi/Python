#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:21:54 2019
Programa ejemplo de evaluaci'on de criterio de segunda derivada
@author: emiliano
"""
#importar las librerias
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
#%% imprimir en formato latex
sym.init_printing(use_latex='mathjax')
#MathJax.Hub.Config({ TeX: { extensions: ["color.js"] }})
x=0
sym.var('x')

#%% Definimos nuestra funcion
#def f(x):
#    return x**2
#f(x)
f = x**3-3*x
f
#%% Derivamos la función dos veces
df = sym.diff(f,x)
df
#%%
d2f = sym.diff(f, x, 2)
d2f
#%%
x_c = sym.solve(df, x)
x_c
#%%Se evalúan los extremos(de -2.2 y 1.8) y en los puntos críticos:
f.subs(x, -2.2), f.subs(x,1.8)
#%%
a0 = f.subs(x, x_c[0])
a1 = f.subs(x, x_c[1])   
#%% Concluimos que el máximo absoluto de la función en el intervalo es 0
# y se alcanza en x=0
# y que el mínimo absoluto es -9 y se alcanza en x=3
f_num = sym.lambdify([x], f, 'numpy')
x_vec = np.linspace(-2.2, 1.8, 100)
#%% Configuración de la gráfica
plt.figure(figsize=(8,6))
plt.plot(x_vec, f_num(x_vec), 'k--', label = '$y=f(x)$')
plt.plot([x_c[0]], [a0], '*r', label = '$(x_c[0],a0=\max_{-2.2\leq x\leq 1.8} f(x))$')
plt.plot([x_c[1]], [a1], '*b', label = '$(1,-2=\min_{0\leq x\leq 5} f(x))$')
plt.legend(loc='best')
plt.xlabel('x')
#plt.grid(b=None)
plt.grid(which='major', axis='both', linewidth = 1)
plt.show()