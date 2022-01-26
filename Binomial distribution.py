#PMF:
#import matplotlib.pyplot as plt
#from scipy.stats import binom
#
#fig,ax=plt.subplots(3,1)
#params=[(10,0.25),(10,0.5),(10,0.8)]
#x=range(0,11)
#for i in range(len(params)):
#    binom_rv=binom(n=params[i][0],p=params[i][1])
#    ax[i].set_title('n={},p={}'.format(params[i][0],params[i][1]))
#    ax[i].plot(x,binom_rv.pmf(x),'bo',ms=8)
#    ax[i].vlines(x,0,binom_rv.pmf(x),colors='b',lw=3)
#    ax[i].set_xlim(0,10)
#    ax[i].set_ylim(0,0.35)
#    ax[i].set_xticks(x)
#    ax[i].set_yticks([0,0.1,0.2,0.3])
#    ax[i].grid(ls="--")
#
#plt.show()

#samples collect:
#import matplotlib.pyplot as plt
#from scipy.stats import binom
#
#fig,ax=plt.subplots(3,1)
#params=[(10,0.25),(10,0.5),(10,0.8)]
#x=range(0,11)
#for i in range(len(params)):
#    binom_rv=binom(n=params[i][0],p=params[i][1])
#    rvs=binom_rv.rvs(size=100000)
#    ax[i].hist(rvs,bins=11,density=False,alpha=0.6,edgecolor='k')
#    ax[i].set_title('n={},p={}'.format(params[i][0],params[i][1]))
#    ax[i].set_xlim(0,10)
#    ax[i].set_ylim(0,0.4)
#    ax[i].set_xticks(x)
#    ax[i].grid(ls="--")
#    print('rvs:{}:{}'.format(i,rvs))
#
#plt.show()

#justify numerical features:
import numpy as np
from scipy.stats import binom
binom_rv = binom(n=10,p=0.25)
mean,var,skew,kurt=binom_rv.stats(moments='mvsk')
binom_rvs=binom_rv.rvs(size=100000)
E_sim=np.mean(binom_rvs)
S_sim=np.std(binom_rvs)
V_sim=S_sim*S_sim

print("mean={},var={}".format(mean,var))
print("E_sim={},V_sim={}".format(E_sim,V_sim))
