#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16

import random
from perceptron import perceptron
from letter import letter

# process data
with open('letter-recognition.data', 'r') as f:
    data = f.read().split('\n')
#random.shuffle(data)

training_data = data[:10000] # data up to, not including data[10000]
testing_data = data[10000:] # data from data[10000] to the end of the list

# sort by letter (first element of list)
training_data = sorted(training_data)
testing_data = sorted(training_data)

# list of letters from training data
letters_list_training = []
for (i, training_data) in enumerate(training_data):
    letters_list_training.append(letter(training_data.split(',')))
    print letters_list_training[i].value
    print letters_list_training[i].attributes

# ###perceptron = perceptron('blarg')
# perceptron inputs are letter attributes from the training set attributes
# 16 attributes from letter -> perceptron inputs
###perceptron_inputs = a_training_letter.attributes

# print line debugging!
###print perceptron.weights
###print perceptron.bias