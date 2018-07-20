#coding:utf-8
import vector
import logistic_regression
import SVM

filename = vector.vector('twitter_news')

print(logistic_regression.result(filename))
print('SVM',SVM.result(filename))
