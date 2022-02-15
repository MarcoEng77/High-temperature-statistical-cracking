
import numpy as np
import scipy 

from scipy import optimize
from scipy.optimize import basinhopping

func = lambda x: np.cos(14.5 * x - 0.3) + (x**x + 0.2) * x
x0=[1.]

minimizer_kwargs = {"method": "BFGS"}
ret = basinhopping(func, x0, minimizer_kwargs=minimizer_kwargs,niter=200)
print("global minimum: x = %.4f, f(x0) = %.4f" % (ret.x, ret.fun))

def func2d(x):
        f = np.cos(14.5 * x[0] - 0.3) + (x[1] + 0.2) * x[1]  + (x[0] +
                                                          0.2) * x[0]
        df = np.zeros(2)
        df[0] = -14.5 * np.sin(14.5 * x[0] - 0.3) + 2. * x[0] + 0.2
        df[1] = 2. * x[1] + 0.2
        return f, df

minimizer_kwargs = {"method":"L-BFGS-B", "jac":True}
x0 = [1.0, 1.0]
ret = basinhopping(func2d, x0, minimizer_kwargs=minimizer_kwargs,
                   niter=200)
print("global minimum: x = [%.4f, %.4f], f(x0) = %.4f" % (ret.x[0],
                                                           ret.x[1],
                                                           ret.fun))
