#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16

import string
from perceptron import perceptron
import letter
from input import letters_list_training
import random
import numpy as np

# get stats for perceptron run
def get_stats(correct_output, incorrect_output, accuracy, accuracy_prev):
    print "correct: ", correct_output
    print "incorrect: ", incorrect_output
    total = correct_output + incorrect_output
    print "total: ", total

    print "accuracy before comparison ", accuracy
    print "prev accuracy before comparison ", accuracy_prev

    return total


eta = 0.2  # learning rate is 0.2 for training perceptrons
epochs = 5 # start with 5, work up to 30

###    print letters_list_training[i].value
###    print letters_list_training[i].attributes

# create a dictionary of perceptrons
# such that all different letter combinations are represented
perceptrons = {}
for letter1 in string.ascii_uppercase:
    for letter2 in string.ascii_uppercase:
        if letter1 != letter2:
            if letter2 + letter1 not in perceptrons:
                # perceptrons[i+j] = {w0":0.1,"w1":0.2,"w3":0.3}
                letters_combined = letter1 + letter2
                perceptrons[letters_combined] = perceptron()

# print perceptrons
# print perceptrons['AB']
# count = len(perceptrons)
# print count
# if count == 325:
# 	print "325 perceptrons"

# print line debugging!
#print perceptrons['AZ'].weights
#print perceptrons['AZ'].bias


# # for letter in letters_list_training: print letter.value
# for letter in letters_list_training:
# ###    print type(letter.attributes) is list
# ###    print [float(i) for i in letter.attributes]
#     if 'A' in letter.value: #or 'Z' in letter.value:
#         perceptron.train(perceptrons['AZ'], letter.attributes, 1.0)
#         ### for i in range(len(letter.attributes)):
#         ###    print letter.attributes[i]
#         perceptron.test(perceptrons['AZ'], letter.attributes)
#         #print letter.attributes
#         #print letter.value
#         #print "match"

# track correct and incorrect output from perceptron
# correct_output is incremented when perceptron correctly
# classifies a letter input
# incorrect_output is incremented when perceptron incorrectly
# classifies letter input
correct_output = 0.0
incorrect_output = 0.0
# at the end of an epoch, test accuracy of perceptron
# and revert to old weights using perceptron class method if
# accuracy has gotten worse
accuracy = 0.0
accuracy_prev = 0.0

# loop through dictionary of perceptron instances
# and train perceptron for matching input
# e.g. perceptron[AB] gets all A and all B training instances
# from the training data
#for i in range (1, len(perceptrons)):
print "***Training***"

matching_letters = []
# shuffle letters
random.shuffle(letters_list_training)
# for letter in letters_list_training:
#     print letter.value[0]

for m, n in perceptrons: #m, n are the two letters in the perceptron representation (perceptron[kv])
    print m, n
    # collect matching letters m,n to train perceptron[mn]
    for letter in letters_list_training:
        if m in letter.value:
            matching_letters.append(letter)
            # for letter in matching_letters:
            #     print letter.value
            #     print letter.attributes
            # match letter m to target 1
            letter.target = 1
        if n in letter.value:
            matching_letters.append(letter)
            # match letter n to target -1
            letter.target = -1
    # shuffle list of inputs
    random.shuffle(matching_letters)
    # for letter in matching_letters:
    #     print letter.value
    #     print letter.attributes
    #     print letter.target

    # preserve weights to revert if necessary
    saved_bias = np.array([])
    saved_weights = np.array([])
    saved_bias = perceptron.save_bias(perceptrons[m+n])
    saved_weights =  perceptron.save_weights(perceptrons[m+n])
    print saved_bias
    print saved_weights

    for i in range(0, epochs):
        # Start epoch
        # Steps in epoch:
        #   1. Test initial accuracy (preserve weights)
        #   2. Train perceptrons (alter weights)
        #   3. End of epoch: test accuracy
        #       - Revert weights if accuracy goes down
        #       - Break if accuracy has not improved

        saved_bias = perceptron.save_bias(perceptrons[m+n])
        saved_weights =  perceptron.save_weights(perceptrons[m+n])
        # 1) Test accuracy of perceptron[mn] for the matching letters [m] or [n]
        # test_accuracy runs perceptron.test() function for all matching letter instances
        num_accurate = perceptron.test_accuracy(perceptrons[m+n], matching_letters)
        print "Start of epoch, num accurate: ", num_accurate

        # 2) Train perceptron
        for letter in matching_letters:
            perceptron.train(perceptrons[m+n], letter.attributes, letter.target)

        # 3) Test accuracy after weights have been updated
        # After weights have been updated, test accuracy of perceptron again
        # Revert weights if need be
        num_accurate_revised = perceptron.test_accuracy(perceptrons[m+n], matching_letters)
        print "End of epoch, num accurate: ", num_accurate_revised
        # can use num_accurate at the end of the epoch
        #  as the num_accurate for the start of the next epoch

        # revert weights if accuracy has worsened
        if(num_accurate_revised < num_accurate):
            print "Accuracy worse, revert weights"
            perceptron.revert_weights(perceptrons[m+n], saved_bias, saved_weights)

        # stop training if accuracy stops improving
        if (num_accurate_revised == num_accurate):
            print "No accuracy improvement, stopping training"
            break

        # revise accuracy for next epoch run
        print "Reassigning accuracy for next epoch start"
        print "num_accurate before: ", num_accurate
        print "num_accurate_revised before: ", num_accurate_revised
        num_accurate_revised = num_accurate
        print "num_accurate after: ", num_accurate
        print "num_accurate_revised after: ", num_accurate_revised





