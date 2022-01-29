import numpy as np
import matplotlib.pyplot as plt

#mean=np.array([0,0])
#conv_1=np.array([[1,0],[0,1]])
#conv_2=np.array([[4,0],[0,0.25]])
#
#x_1,y_1=np.random.multivariate_normal(mean=mean,cov=conv_1,size=5000).T
#x_2,y_2=np.random.multivariate_normal(mean=mean,cov=conv_2,size=5000).T
#plt.figure(figsize=(6,6))
#plt.plot(x_1,y_1,'ro',alpha=0.05)
#plt.plot(x_2,y_2,'bo',alpha=0.05)
#plt.gca().axes.set_xlim(-6,6)
#plt.gca().axes.set_ylim(-6,6)
#plt.grid(ls='--')
#plt.show()

fig,ax=plt.subplots(2,2)
mean=np.array([0,0])

conv_1=np.array([[1,0],[0,1]])
conv_2=np.array([[1,0.3],[0.3,1]])
conv_3=np.array([[1,0.85],[0.85,1]])
conv_4=np.array([[1,-0.85],[-0.85,1]])

x_1,y_1=np.random.multivariate_normal(mean=mean,cov=conv_1,size=3000).T
x_2,y_2=np.random.multivariate_normal(mean=mean,cov=conv_2,size=3000).T
x_3,y_3=np.random.multivariate_normal(mean=mean,cov=conv_3,size=3000).T
x_4,y_4=np.random.multivariate_normal(mean=mean,cov=conv_4,size=3000).T

ax[0][0].plot(x_1,y_1,'bo',alpha=0.05)
ax[0][1].plot(x_2,y_2,'bo',alpha=0.05)
ax[1][0].plot(x_3,y_3,'bo',alpha=0.05)
ax[1][1].plot(x_4,y_4,'bo',alpha=0.05)

ax[0][0].grid(ls='--')
ax[0][1].grid(ls='--')
ax[1][0].grid(ls='--')
ax[1][1].grid(ls='--')
plt.show()