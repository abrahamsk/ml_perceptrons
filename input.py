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



# with open('training_data_test.txt', 'w+') as f_training_out:
#      for row in training_data:
#          ###print row
#          f_training_out.write("%s\n" % str(row))
#
# with open('testing_data_test.txt', 'w+') as f_testing_out:
#      for row in testing_data:
#          ###print row
#          f_testing_out.write("%s\n" % str(row))

# instantiate letter and perceptron class
###a_training_letter = letter()
###perceptron = perceptron('blarg')

# read in from files
### with open('letter-recognition_training.data') as f:
###     lines = (line.rstrip('\n') for line in open(f))

# perceptron inputs are letter attributes from the training set attributes
# 16 attributes from letter -> perceptron inputs
###perceptron_inputs = a_training_letter.attributes

# print line debugging!
print perceptron.weights
print perceptron.bias