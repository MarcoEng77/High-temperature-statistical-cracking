import numpy as np
import random
import copy
from scipy.optimize import basinhopping
from scipy.optimize import minimize
from datetime import datetime


startTime = datetime.now()


random.seed(123)

# create k equidistributed points on a n-sphere using Marsaglia's algorithm


def sampling (k,n) :
    sampl = np.zeros((k,n))
    point=np.zeros(n)
    for i in range (k):
        point = np.repeat(1,n)
        while np.sqrt(point.dot(point))>=1:
            point = np.random.uniform(-1,1,n)
        sampl[i] = [h * (1/np.sqrt(point.dot(point))) for h in point  ] 
    return sampl


# for each point on the n-sphere, compute the equivalent amplitude given vectors of amplitudes, phase shifts and a point on the n-sphere


def eq_ampl(c, ome, a):
    ctot_sq = sum ( c[i]*a[i]*c[j]*a[j]*np.cos(ome[i]-ome[j]) for i in range (c.size ) for j in range(a.size)    )
    ctot = np.sqrt(ctot_sq)
    return ctot



# Compute damage vector for given the Basquin coeff., points on the n-sphere and amplitudes & phase shifts vectors 


def dam_vec ( spher_sampl, amplit, omega, beta):
    n =  spher_sampl.shape[0]
    dam = np.zeros(n)
    for i in range (n):
        dam [i]= np.power ( eq_ampl (amplit, omega , spher_sampl[i]), 1/beta)
    return dam
        


# Define actual loads 



c_act = np.array   ([ 1 , 2, 3, 1, 0.5, 0.2 ])
ome_act = np.array ([ 0, 20, 15, 5, 5, 15 ])

## define n-sphere sampling to be used and damage vector for actual loads


sampl_min = sampling (100,c_act.size)

dam_act = dam_vec ( sampl_min, c_act, ome_act, 2 )



# Define function to be minimised 

def func_min (x):
    siz = np.int( x.size / 2)
    f = np.sum (  np.power ( np.subtract ( dam_act, dam_vec (sampl_min, x[0:siz:1] ,  x[siz: ], 2  )) , 2) )
    return f

 
# Minimisation

guess = np.zeros((2*6))

minimizer_kwargs = {"method": "BFGS"}
res = basinhopping(func_min, guess,minimizer_kwargs = minimizer_kwargs, niter = 200)


#print("global minimum: x = %.4f, f(x0) = %.4f" % (res.x, res.fun))

#res = minimize(func_min, guess, method='Nelder-Mead', tol=1e-6)

print(datetime.now() - startTime)
             

        
     




    
