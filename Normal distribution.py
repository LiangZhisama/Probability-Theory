from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

#PDF:
#fig,ax=plt.subplots(1,1)
#norm_0 = norm(loc=0,scale=1)
#norm_1 = norm(loc=1,scale=2)
#
#x=np.linspace(-10,10,1000)
#ax.plot(x,norm_0.pdf(x),color='red',lw=3,alpha=0.6,label='loc=0,scale=1')
#ax.plot(x,norm_1.pdf(x),color='blue',lw=3,alpha=0.6,label='loc=1,scale=2',linestyle="--")
#ax.legend(loc='best',frameon=False)
#plt.grid(ls='--')
#plt.show()

#samples collect:
norm_rv = norm(loc=2,scale=2)
norm_rvs=norm_rv.rvs(size=100000)
x=np.linspace(-10,10,1000)
plt.plot(x,norm_rv.pdf(x),'r',lw=3,alpha=0.6,label="$\\mu$=2,$\\sigma=2$")
plt.hist(norm_rvs,density=True,bins=50,alpha=0.6,edgecolor='k')
plt.legend()
plt.grid(ls="--")
plt.show()