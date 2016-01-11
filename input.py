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

letters_list = []
for (i, training_data) in enumerate(training_data):
    letters_list.append(letter(training_data.split(',')))
    print letters_list[i].value
    print letters_list[i].attributes

# letters_list = []
#
# for i in enumerate(training_data):
#     letters_list.append(letter(training_data.split(',')))
#
# #later
#
# for obj in letters_list:
#     print letters_list.value


# # instantiate letter and perceptron class
# for (i, training_data) in enumerate(training_data):
#     ###print i, training_data[:1], training_data[1:], '\n', training_data
#     ###training_data = training_data.replace(',','')
#     a_training_letter = letter(training_data.split(','))
# ###perceptron = perceptron('blarg')

# read in from files
### with open('letter-recognition_training.data') as f:
###     lines = (line.rstrip('\n') for line in open(f))

# perceptron inputs are letter attributes from the training set attributes
# 16 attributes from letter -> perceptron inputs
###perceptron_inputs = a_training_letter.attributes

# print line debugging!
###print perceptron.weights
###print perceptron.bias
# print a_training_letter.value
# print a_training_letter.attributes
# print a_training_letter.attributes[0]
# print a_training_letter.attributes[1]
# print a_training_letter.attributes[2]
# print a_training_letter.attributes[3]
# total = a_training_letter.attributes[3]+a_training_letter.attributes[3]
# print total