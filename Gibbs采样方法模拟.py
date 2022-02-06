import numpy as np
import matplotlib.pyplot as plt

def p_x1_given_x2(x2,mu,sigma):
    mu=mu[0]+sigma[0][1]/sigma[1][1]*(x2-mu[1])
    sigma=sigma[0][0]-sigma[0][1]*sigma[1][0]/sigma[1][1]
    return np.random.normal(mu,sigma)

def p_x2_given_x1(x1,mu,sigma):
    mu=mu[1]+sigma[1][0]/sigma[0][0]*(x1-mu[0])
    sigma=sigma[1][1]-sigma[1][0]*sigma[0][1]/sigma[0][0]
    return np.random.normal(mu,sigma)

def gibbs_sampling(mu,sigma,samples_period):
    samples=np.zeros((samples_period,2))
    x2=np.random.rand()*10
    for i in range(samples_period):
        x1=p_x1_given_x2(x2,mu,sigma)
        x2=p_x2_given_x1(x1,mu,sigma)
        samples[i,:]=[x1,x2]
    return samples

mus=np.array([2,4])
sigmas=np.array([[1,.7],
                [.7,1]])

burn_period = int(1e4)
samples_period=int(1e5)

samples=gibbs_sampling(mus,sigmas,samples_period)[burn_period:]
plt.plot(samples[:,0],samples[:,1],'ro',alpha=0.05,markersize=1)
plt.grid(ls='--')
plt.show()