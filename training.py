#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16
import perceptron
import letter
import input

learning_rate = 0.2 # eta is 0.2 for training perceptrons

###    print letters_list_training[i].value
###    print letters_list_training[i].attributes
perceptrons = []
for i in range(325):
    perceptrons.append(perceptron(i))

perceptron = perceptron(input.letters_list_training[i].attributes)
# perceptron inputs are letter attributes from the training set attributes
# 16 attributes from letter -> perceptron inputs
###perceptron_inputs = a_training_letter.attributes


# print line debugging!
print perceptron.weights
print perceptron.bias
