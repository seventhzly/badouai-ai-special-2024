import numpy as np
class cpca:
    def __init__(self,X,K):
        self.X=X
        self.K=K
        self.C=[]
        self.U=[]
        self.Z=[]
        self.C=self.centralize()
        self.U=self.eigen()
        self.Z=self.dot()

    def centralize(self):
        C=self.X-self.X.mean(axis=0)
        print("中心化后的矩阵是\n",C)
        return C

    def eigen(self):
        cov=np.dot(self.C.T,self.C)/(self.X.shape[0]-1)
        a, b = np.linalg.eig(cov)
        ind=np.argsort(-a)
        UT=[b[:,ind[i]] for i in range(self.K)]
        print("特征向量矩阵是\n",U)
        return U

    def dot(self):
        Z=np.dot(self.X,self.U)
        print("样本矩阵的降维矩阵是\n",Z)
        return Z

if __name__=="__main__":
    X = np.array([[10, 15, 29],
                  [15, 46, 13],
                  [23, 21, 30],
                  [11, 9, 35],
                  [42, 45, 11],
                  [9, 48, 5],
                  [11, 21, 14],
                  [8, 5, 15],
                  [11, 12, 21],
                  [21, 20, 25]])
    pca=cpca(X,2)

