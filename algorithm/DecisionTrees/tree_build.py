# -*- coding: UTF-8 -*-
"""
@Time: 2018/9/25 11:34
@Author: TingTing W
"""
import operator

from algorithm.DecisionTrees import data_partition as dp


# ===============================================
# 输入：
#        classList: 类标签集
# 输出：
#        sortedClassCount[0][0]: 出现次数最多的标签
# ===============================================
def majorityCnt(classList):
    '采用多数表决的方式求出classList中出现次数最多的类标签'

    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]


# ===============================================
# 输入：
#        dataSet: 数据集
#        labels: 划分标签集
# 输出：
#        myTree: 生成的决策树
# ===============================================
def createTree(dataSet, labels):
    '创建决策树'

    # 获得类标签列表
    classList = [example[-1] for example in dataSet]

    # 递归终止条件一：如果数据集内所有分类一致
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    # 递归终止条件二：如果所有特征都划分完毕
    if len(dataSet[0]) == 1:
        # 将它们都归为一类并返回
        return majorityCnt(classList)

    # 选择最佳划分特征
    bestFeat = dp.chooseBestFeatureToSplit(dataSet)
    # 最佳划分对应的划分标签。注意不是分类标签
    bestFeatLabel = labels[bestFeat]
    # 构建字典空树
    myTree = {bestFeatLabel: {}}
    # 从划分标签列表中删掉划分后的元素
    del (labels[bestFeat])
    # 获取最佳划分对应特征的所有特征值
    featValues = [example[bestFeat] for example in dataSet]
    # 对特征值列表featValues唯一化，结果存于uniqueVals。
    uniqueVals = set(featValues)

    for value in uniqueVals:  # 逐行遍历特征值集合
        # 保存所有划分标签信息并将其伙同划分后的数据集传递进下一次递归
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(dp.splitDataSet(dataSet, bestFeat, value), subLabels)

    return myTree


# ==============================================
# 输入：
#        空
# 输出：
#        用于测试的数据集和划分标签集
# ==============================================
def createDataSet():

    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']

    return dataSet, labels


def test():
    '测试'

    myDat, labels = createDataSet()
    myTree = createTree(myDat, labels)
    print (myTree)


if __name__ == '__main__':
    test()