import scipy
import matplotlib.pyplot as plt
from math import sqrt

s0=10.0
T=1.0
n=244*T
mu=0.15
sigma=0.2
n_simulation=10000

dt=T/n
s_array=[]

for i in range(n_simulation):
    s=s0
    for j in range(int(n)):
        e=scipy.random.normal()
        s=s+mu*s*dt+sigma*s*e*sqrt(dt)
    s_array.append(s)

plt.hist(s_array,alpha=0.6,bins=30,density=True,edgecolor='k')
plt.grid(ls='--')
plt.show()