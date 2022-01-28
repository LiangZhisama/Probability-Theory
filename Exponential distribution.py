from scipy.stats import expon
import matplotlib.pyplot as plt
import numpy as np

#PDF:
#x=np.linspace(0,10,1000)
#expon_rv_0=expon()
#plt.plot(x,expon_rv_0.pdf(x),color="r",lw=3,alpha=0.6,label='$\\lambda$=1')
#expon_rv_1=expon(scale=2)
#plt.plot(x,expon_rv_1.pdf(x),color="b",lw=3,alpha=0.6,label='$\\lambda$=0,5',linestyle="--")
#plt.legend(loc='best',frameon=False)
#plt.grid(ls='--')
#plt.show()

#samples collect:
x=np.linspace(0,10,1000)
expon_rv=expon()
expon_rvs=expon_rv.rvs(100000)
plt.plot(x,expon_rv.pdf(x),color='r',lw=3,alpha=0.6,label='$\\lambda$=1')
plt.hist(expon_rvs,density=True,alpha=0.6,bins=50,edgecolor='k')
plt.legend(loc='best',frameon=False)
plt.grid(ls='--')
plt.show()