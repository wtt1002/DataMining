# -*- coding: UTF-8 -*-
"""
@Time: 2018/9/25 15:13
@Author: TingTing W
"""

from algorithm.DecisionTrees import data_partition as dp
from algorithm.DecisionTrees import tree_build as tb
# ========================
# 输入：
#        inputTree:    决策树文件名
#        featLabels:    分类标签集
#        testVec:        待分类对象
# 输出：
#        classLabel:    分类结果
# ========================
def classify(inputTree, featLabels, testVec):
    '使用决策树分类'

    # 当前分类标签
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    # 找到当前分类标签在分类标签集中的下标
    featIndex = featLabels.index(firstStr)
    # 获取待分类对象中当前分类的特征值
    key = testVec[featIndex]

    # 遍历
    valueOfFeat = secondDict[key]

    # 子树分支则递归
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    # 叶子分支则返回结果
    else:
        classLabel = valueOfFeat

    return classLabel


def test():
    '测试'

    myDat, labels = tb.createDataSet()
    myTree = tb.createTree(myDat, labels)
    # 再创建一次数据的原因是创建决策树函数会将labels值改动
    myDat, labels = tb.createDataSet()
    print(classify(myTree, labels, [1, 1]))

if __name__ == '__main__':
    test()