
import numpy as np
import scipy 

from scipy import optimize


params = (2, 3, 7, 8, 9, 10, 44, -1, 2, 26, 1, -2, 0.5)
def f1(z, *params):
        x, y = z
        a, b, c, d, e, f, g, h, i, j, k, l, scale = params
        return (a * x**2 + b * x * y + c * y**2 + d*x + e*y + f)

def f2(z, *params):
        x, y = z
        a, b, c, d, e, f, g, h, i, j, k, l, scale = params
        return (-g*np.exp(-((x-h)**2 + (y-i)**2) / scale))
def f3(z, *params):
        x, y = z
        a, b, c, d, e, f, g, h, i, j, k, l, scale = params
        return (-j*np.exp(-((x-k)**2 + (y-l)**2) / scale))

def f(z, *params):
        x, y = z
        a, b, c, d, e, f, g, h, i, j, k, l, scale = params
        return f1(z, *params) + f2(z, *params) + f3(z, *params)
x0 = np.array([2., 2.])



np.random.seed(555)   # Seeded to allow replication.

res = optimize.anneal(f, x0, args=params, schedule='boltzmann',
                          full_output=True, maxiter=500, lower=-10,
                          upper=10, dwell=250, disp=True)
        
