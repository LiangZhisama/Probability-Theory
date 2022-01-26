#PMF:
#import matplotlib.pyplot as plt
#from scipy.stats import geom
#
#fig,ax=plt.subplots(2,1)
#params=[0.5,0.25]
#x=range(1,11)
#for i in range(len(params)):
#    geom_rv=geom(p=params[i])
#    ax[i].set_title('p={}'.format(params[i]))
#    ax[i].plot(x,geom_rv.pmf(x),'bo',ms=8)
#    ax[i].vlines(x,0,geom_rv.pmf(x),colors='b',lw=5)
#    ax[i].set_xlim(0,10)
#    ax[i].set_ylim(0,0.6)
#    ax[i].set_xticks(x)
#    ax[i].set_yticks([0,0.1,0.2,0.3,0.4,0.5])
#    ax[i].grid(ls="--")
#
#plt.show()

#samples collect:
from scipy.stats import geom
import matplotlib.pyplot as plt
x=range(1,21)
geom_rv=geom(p=0.5)
geom_rvs=geom_rv.rvs(size=100000)
plt.hist(geom_rvs,bins=20,density=True,alpha=0.6,edgecolor='k')
plt.gca().axes.set_xticks(range(1,21))

mean,var,shew,kurt=geom_rv.stats(moments="mvsk")
print('mean={},var={}'.format(mean,var))
plt.grid(ls='--')
plt.show()