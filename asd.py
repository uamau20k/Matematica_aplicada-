import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(t):
    return -0.21*t**2+3.2*t 

def g(t): 
    return -0.2*t**2+3*t

def h(t): 
    return -0.15*t**2+2.5*t

x = np.arange(0,15,0.01)
plt.plot(x, f(x), label = 'f(x)')
plt.plot(x, g(x), label = 'f(x)')
plt.plot(x, h(x), label = 'f(x)')
plt.title('Relacion entre altura y tiempo')
plt.ylabel('Altura(metros)')
plt.xlabel('Tiempo transcurrido(segundos)')
plt.legend()
plt.show()