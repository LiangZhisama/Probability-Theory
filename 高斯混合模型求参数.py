import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.datasets._samples_generator import make_blobs

X,y_true=make_blobs(n_samples=1000,centers=4)
fig,ax=plt.subplots(1,2,sharey='row')
ax[0].scatter(X[:,0],X[:,1],s=5,alpha=0.5)
ax[0].grid(ls='--')

gmm=GaussianMixture(n_components=4)
gmm.fit(X)
print('各分布的权重:')
print(gmm.weights_)
print('各分部的均值:')
print(gmm.means_)
print('各分部的协方差矩阵:')
print(gmm.covariances_)

print('样本点属于每个分布的概率（取前10个）：')
print(gmm.predict_proba(X)[:10].round(5))

labels=gmm.predict(X)
print('每个样本点所属的类别:')
print(labels)
ax[1].scatter(X[:,0],X[:,1],s=5,alpha=0.5,c=labels,cmap='viridis')
ax[1].grid(ls='--')
plt.show()