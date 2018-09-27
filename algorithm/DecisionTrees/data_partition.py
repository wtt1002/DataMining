# -*- coding: UTF-8 -*-
"""
@Time: 2018/9/25 10:58
@Author: TingTing W
"""

# ==============================================
# 输入：
#        dataSet: 数据集文件名(含路径)
# 输出：
#        shannonEnt: 输入数据集的香农熵
# ==============================================
from math import log


def calcShannonEnt(dataSet):
    '计算香农熵'

    # 数据集个数
    numEntries = len(dataSet)
    # 标签集合
    labelCounts = {}
    for featVec in dataSet:  # 行遍历数据集
        # 当前标签
        currentLabel = featVec[-1]
        # 加入标签集合
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    # 计算当前数据集的香农熵并返回
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)

    return shannonEnt


# ==============================================
# 输入：
#        dataSet: 训练集文件名(含路径)
#        axis: 用于划分的特征的列数
#        value: 划分值
# 输出：
#        retDataSet: 划分后的子列表
# ==============================================
def splitDataSet(dataSet, axis, value):
    '数据集划分'

    # 划分结果
    retDataSet = []
    for featVec in dataSet:  # 逐行遍历数据集
        if featVec[axis] == value:  # 如果目标特征值等于value
            # 抽取掉数据集中的目标特征值列
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            # 将抽取后的数据加入到划分结果列表中
            retDataSet.append(reducedFeatVec)
    # print(retDataSet)
    return retDataSet


# ===============================================
# 输入：
#        dataSet: 数据集
# 输出：
#        bestFeature: 和原数据集熵差最大划分对应的特征的列号
# ===============================================
def chooseBestFeatureToSplit(dataSet):
    '选择最佳划分方案'

    # 特征个数
    numFeatures = len(dataSet[0]) - 1
    # 原数据集香农熵
    baseEntropy = calcShannonEnt(dataSet)
    # 暂存最大熵增量
    bestInfoGain = 0.0
    # 和原数据集熵差最大的划分对应的特征的列号
    bestFeature = -1

    for i in range(numFeatures):  # 逐列遍历数据集
        # 获取该列所有特征值
        featList = [example[i] for example in dataSet]
        # 将特征值列featList的值唯一化并保存到集合uniqueVals
        uniqueVals = set(featList)

        # 新划分法香农熵
        newEntropy = 0.0
        # 计算该特征划分下所有划分子集的香农熵，并叠加。
        for value in uniqueVals:  # 遍历该特征列所有特征值
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)

        # 保存所有划分法中，和原数据集熵差最大划分对应的特征的列号。
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature

# ==============================================
# 输入：
#        空
# 输出：
#        dataSet: 测试数据集列表
# ==============================================
def createDataSet():
    '创建测试数据集'

    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]

    return dataSet


def test():
    '测试'

    # 创建测试数据集
    myDat = createDataSet()
    # 求出其熵并打印
    print (chooseBestFeatureToSplit(myDat))


if __name__ == '__main__':
    test()