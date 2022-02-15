import numpy as np
import random
import copy

from random import randrange

# create test vector

random.seed(123)

c = 1

# applied to a configuration count
def energy(vect):
 griffo = 1
 sigma =0.85
 energy = 2*griffo*vect - 0.3* sigma**2*vect**2
 return energy

def perturb (vect1):
    aux = copy.deepcopy(vect1)
    incre = np.random.normal(0,1)
    
    if aux + incre > 0:
        aux = aux + incre
    return aux

#applied to configurations    
def acceptance(old,new,T):
    energy_old = energy(old)
    energy_new = energy (new)
    alfa = min(1, np.exp(-(1/T)*(energy_new-energy_old) ) )
    beta = random.uniform(0,1)
    if beta < alfa:
        old = new
    return old

# checking expectation on two consecutive digits
#fava = config_count(test)
#print(test) 
#print(fava)
#f = np.linspace(0,c-1,num=c)
#consec = np.dot(fava,f)
#expect = consec / c
#print(expect)


# Main body

# initialise nihil configuration
T=1.2
T_delta=0.3
num_temp=3
num_trial = 500

times=np.zeros((num_temp,num_trial))

for j in range(1,num_temp+1):
    T=T-T_delta
    for i in range (1,num_trial+1):
     actual =  1
     time= 0
     while actual < 4.15:
       candidate = perturb(actual)
       actual = acceptance(actual, candidate, T)
       time=time+1
       times[j-1, i-1]=time-1
   
#extract averages
res=np.zeros(num_temp)
for i in range (0,num_temp):
    res[i] = np.average(times[i,:])
    
    


