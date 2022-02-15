import numpy as np
import random
import copy
from random import randrange
from scipy import stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time

def energy (x):
    x = np.asarray(x)
    energy = -np.power(x,2) + np.power(x,4)
    return energy

def tempInit(nres, T):
    temp = np.zeros(nres * len(T))
    for i in range (len(T)):
        for j in range(nres):
            a = j + nres*(i)
            temp [a] = T[i]
    return temp

def PosInit (nres, ntemp):
    initpos = np.zeros(nres*ntemp) - 1/ np.sqrt(2)
    return initpos

def newPos (x,eps, nres, ntemp):
    x = x + np.random.randint(-1,2, size=nres*ntemp) * eps
    return x

def acceptance(xOld, xNew, T, nres, ntemp):
    energy_old = energy(xOld)
    energy_new = energy (xNew)
    alfa = np.minimum(1, np.exp(-(1/T)*(energy_new-energy_old) ) )
    beta = np.random.uniform(0,1, nres * ntemp )
   # if beta < alfa:
    #    xOld = xNew
    xOld = np.where(beta < alfa, xNew, xOld)
    return  xOld

def main (T, nrealis, eps):
    ntemp = len(T)
    poszero = np.zeros(nrealis * ntemp)
    time = np.zeros(nrealis * ntemp)
    metatime = np.zeros(nrealis * ntemp)
    actual = PosInit(nrealis, ntemp)
    tempe = tempInit (nrealis, T)
    while np.any(metatime == 0):
                candidate = newPos(actual,eps, nrealis, ntemp)
                actual = acceptance(actual, candidate, tempe, nrealis, ntemp)
                metatime = np.where(actual > poszero , np.where(metatime !=0, metatime, time), metatime )
                time = time + 1
   # arrhenius = activEnergy(times, T - T_delta, T_delta, itera)
    return metatime

temparr = [0.021,0.023]

start = time.time()

res = main(temparr, 1000,0.1)

end = time.time()

res1 = np.reshape(res,(2,1000))

meantimes = np.mean(np.log(res1), axis=1)
#meantimes = np.mean(res1, axis=1)
meantimes

#x2 = np.log(meantimes)
x2 = meantimes
#tempes = (0.035,0.03,0.035)
y2 = (1/np.asarray(temparr)).reshape((-1, 1))
modelOne = LinearRegression()
modelOne.fit(y2, x2 )
modelOne.coef_



arrhen = (meantimes[0]-meantimes[1]) / (1/0.025-1/0.026)
print (arrhen)
print(end - start)
