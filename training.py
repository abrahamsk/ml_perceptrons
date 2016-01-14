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

# scheme for dictionary of dictionaries {char : {char : perceptron}}
perceptrons = {}
# for key in dict.iterkeys():
    # perceptrons[key] = {}
    # for key in dict.iterkeys():
        # perceptrons[key][key] = {}

# create perceptron combos
for c1 in string.ascii_lowercase:
		for c2 in string.ascii_lowercase:
			if c1 != c2:
				if c2+c1 not in perceptrons:
					#perceptrons[c1+c2] = "{\"w0\":0.1,\"w1\":0.2,\"w3\":0.3}"
					perceptrons[c1+c2] = perceptron()


#print perceptrons
# print perceptrons['ab']
# count = len(perceptrons)
# print count
# if count == 325:
# 	print "yay!"

# print line debugging!
print perceptrons['ab'].weights
print perceptrons['yz'].bias

for (i, letters_list_training) in enumerate(letters_list_training):
	print letters_list_training[i].value
	if letters_list_training[i].value == 'Y': #or ['Z']:
		perceptron.train(perceptrons['yz'], letters_list_training[i].attributes)



# scheme for dictionary of dictionaries {char : {char : perceptron}}
# perceptrons = {}
# for key in dict.iterkeys():
#     perceptrons[key] = {}
#     for key in dict.iterkeys():
#         perceptrons[key][key] = {}
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



