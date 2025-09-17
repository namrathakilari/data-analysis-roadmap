import numpy as np
arr=np.array([10,20,30,40])
newarr=arr*2
print(newarr)

a1=np.array([1,2,3])
a2=np.array([4,5,6])
n1=np.concatenate((a1,a2))
print(n1)

a3=np.array([1,4,5,6,7])
maximum=np.max(a3)
minimum=np.min(a3)
sums=np.sum(a3)
mean=np.mean(a3)
print("Maximum:",maximum)
print("Minimum:",minimum)
print("Sum:",sums)
print("mean:",mean)

aa=np.arange(1,21)
y=np.where(aa%2==0)
print(y)