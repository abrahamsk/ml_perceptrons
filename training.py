#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16
import string
from perceptron import perceptron
import letter
from input import letters_list_training


eta = 0.2 # eta is 0.2 for training perceptrons

###    print letters_list_training[i].value
###    print letters_list_training[i].attributes

# scheme for dictionary of dictionaries {char+char : perceptron instance}
perceptrons = {}
# for key in dict.iterkeys():
    # perceptrons[key] = {}
    # for key in dict.iterkeys():
        # perceptrons[key][key] = {}

# create perceptron combos
for i in string.ascii_lowercase:
		for j in string.ascii_lowercase:
			if i != j:
				if j+i not in perceptrons:
					#perceptrons[i+j] = "{\"w0\":0.1,\"w1\":0.2,\"w3\":0.3}"
					perceptrons[i + j] = perceptron()


#print perceptrons
# print perceptrons['ab']
# count = len(perceptrons)
# print count
# if count == 325:
# 	print "yay!"

# print line debugging!
###print perceptrons['ab'].weights
###print perceptrons['yz'].bias

#for letter in letters_list_training: print letter.value
for letter in letters_list_training:
    if letter.value == "Y":
        print "match"

# scheme for dictionary of dictionaries {char : {char : perceptron}}
# perceptrons = {}
# for key in dict.iterkeys():
#     perceptrons[key] = {}
#     for key in dict.iterkeys():
#         perceptrons[key][key] = {}
#
# perceptrons = {}
# for char_outer in ('A' to 'Y')
#     perceptrons[char_outer] = {}
#         for char_inner in char_outer+1 to 'Z'
#             perceptrons[char_outer][char_inner] = {}

#
# perceptron = perceptron(input.letters_list_training[i].attributes)
# perceptron inputs are letter attributes from the training set attributes
# 16 attributes from letter -> perceptron inputs
###perceptron_inputs = a_training_letter.attributes



