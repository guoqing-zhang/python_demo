# -*- coding: utf-8 -*-
# Created : 2020/3/30 10:49
# Author  : zhangguoqing
# E-mail  : zhangguoqing84@westlake.edu.cn

from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
result = clf.predict(iris.data[:1,:])
result_prob = clf.predict_proba(iris.data[:1,:])
print(result)
print(result_prob)
