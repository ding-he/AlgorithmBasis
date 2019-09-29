# -- coding: utf-8 --
import numpy as np
import operator
import matplotlib.pyplot as plt

np.random.seed(123)


def createDataSet():
    # 创建训练集
    # group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    # labels = ['A', 'A', 'B', 'B']

    delta1 = np.random.normal(0, 1, [100, 2])
    delta2 = np.random.normal(0, 1, [100, 2]) + 4

    group = np.concatenate((delta1, delta2),axis=0)
    labels = ['A' for _ in range(delta1.shape[0])] + ['B' for _ in range(delta2.shape[0])]

    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]

    # 根据欧式距离计算训练集中每个样本到测试点的距离
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5

    # 计算完所有点的距离后，对数据按照从小到大的次序排序
    sortedDistIndicies = distances.argsort()

    # 确定前k个距离最小的元素所在的主要分类，最后返回发生频率最高的元素类别
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount


group, labels = createDataSet()
# print(group)
# print(labels)
x0, y0 = [1.5, 1.8]
print(classify0([x0, y0], group, labels, 20))
x = group[:, 0]
y = group[:, 1]
plt.scatter(x[:100], y[:100], c='r')
plt.scatter(x[100:], y[100:], c='b')
plt.scatter(x0, y0, c='g')
plt.show()
