# -*- coding: UTF-8 -*-
"""
@Time: 2018/9/26 11:40
@Author: TingTing W
"""


# ======================
# 输入：
#        myTree:    决策树
# 输出：
#        决策树文件
# ======================
def storeTree(inputTree, filename):
    '保存决策树'

    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()


# ========================
# 输入：
#        filename:    决策树文件名
# 输出：
#        pickle.load(fr):    决策树
# ========================
def grabTree(filename):
    '打开决策树'

    import pickle
    fr = open(filename)
    return pickle.load(fr)