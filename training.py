#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16
import string
import perceptron
import letter
import input


eta = 0.2 # eta is 0.2 for training perceptrons

###    print letters_list_training[i].value
###    print letters_list_training[i].attributes

# scheme for dictionary of dictionaries {char : {char : perceptron}}
perceptrons = {}
for key in dict.iterkeys():
    perceptrons[key] = {}
    for key in dict.iterkeys():
        perceptrons[key][key] = {}
# perceptrons = {}
# for char_outer in ('A' to 'Y')
#     perceptrons[char_outer] = {}
#         for char_inner in char_outer+1 to 'Z'
#             perceptrons[char_outer][char_inner] = {}

# perceptrons = dict.fromkeys(string.ascii_lowercase, 0)

# for i in range(325):
#     perceptrons.append(perceptron(i))
#
# perceptrons = []
# for ( score, gender ) in <some-data-source>:
#     perceptrons.append(perceptron())
#
# perceptron = perceptron(input.letters_list_training[i].attributes)
# perceptron inputs are letter attributes from the training set attributes
# 16 attributes from letter -> perceptron inputs
###perceptron_inputs = a_training_letter.attributes


# print line debugging!
print perceptron.weights
print perceptron.bias
