#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16

import string
from perceptron import perceptron
import letter
from training import perceptrons, letters_list_training
from input import letters_list_testing
from pandas_confusion import ConfusionMatrix

# track correct and incorrect output from perceptron
# correct_output is incremented when perceptron correctly
# classifies a letter input
# incorrect_output is incremented when perceptron incorrectly
# classifies letter input
correct_test_output = 0.0
incorrect_test_output = 0.0
accuracy = 0.0
# set up confusion matrix
y_actu = []
y_pred = []

print "***Testing***"

# run all data instances through trained perceptrons
# to test accuracy
for k, v in perceptrons: #k, v are the two letters in the perceptron representation (perceptron[kv])
    for letter in letters_list_testing:
        output = perceptron.test(perceptrons[k+v], letter.attributes)
        if output == True:
            #print "true loop: output: ", output
            #print "correct: ", "k: ", k, "v: ", v
            correct_test_output = correct_test_output + 1 # increment correct counter if input matches target
            y_pred.append(k)
            y_actu.append(k)
        else:
            #print letter.value
            #print "else: output: ", output
            #print "incorrect: ", "k: ", k, "v: ", v
            incorrect_test_output = incorrect_test_output + 1
            y_pred.append(k)
            y_actu.append(v)


print "correct ", correct_test_output
print "incorrect ", incorrect_test_output
total = correct_test_output + incorrect_test_output
print "total: ", total
accuracy = correct_test_output/total
print "accuracy: ", accuracy

# create confusion matrix to describe performance
# of perceptron learning algorithm
# using pandas library
##y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
##y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
# confusion_matrix(y_pred, y_actu)
# print confusion_matrix(y_pred, y_actu)

###cm = ConfusionMatrix(y_actu, y_pred)
###print("Confusion matrix:\n%s" % cm)
###cm.print_stats()

