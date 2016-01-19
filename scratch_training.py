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
import copy

eta = 0.2  # learning rate is 0.2 for training perceptrons
#epochs = 4 # number of training epochs
matching_letters = []

#functions to train perceptrons

# run a perceptron through a training epoch
# Steps in epoch:
#   1. Test initial accuracy (preserve weights)
#   2. Train perceptrons (alter weights)
#   3. End of epoch: test accuracy
#       - Revert weights if accuracy goes down
#       - Break if accuracy has not improved
def training_epoch(perceptron):
    # Step 1) Test accuracy of perceptron[mn] for the matching letters [m] or [n]
    # test_accuracy runs perceptron.test() function for all matching letter instances
    accuracy = perceptron.test_accuracy(matching_letters)
    # adjust weights unless perceptron is already totally correct
    if accuracy < 1:
        ###print "accuracy < 1: ", accuracy
        # Step 2) Train perceptron
        # make a new interim perceptron that will be saved if there's improvements
        ###new_contender = perceptron.adjust_weights(perceptron, letter.attributes, letter.target)
        new_contender = copy.deepcopy(perceptron)
        new_contender.adjust_weights(letter.attributes, letter.target)
        # get the accuracy for the new potential perceptron
        accuracy_new_weights = new_contender.test_accuracy(matching_letters)
        # use new weights if accuracy has improved
        if accuracy_new_weights > accuracy:
            print "accuracy improved: new accuracy:", accuracy_new_weights, "old accuracy:", accuracy
            perceptron.update_weights(new_contender)
            return True # improvement has occurred
    else:
        # no training needed
        return False


# train perceptron until accuracy stops improving
def train(perceptron):
    another_epoch = True
    while another_epoch:
        another_epoch = training_epoch(perceptron)
    return

###    print letters_list_training[i].value
###    print letters_list_training[i].attributes

# create a dictionary of perceptrons
# such that all different letter combinations are represented
# perceptrons = {}
# for letter1 in string.ascii_uppercase:
#     for letter2 in string.ascii_uppercase:
#         if letter1 != letter2:
#             if letter2 + letter1 not in perceptrons:
#                 letters_combined = letter1 + letter2
#                 perceptrons[letters_combined] = perceptron()

# sublist of letters for testing
perceptrons_sublist = {}
for letter1 in string.ascii_uppercase:
    for letter2 in string.ascii_uppercase:
        if letter1 != letter2:
            if letter2 + letter1 not in perceptrons_sublist:
                letters_combined = letter1 + letter2
                perceptrons_sublist[letters_combined] = perceptron()

# print "perceptron sublist"
# for m, n in perceptrons_sublist:
#     print m, n

# for g, h in perceptrons_sublist:
#     print perceptrons_sublist[g+h].bias

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

# get a slice of the perceptrons dictionary to test training algorithm
# perceptrons_sublist = take(5, perceptrons.iteritems())
# for g, h in perceptrons_sublist:
#     print "sublist weights", perceptrons_sublist[g+h].weights

