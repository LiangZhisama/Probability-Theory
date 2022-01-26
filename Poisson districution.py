#PMF:
#from scipy.stats import poisson
#import matplotlib.pyplot as plt
#
#fig,ax=plt.subplots(2,1)
#x = range(0,20)
#params=[10,2]
#for i in range(len(params)):
#    poisson_rv=poisson(mu=params[i])
#    mean,var,skew,kurt=poisson_rv.stats(moments='mvsk')
#    ax[i].plot(x,poisson_rv.pmf(x),'bo',ms=8)
#    ax[i].vlines(x,0,poisson_rv.pmf(x),colors='b',lw=5)
#    ax[i].set_title('$\\lambda$={}'.format(params[i]))
#    ax[i].set_xticks(x)
#    ax[i].grid(ls='--')
#    print('lambda={},E[x]={},V[x]={}'.format(params[i],mean,var))
#
#plt.show()

#samples collect & justify numerical features:
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

lambda_=2
data=poisson.rvs(mu=lambda_,size=100000)
#plt.figure()
plt.hist(data,density=True,alpha=0.6,edgecolor='k')
plt.gca().axes.set_xticks(range(0,11))
print('mean=',np.mean(data))
print('var=',np.square(np.std(data)))
plt.grid(ls='--')
plt.show()
