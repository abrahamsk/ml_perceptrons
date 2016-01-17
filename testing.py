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
import pprint

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
# dictionary for votes for letters (all alphabet letters valued at 0 to count votes)
intermed_votes = {c:i for i, c in enumerate(string.ascii_uppercase, 1)}
#print intermed_votes
votes = dict.fromkeys(intermed_votes.iterkeys(), 0)
#print votes

# convert list of letters to tuple to use as dictionary key
letters_tup_testing = tuple(letters_list_testing)

print "***Testing***"

# run all data instances through trained perceptrons
# to test accuracy
# for k, v in perceptrons: #k, v are the two letters in the perceptron representation (perceptron[kv])
#     for letter in letters_list_testing:
#         output = perceptron.test(perceptrons[k+v], letter.attributes)
#         if output == True:
#             #print "true loop: output: ", output
#             #print "correct: ", "k: ", k, "v: ", v
#             correct_test_output = correct_test_output + 1 # increment correct counter if input matches target
#             y_pred.append(k)
#             y_actu.append(k)
#         else:
#             #print letter.value
#             #print "else: output: ", output
#             #print "incorrect: ", "k: ", k, "v: ", v
#             incorrect_test_output = incorrect_test_output + 1
#             y_pred.append(k)
#             y_actu.append(v)

# for every letter, run through every perceptron
# and record votes for which letter perceptron returns
for letter in letters_list_testing:
    for k, v in perceptrons:
        actual_letter = str(letter.value[0])
        # print "actual letter ", actual_letter
        output = perceptron.test(perceptrons[k+v], letter.attributes)
        if output == True: # perceptron guessed first letter (i in perceptron[ij])
            ###pprint.pprint(votes)
            ###pprint.pprint(actual_letter)
            votes[actual_letter] += 1 # record a vote for that letter
        else:
            votes[perceptron[v]] += 1
print votes

# *********************
# print "correct ", correct_test_output
# print "incorrect ", incorrect_test_output
# total = correct_test_output + incorrect_test_output
# print "total: ", total
# accuracy = correct_test_output/total
# print "accuracy: ", accuracy

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

