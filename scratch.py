# epochs = 5
#
# for i in range(0, epochs):
#     print i
#
# for i in range(0, epochs):
#     print "Epoch", i, "begins! "

import string
#
# votes = {c:i for i, c in enumerate(string.ascii_uppercase, 1)}
# votes = dict.fromkeys(votes.iterkeys(), 0)
# print votes['A']

# import random
from input import letters_list_training
#
# # print letters_list_training
# random.shuffle(letters_list_training)
# print letters_list_training
# for letter in letters_list_training:
#     print letter.value[0]

epochs = 5 # start with 5, work up to 30
# for i in range(0, epochs):
#     print "\nEpoch", i, "begins"
#     for letter in letters_list_training:
#          print letter.value
#     print "\nEpoch", i, "ends"
#
# for i in range(0, epochs):
#     print "\nEpoch", i, "begins"
#     print "i: ", i
#     print "Epoch", i, "ends"

# count = 0
# accuracy = 0
# print "count before loop: ", count
# for i in range(0, epochs):
#     print "\nEpoch", i, "begins"
#     print "accuracy before reset: ", accuracy
#     accuracy = 0
#     print "accuracy after reset: ", accuracy
#     print "i: ", i
#     # for letter in letters_list_training:
#     #     print letter.value
#     #     count += 1
#     #     print "count in loop: ", count
#     for letter1 in string.ascii_uppercase:
#         print letter1
#         count += 1
#     accuracy += 1
#     print "accuracy at end: ", accuracy
#     print "Epoch", i, "ends"
#
# print "count after loops: ", count

# # dictionary for votes for letters (all alphabet letters valued at 0 to count votes)
# intermed_votes = {c:i for i, c in enumerate(string.ascii_uppercase, 1)}
# #print intermed_votes
# votes = dict.fromkeys(intermed_votes.iterkeys(), 0)
#
# letter = 'A'
#
# print votes[letter]

# import random#
# print random.randint(0, 1000)

from input import letters_list_testing
from scratch_training import perceptrons_sublist

count_loops = 0

# for letter in letters_list_testing:
#     #print letter.value[0]
#     actual_letter = str(letter.value[0])
#     print "actual letter:", actual_letter
#     for m, n in perceptrons_sublist:
#         print m, n
#         count_loops += 1
#
#     print count_loops
#
# for m, n in perceptrons_sublist:
#     print m, n
#     count_loops += 1
#     print count_loops
#
# print count_loops


