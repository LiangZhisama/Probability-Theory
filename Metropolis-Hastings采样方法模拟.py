import random
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

def pi(x):
    return (0.3*np.exp(-(x-0.3)**2)+0.7*np.exp(-(x-2.)**2/0.3))/1.2113

m=10000
N=100000
sample = [0 for i in range(m+N)]

sample[0]=2
for t in range(1,m+N):
    x=sample[t-1]
    x_star=norm.rvs(loc=x,scale=1,size=1)[0]
    alpha=min(1,(pi(x_star)/pi(x)))
    u=random.uniform(0,1)
    if u<alpha:
        sample[t]=x_star
    else:
        sample[t]=x

x=np.arange(-2,3,0.01)
plt.plot(x,pi(x),color='r',lw=3,label='Original Curve')
plt.hist(sample[m:],bins=100,density=True,edgecolor='k',alpha=0.6)
plt.grid(ls='--')
plt.legend()
plt.show()
