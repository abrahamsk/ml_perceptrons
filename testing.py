#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16

import string
from perceptron import perceptron
import letter
from input import letters_list_testing
from pandas_confusion import ConfusionMatrix


# create confusion matrix to describe performance
# of perceptron learning algorithm
# using pandas library
y_actual     = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
x_predicted = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
# confusion_matrix(x_predicted, y_actual)
# print confusion_matrix(x_predicted, y_actual)


cm = ConfusionMatrix(y_actual, x_predicted)
cm.print_stats()

