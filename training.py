#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16
import string
from perceptron import perceptron
import letter
from input import letters_list_training

eta = 0.2  # eta is 0.2 for training perceptrons

###    print letters_list_training[i].value
###    print letters_list_training[i].attributes

# scheme for dictionary of dictionaries {char+char : perceptron instance}
perceptrons = {}
# for key in dict.iterkeys():
# perceptrons[key] = {}
# for key in dict.iterkeys():
# perceptrons[key][key] = {}

# create perceptron combos
for letter1 in string.ascii_uppercase:
    for letter2 in string.ascii_uppercase:
        if letter1 != letter2:
            if letter2 + letter1 not in perceptrons:
                # perceptrons[i+j] = {w0":0.1,"w1":0.2,"w3":0.3}
                perceptrons[letter1 + letter2] = perceptron()

#print perceptrons
#print perceptrons['AB']
# count = len(perceptrons)
# print count
# if count == 325:
# 	print "yay!"

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

#for i in range (1, len(perceptrons)):
for k, v in perceptrons: #k, v are the two letters in the perceptron representation
    #print k, v
    # for k in letters_list_training:
    #     for v in letters_list_training:
    #         if k != v:
    for letter in letters_list_training:
        if k in letter.value: #or v in letter.value:
            perceptron.train(perceptrons[k+v], letter.attributes, 1.0)
            #perceptron.test(perceptrons[k+v], letter.attributes)
        if v in letter.value:
            perceptron.train(perceptrons[k+v], letter.attributes, -1.0)




#if letter1 != letter2:
    # for letter1 in perceptrons[letter1 + letter2]:
    #     for letter2 in perceptrons[letter1 + letter2]:
    #         print letter1+letter2
    #         for letter in letters_list_training:
    #             if letter1 in letter.value or letter2 in letter.value:
    #                 perceptron.train(perceptrons[letter1 + letter2], letter.attributes, 1.0)
    #                 perceptron.test(perceptrons[letter1 + letter2], letter.attributes)


# for letter in letters_list_training: print letter.value
####for letter in letters_list_training:
###    print type(letter.attributes) is list
###    print [float(i) for i in letter.attributes]
#####if 'A' in letter.value or 'Z' in letter.value:


####perceptron.train(perceptrons['AZ'], letter.attributes, 1.0)
### for i in range(len(letter.attributes)):
###    print letter.attributes[i]
####perceptron.test(perceptrons['AZ'], letter.attributes)
        #print letter.attributes
        #print letter.value
        #print "match"



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
