import numpy as np
import matplotlib.pyplot as plt

#case1:(by binomial distribution)
#from scipy.stats import binom
#n=10
#p=0.4
#sample_size=15000
#expected_value=n*p
#N_samples=range(1,sample_size,10)
#for k in range(3):
#    binom_rv=binom(n=n,p=p)
#    X=binom_rv.rvs(size=sample_size)
#    sample_average=[X[:i].mean() for i in N_samples]
#    plt.plot(N_samples,sample_average,label='average of sample {}'.format(k))
#
#plt.plot(N_samples,expected_value*np.ones_like(sample_average),ls='--'
#    ,label='true expected value:n*p={}'.format(n*p),c='k')
#
#plt.legend()
#plt.grid(ls='--')
#plt.show()

#case2:(by normal distribution)
from scipy.stats import norm
norm_rvs = norm(loc=0,scale=20).rvs(size=1000000)
plt.hist(norm_rvs,density=True,alpha=0.3,color='b',bins=100,label='original')

mean_array=[]
for i in range(10000):
    sample = np.random.choice(norm_rvs,size=5,replace=False)
    mean_array.append(np.mean(sample))
plt.hist(mean_array,density=True,alpha=0.3,color='r',bins=100,label='sample size=5')

for i in range(10000):
    sample=np.random.choice(norm_rvs,size=50,replace=False)
    mean_array.append(np.mean(sample))
plt.hist(mean_array,density=True,alpha=0.3,color='g',bins=100,label='sample size=50')

plt.gca().axes.set_xlim(-60,60)
plt.legend(loc='best')
plt.grid(ls='--')
plt.show()