#     for i in range(0, epochs):
#         # compute accuracy of perceptron before epoch begins
#
#         # reset values for counts for each new epoch
#         correct_output = 0.0
#         incorrect_output = 0.0
#         total = 0.0
#
#         #print "\nEpoch", i, "begins! "
#         # for k in letters_list_training:
#         #     for v in letters_list_training:
#         #         if k != v:
#         for letter in letters_list_training:
#             #print letter.value
#             if m in letter.value:
#                 # test perceptrons that contain the letter matching m in perceptron[mn]
#                 output = perceptron.test(perceptrons[m + n], letter.attributes)
#                 # if perceptron output is true, sgn((dot product(w,x))) is positive
# ##                print "output: ", output
#                 if output == True:
#                     correct_output = correct_output + 1 # increment correct counter if input matches target
# #                    print "+ Input m: ", m, " from perceptron ", m,n, " result: ", m
#                 else:
#                     incorrect_output = incorrect_output + 1
#                     # set t = 1 for input m in perceptron[mn]
#                     perceptron.train(perceptrons[m + n], letter.attributes, 1.0)
# #                    print "- Input m: ", m, " from perceptron ", m,n, " result: ", n
#             if n in letter.value:
#                 # test perceptrons that contain the letter matching m in perceptron[mn]
#                 output = perceptron.test(perceptrons[m + n], letter.attributes)
# ##                print "output: ", output
#                 if output == True:
#                     correct_output = correct_output + 1 # increment correct counter if input matches target
# #                    print ">>> + Input n: ", n, " from perceptron ", m,n, " result: ", n
#                 else:
#                     incorrect_output = incorrect_output + 1
#                     # set t = -1 for input n in perceptron[mn]
#                     perceptron.train(perceptrons[m + n], letter.attributes, -1.0)
# #                    print ">>> - Input n: ", n, " from perceptron ", m,n, " result: ", m
#         print "\nEpoch", i, "ends, compute correctness/accuracy next "
#         #get_stats(correct_output, incorrect_output, accuracy, accuracy_prev)
#         print "\ncorrect: ", correct_output
#         print "incorrect: ", incorrect_output
#         total = correct_output + incorrect_output
#         print "total: ", total
#
#         print "accuracy before comparison ", accuracy
#         print "prev accuracy before comparison ", accuracy_prev
#
#          # revert weights if accuracy has gotten worse
#         if(accuracy < accuracy_prev):
#             print "reverting weights"
#             perceptron.revert_weights(perceptrons[m + n])
#             # for k in perceptrons:
#             #     if (perceptron.check_result(perceptrons[k])) == False:
#             #         perceptron.revert_weights(perceptrons[k])
#
#         accuracy_prev = accuracy # store previous accuracy for comparison (initialized to 0 at training start)
#         print "new previous accuracy: ", accuracy_prev
#         accuracy = correct_output/total
#         print " accuracy: ", accuracy
#
#         # stop training if accuracy stops improving
#         if (accuracy == accuracy_prev and accuracy != 0):
#             print "no accuracy improvement"
#             break
