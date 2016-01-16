#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16

import string
from perceptron import perceptron
import letter
from input import letters_list_training

# get stats for perceptron run
def get_stats(correct_output, incorrect_output, accuracy, accuracy_prev):
    print "correct: ", correct_output
    print "incorrect: ", incorrect_output
    total = correct_output + incorrect_output
    print "total: ", total

    print "accuracy before comparison ", accuracy
    print "prev accuracy before comparison ", accuracy_prev

    return total


eta = 0.2  # learning rate is 0.2 for training perceptrons
epochs = 5 # start with 5, work up to 30

###    print letters_list_training[i].value
###    print letters_list_training[i].attributes

# create a dictionary of perceptrons
# such that all different letter combinations are represented
perceptrons = {}
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

# track correct and incorrect output from perceptron
# correct_output is incremented when perceptron correctly
# classifies a letter input
# incorrect_output is incremented when perceptron incorrectly
# classifies letter input
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
for k, v in perceptrons: #k, v are the two letters in the perceptron representation (perceptron[kv])
    # reset values for counts
    correct_output = 0.0
    incorrect_output = 0.0
    for i in range(0, epochs):
        print "\nEpoch", i, "begins! "
        total = 0.0
        print k, v
        # for k in letters_list_training:
        #     for v in letters_list_training:
        #         if k != v:
        for letter in letters_list_training:
            #print letter.value
            if k in letter.value:
                # train perceptrons that contain the letter matching k in perceptron[kv]
                # set t = 1 for input i in perceptron[ij]
     ####           output = perceptron.train(perceptrons[k+v], letter.attributes, 1.0)
                output = perceptron.test(perceptrons[k+v], letter.attributes)
                #perceptron.test(perceptrons[k+v], letter.attributes)
                # if perceptron output is true, sgn((dot product(w,x))) is positive
                if output == True:
                    correct_output = correct_output + 1 # increment correct counter if input matches target
    #                print "+ Input k: ", k, " from perceptron ", k,v, " result: ", k
                else:
                    incorrect_output = incorrect_output + 1
                    perceptron.train(perceptrons[k+v], letter.attributes, 1.0)
                    # mark that y neq t, so that weights can be adjusted
                    ####perceptron.set_incorrect_result(perceptrons[k+v])
                    # revert weights
                    ####perceptron.revert_weights(perceptrons[k+v])
    #                print "- Input k: ", k, " from perceptron ", k,v, " result: ", v
            # train perceptrons that contain the letter matching v in perceptron[kv]
            # set t = -1 for input j in perceptron[ij]
            if v in letter.value:
    ####            output = perceptron.train(perceptrons[k+v], letter.attributes, -1.0)
                output = perceptron.test(perceptrons[k+v], letter.attributes)
                #perceptron.test(perceptrons[k+v], letter.attributes)
                if output == True:
                    correct_output = correct_output + 1 # increment correct counter if input matches target
    #                print ">>> + Input v: ", v, " from perceptron ", k,v, " result: ", v
                else:
                    incorrect_output = incorrect_output + 1
                    perceptron.train(perceptrons[k+v], letter.attributes, 1.0)
                    ####perceptron.set_incorrect_result(perceptrons[k+v])
                    # revert weights
                    ####perceptron.revert_weights(perceptrons[k+v])
    #                print ">>> - Input v: ", v, " from perceptron ", k,v, " result: ", k
    #get_stats(correct_output, incorrect_output, accuracy, accuracy_prev)
    print "correct: ", correct_output
    print "incorrect: ", incorrect_output
    total = correct_output + incorrect_output
    print "total: ", total

    print "accuracy before comparison ", accuracy
    print "prev accuracy before comparison ", accuracy_prev

     # revert weights if accuracy has gotten worse
    if(accuracy < accuracy_prev):
        perceptron.revert_weights(perceptrons[k+v])
        # for k in perceptrons:
        #     if (perceptron.check_result(perceptrons[k])) == False:
        #         perceptron.revert_weights(perceptrons[k])

    accuracy_prev = accuracy # store previous accuracy for comparison (initialized to 0 at training start)
    print "previous accuracy: ", accuracy_prev
    accuracy = correct_output/total
    print "accuracy: ", accuracy

    # stop training if accuracy stops improving
    if (accuracy == accuracy_prev):
        print "no accuracy improvement"
        break





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