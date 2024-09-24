import numpy as np
class pca:
    def __init__(self,X,K):
        self.X=X
        self.K=K
    def cpca(self):
        centralize=self.X-np.array([np.mean(i) for i in self.X.T])
        cov=np.dot(centralize.T,centralize)
        a,b=np.linalg.eig(cov)
        ind=np.argsort(-a)
        UT=[b[:,ind[i]] for i in range(self.K)]
        return np.dot(self.X,np.transpose(UT))


X = np.array([[10, 15, 29],
              [15, 46, 13],
              [23, 21, 30],
              [11, 9,  35],
              [42, 45, 11],
              [9,  48, 5],
              [11, 21, 14],
              [8,  5,  15],
              [11, 12, 21],
              [21, 20, 25]])
y = pca(X,2)
newX = y.cpca()
print(newX)