# #!/usr/bin/env python
#
# # Machine Learning 445
# # HW 1: Perceptrons
# # Katie Abrahams, abrahake@pdx.edu
# # 1/19/16
#
# import string
# from perceptron import perceptron
# import letter
# from input import letters_list_training
# import random
# import numpy as np
# from itertools import islice
#
# eta = 0.2  # learning rate is 0.2 for training perceptrons
# epochs = 4 # number of training epochs
#
# ###    print letters_list_training[i].value
# ###    print letters_list_training[i].attributes
#
# # create a dictionary of perceptrons
# # such that all different letter combinations are represented
# # perceptrons = {}
# # for letter1 in string.ascii_uppercase:
# #     for letter2 in string.ascii_uppercase:
# #         if letter1 != letter2:
# #             if letter2 + letter1 not in perceptrons:
# #                 letters_combined = letter1 + letter2
# #                 perceptrons[letters_combined] = perceptron()
#
# # sublist of letters for testing
# perceptrons_sublist = {}
# for letter1 in string.ascii_uppercase[0:5]:
#     for letter2 in string.ascii_uppercase[0:5]:
#         if letter1 != letter2:
#             if letter2 + letter1 not in perceptrons_sublist:
#                 letters_combined = letter1 + letter2
#                 perceptrons_sublist[letters_combined] = perceptron()
#
# print "perceptron sublist"
# for m, n in perceptrons_sublist:
#     print m, n
#
# # for g, h in perceptrons_sublist:
# #     print perceptrons_sublist[g+h].bias
#
# correct_output = 0.0
# incorrect_output = 0.0
# # at the end of an epoch, test accuracy of perceptron
# # and revert to old weights using perceptron class method if
# # accuracy has gotten worse
# accuracy = 0.0
# accuracy_prev = 0.0
#
# # loop through dictionary of perceptron instances
# # and train perceptron for matching input
# # e.g. perceptron[AB] gets all A and all B training instances
# # from the training data
# #for i in range (1, len(perceptrons)):
# print "***Training***"
#
# # shuffle letters
# random.shuffle(letters_list_training)
# # for letter in letters_list_training:
# #     print letter.value[0]
#
# # get a slice of the perceptrons dictionary to test training algorithm
# # perceptrons_sublist = take(5, perceptrons.iteritems())
# # for g, h in perceptrons_sublist:
# #     print "sublist weights", perceptrons_sublist[g+h].weights
#
# perceptron_increment = 1
# for m, n in perceptrons_sublist: #m, n are the two letters in the perceptron representation (perceptron[kv])
#     print m, n
#
#     print "Training perceptron",perceptron_increment,"/", len(perceptrons_sublist)
#     perceptron_increment += 1
#     # collect matching letters m,n to train perceptron[mn]
#     matching_letters = []
#     for letter in letters_list_training:
#         if m in letter.value:
#             matching_letters.append(letter)
#             # for letter in matching_letters:
#             #     print letter.value
#             #     print letter.attributes
#             # set letter m to target 1
#             letter.target = 1
#         if n in letter.value:
#             matching_letters.append(letter)
#             # set letter n to target -1
#             letter.target = -1
#     # shuffle list of inputs
#     random.shuffle(matching_letters)
#     # for letter in matching_letters:
#     #     print letter.value
#     #     print letter.attributes
#     #     print letter.target
#
#     # preserve weights to revert if necessary
#     # saved_bias = np.array([])
#     # saved_weights = np.array([])
#     saved_bias = np.array(perceptrons_sublist[m+n].bias)
#     # print saved_bias == np.array(perceptrons[m+n].bias)[0]
#     # print np.array(perceptrons[m+n].bias)[0]
#     #print saved_bias is np.array(perceptrons[m+n].bias)
#
#     # try:
#     #     saved_weights
#     # except NameError:
#     #     saved_weights = np.array([])
#     saved_weights = np.array([])
#     for i in range(0, len(np.array(perceptrons_sublist[m+n].weights))):
#         saved_weights = np.append(saved_weights, np.array(perceptrons_sublist[m+n].weights)[i])
#         # saved_weights.append(np.array(perceptrons[m+n].weights)[i])
#     print "Saved bias and weights: "
#     print saved_bias
#     print saved_weights
#
#     for j in range(0, epochs):
#         # Start epoch
#         # Steps in epoch:
#         #   1. Test initial accuracy (preserve weights)
#         #   2. Train perceptrons (alter weights)
#         #   3. End of epoch: test accuracy
#         #       - Revert weights if accuracy goes down
#         #       - Break if accuracy has not improved
#
#         saved_bias = np.array(perceptrons_sublist[m+n].bias)
#         saved_weights = np.array([])
#         for i in range(0, len(np.array(perceptrons_sublist[m+n].weights))):
#             saved_weights = np.append(saved_weights, np.array(perceptrons_sublist[m+n].weights)[i])
#         print "Saved bias and weights in loop: "
#         print saved_bias
#         print saved_weights
#         # 1) Test accuracy of perceptron[mn] for the matching letters [m] or [n]
#         # test_accuracy runs perceptron.test() function for all matching letter instances
#         # num_accurate = perceptron.test_accuracy(perceptrons[m+n], matching_letters)
#         num_accurate = perceptrons_sublist[m+n].test_accuracy(matching_letters)
#         print "\nStart of epoch", j
#         print "num accurate:", num_accurate
#
#         # 2) Train perceptron
#         for letter in matching_letters[0:5]:
#             # output = perceptron.test(perceptrons[m+n], letter.attributes)
#             output = perceptrons_sublist[m+n].test(letter.attributes)
#             # if perceptron doesn't return the expect output,
#             # run training on perceptron to modify the weights
#             if output != letter.target:
#                 print "output of perceptron test of", letter.value[0], "doesn't match target, train perceptron"
#                 # perceptron.train(perceptrons[m+n], letter.attributes, letter.target)
#                 perceptrons_sublist[m+n].train(letter.attributes, letter.target)
#             if output == letter.target:
#                 print "output of perceptron test of", letter.value[0], "equals target, skip training"
#
#
#         # 3) Test accuracy after weights have been updated
#         # After weights have been updated, test accuracy of perceptron again
#         # Revert weights if need be
#         # num_accurate_revised = perceptron.test_accuracy(perceptrons[m+n], matching_letters)
#         num_accurate_revised = perceptrons_sublist[m+n].test_accuracy(matching_letters)
#         print "End of epoch, num accurate: ", num_accurate_revised
#
#         # revert weights if accuracy has worsened
#         if(num_accurate_revised < num_accurate):
#             print "Accuracy worse, revert weights"
#             # perceptron.revert_weights(perceptrons[m+n], saved_bias, saved_weights)
#             perceptrons_sublist[m+n].revert_weights(saved_bias, saved_weights)
#
#         # stop training if accuracy stops improving
#         if (num_accurate_revised == num_accurate):
#             if epochs != 0:
#                 print "No accuracy improvement, stopping training"
#                 break
#
#         # set accuracy to revised accuracy computed for this instance
#         # for next epoch
#         num_accurate = num_accurate_revised


from perceptron import perceptron
from letter import letter

def trainPtron(ptron_id):
    # runs a ptron through epoch's until there is no improvement in accuracy between epoch's
    epochPosChange = True
    while epochPosChange:
        epochPosChange = runEpoch(ptron_id)


def runEpoch(ptron_id):
    # if ptron isn't 100% accurate, adjust weights, if new weights are more accurate commit change and return True
    accuracyOne = getAccuracy(ptron_id, perceptrons[ptron_id]) # let's see where we are at

    if accuracyOne < 1: # only adjust weights if not perfect already
        adjustedPtron = adjustWeights(ptron_id) # give me a better one
        accuracyTwo = getAccuracy(ptron_id, adjustedPtron) # how are we now?
        if accuracyTwo > accuracyOne: # there is improvement, commit change
            perceptrons[ptron_id].update(adjustedPtron)
            return True
    else: # adjustment not needed
        return False

def getAccuracy(ptron_id, ptron):
    # tests one ptron with all matching featureVectors in the training list
    correct = float(0)
    total = float(0)
    decision = str

    for featureVector in trainingSet:
        target = featureVector[0].lower()

        if target in str(ptron_id): # decides if a trainingVector is right for this ptron
            decision = signumToAlpha(ptron_id, testFeatureVector(ptron, featureVector))

            total += 1 # increment the total for this featureVector
            if  decision == target: # ptron decided correctly
                correct += 1 # increment correct counter
    # incase there were no training examples for this prton. Mainly durning dev.
    if total > 0: return float(correct)/float(total)
    else: return 0.0
############################



