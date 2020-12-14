# importar la librería numpy
import numpy as np
# importar la librería sympy (Que se encarga del formato
# algebráico de mis funciones)
import sympy as sym
# importar matplotlib.pyplot
import matplotlib.pyplot as plt

#%% imprimir en formato latex
sym.init_printing(use_latex='mathjax')
#Esto es para background color
fig = plt.figure()
fig.patch.set_facecolor('xkcd:dark cream')
#Este es para color dentro de la grafica
ax = plt.gca()
ax.patch.set_facecolor('xkcd:light rose')
#%% Sabemos de antemano que la función f(x) = x^2  tiene un mínimo global en x = 0, 
# pues f(x) = x^2>= 0 y f(x) = x^2 = 0, si y solo si x = 0 (por la gráfica que genera)

sym.var('x', real = True)   # Ahora se declara la variable como real

#%% Declarar ahora la función f=x^2 y mostrar
f = x**2
f
#%% Derivar f respecto a x y mostrar
df = sym.diff(f, x)
df
#%% Resolver f'(x)=0 y mostrar soluciones
xc = sym.solve(df, x)
xc

#%% Convertir f en una función que se pueda evaluar numéricamente (función lambdify de la librería sympy)
f_num = sym.lambdify([x], f, 'numpy')
x_vec = np.linspace(-5, 5, 100)

#%% Graficar
plt.plot(x_vec, f_num(x_vec), c='xkcd:baby poop green') #Los colores con nombres más chistosos 
plt.xlabel('$x$')
plt.ylabel('$x^2$')
plt.title('Función $f(x)=x^2$')
#Esto es para background color

plt.show()

