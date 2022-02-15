import numpy as np
import random
import copy

from random import randrange

# create test vector

random.seed(123)

c = 15
min_cra = 4



test = np.random.randint(2, size=c-2)

test = np.append(np.zeros(1), test)
test = np.append (test, np.zeros(1))

def config_count(b):
 leng = 0
 res = np.zeros(len(b))
 for i in range(1,len(b)): 
  if (b[i]==0 and b[i-1]==1):
      res[leng-1] = res[leng-1]+1
      leng=0
  if (b[i]==1):
   leng = leng+1
 return res

# applied to a configuration count
def energy(vect):
 griffo = 1
 sigma =0.7
 ene = np.zeros(len(vect))
 for i in range (1,len(vect)):
  ene[i-1] = vect[i-1] * (griffo*(i) - sigma**2*(i)**2/3 )
 energy = np.sum(ene)
 return energy


def swap (b):
    aux = copy.deepcopy(b)
    randelem = randrange(1,len(b))
    if aux[randelem] ==1:
     aux[randelem] = 0
    else:
     aux[randelem]=1
    return aux


#applied to configurations    
def acceptance(old,new,T):
    energy_old = energy(config_count(old))
    energy_new = energy (config_count(new))
    alfa = min(1, np.exp(-(1/T)*(energy_new-energy_old) ) )
    beta = random.uniform(0,1)
    if beta < alfa:
        old = new
    return old

     
         
     


# checking expectation on two consecutive digits
fava = config_count(test)
#print(test) 
#print(fava)
f = np.linspace(0,c-1,num=c)
consec = np.dot(fava,f)
expect = consec / c
print(expect)




# Main body

# initialise nihil configuration
T=4.1
T_delta=1
num_temp=4

times=np.zeros((num_temp,10))

for j in range(1,num_temp+1):
    T=T-T_delta
    for i in range (1,11):
     actual = np.zeros(c)
     time= 0
     while np.sum(config_count(actual)[min_cra:c]) == 0:
       candidate = swap(actual)
       actual = acceptance(actual, candidate, T)
       time=time+1
       times[j-1, i-1]=time-1
   
   
     


