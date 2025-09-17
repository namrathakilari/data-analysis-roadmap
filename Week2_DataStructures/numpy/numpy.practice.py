import numpy as np
from numpy import random as rd 
x=rd.randint(10,size=(3,3))
print(x)

y=rd.randint(100,size=(10))
sd=np.std(y)
print(sd)

a1=np.array([1,2,3])
a2=np.array([4,5,6])
a=np.dot(a1,a2)
print(a)