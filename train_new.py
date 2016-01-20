#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16

from perceptron import perceptron
from input import letters_list_training
import random, copy, sys, string

######################
# function definitions
######################

def training_epoch(perceptron, p_id):
    # run all training instances through perceptron
    # adjust weights if perceptron isn't 100% accurate
    # return true if epoch improved perceptron accuracy
    # false otherwise

    #shuffle training data
    random.shuffle(letters_list_training)

    initial_accuracy = perceptron.test_accuracy(p_id)

    ####print "initial accuracy", initial_accuracy
    if initial_accuracy < 1.0:
        # change at least one weight if perceptron isn't accurate for all instances
        # make a temp perceptron to change weights and test without committing weight changes yet
        new_contender = copy.deepcopy(perceptron)
        # adjust weights if test for instance is wrong
        # don't need to pass in matching letters, it's a global
        new_contender.adjust_weights(p_id)
        # test accuracy of new weights
        new_accuracy = new_contender.test_accuracy(p_id)
        ### print "new accuracy", new_accuracy
        if new_accuracy > initial_accuracy:
            # commit weight changes
            perceptron.update_weights(new_contender)
            return True # perceptron has been improved
    return False # no improvements made

def train(perceptron, p_id):
    # run one perceptron through epochs until false is returned from training_epoch
    run_again = True
    while (run_again):
        run_again = training_epoch(perceptron, p_id)
    return

#################
# data structures
#################
# create a dictionary of perceptrons
# such that all different letter combinations are represented
perceptrons = {}
for letter1 in string.ascii_uppercase:
    for letter2 in string.ascii_uppercase:
        if letter1 != letter2:
            if letter2 + letter1 not in perceptrons:
                letters_combined = letter1 + letter2
                perceptrons[letters_combined] = perceptron()

# loop through dictionary of perceptron instances
# and train perceptron for matching input
# e.g. perceptron[AB] gets all A and all B training instances
# from the training data
#for i in range (1, len(perceptrons)):

# matching_letters = []
# # shuffle letters
# random.shuffle(letters_list_training)

#######
# main
#######
perceptron_increment = 1
#
for m, n in perceptrons: #m, n are the two letters in the perceptron representation (perceptron[kv])
    # print "---------------------------------------",m, n
    # text = "\rTraining perceptron "+str(perceptron_increment)+"/"+str(len(perceptrons))
    # sys.stdout.write(text)
    perceptron_increment += 1
    # train this perceptron for all training instances
    train(perceptrons[m+n], m+n)
    #train(perceptron[m+n], m+n)