perceptron_increment = 1
for m, n in perceptrons_sublist: #m, n are the two letters in the perceptron representation (perceptron[kv])
    #print m, n

    print "\nTraining perceptron",perceptron_increment,"/", len(perceptrons_sublist)
    perceptron_increment += 1
    # collect matching letters m,n to train perceptron[mn]
    matching_letters = []
    for letter in letters_list_training:
        if m in letter.value:
            matching_letters.append(letter)
            # for letter in matching_letters:
            #     print letter.value
            #     print letter.attributes
            # set letter m to target 1
            letter.target = 1
        if n in letter.value:
            matching_letters.append(letter)
            # set letter n to target -1
            letter.target = -1
    # shuffle list of inputs
    random.shuffle(matching_letters)
    # for letter in matching_letters:
    #     print letter.value
    #     print letter.attributes
    #     print letter.target

    # print "matching letters outside of function",
    # for letter in matching_letters:
    #     print letter.value
    #    print letter.attributes

    # train perceptron
    train(perceptrons_sublist[m+n])

    # # preserve weights to revert if necessary
    # # saved_bias = np.array([])
    # # saved_weights = np.array([])
    # saved_bias = np.array(perceptrons_sublist[m+n].bias)
    # # print saved_bias == np.array(perceptrons[m+n].bias)[0]
    # # print np.array(perceptrons[m+n].bias)[0]
    # #print saved_bias is np.array(perceptrons[m+n].bias)
    #
    # # try:
    # #     saved_weights
    # # except NameError:
    # #     saved_weights = np.array([])
    # saved_weights = np.array([])
    # for i in range(0, len(np.array(perceptrons_sublist[m+n].weights))):
    #     saved_weights = np.append(saved_weights, np.array(perceptrons_sublist[m+n].weights)[i])
    #     # saved_weights.append(np.array(perceptrons[m+n].weights)[i])
    # print "Saved bias and weights: "
    # print saved_bias
    # print saved_weights
    #
    # for j in range(0, epochs):
    #     # Start epoch
    #     # Steps in epoch:
    #     #   1. Test initial accuracy (preserve weights)
    #     #   2. Train perceptrons (alter weights)
    #     #   3. End of epoch: test accuracy
    #     #       - Revert weights if accuracy goes down
    #     #       - Break if accuracy has not improved
    #
    #     # 1) Test accuracy of perceptron[mn] for the matching letters [m] or [n]
    #     # test_accuracy runs perceptron.test() function for all matching letter instances
    #     # num_accurate = perceptron.test_accuracy(perceptrons[m+n], matching_letters)
    #     num_accurate = perceptrons_sublist[m+n].test_accuracy(matching_letters)
    #     print "\nStart of epoch", j
    #     print "num accurate:", num_accurate
    #
    #     saved_bias = np.array(perceptrons_sublist[m+n].bias)
    #     saved_weights = np.array([])
    #     for i in range(0, len(np.array(perceptrons_sublist[m+n].weights))):
    #         saved_weights = np.append(saved_weights, np.array(perceptrons_sublist[m+n].weights)[i])
    #     print "Saved bias and weights in loop: "
    #     print saved_bias
    #     print saved_weights
    #
    #
    #     # 2) Train perceptron
    #     for letter in matching_letters[0:5]:
    #         # output = perceptron.test(perceptrons[m+n], letter.attributes)
    #         output = perceptrons_sublist[m+n].test(letter.attributes)
    #         # if perceptron doesn't return the expect output,
    #         # run training on perceptron to modify the weights
    #         if output != letter.target:
    #             print "output of perceptron test of", letter.value[0], "doesn't match target, train perceptron"
    #             # perceptron.train(perceptrons[m+n], letter.attributes, letter.target)
    #             perceptrons_sublist[m+n].train(letter.attributes, letter.target)
    #         if output == letter.target:
    #             print "output of perceptron test of", letter.value[0], "equals target, skip training"
    #
    #
    #     # 3) Test accuracy after weights have been updated
    #     # After weights have been updated, test accuracy of perceptron again
    #     # Revert weights if need be
    #     # num_accurate_revised = perceptron.test_accuracy(perceptrons[m+n], matching_letters)
    #     num_accurate_revised = perceptrons_sublist[m+n].test_accuracy(matching_letters)
    #     print "End of epoch, num accurate: ", num_accurate_revised
    #     # can use num_accurate at the end of the epoch
    #     #  as the num_accurate for the start of the next epoch
    #
    #     # revert weights if accuracy has worsened
    #     if(num_accurate_revised < num_accurate):
    #         print "Accuracy worse, revert weights"
    #         # perceptron.revert_weights(perceptrons[m+n], saved_bias, saved_weights)
    #         perceptrons_sublist[m+n].revert_weights(saved_bias, saved_weights)
    #
    #     # stop training if accuracy stops improving
    #     if (num_accurate_revised == num_accurate):
    #         if epochs != 0:
    #             print "No accuracy improvement, stopping training"
    #             break
    #
    #     # set accuracy to revised accuracy computed for this instance
    #     # for next epoch
    #    num_accurate = num_accurate_revised