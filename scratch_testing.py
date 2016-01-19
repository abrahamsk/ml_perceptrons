#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16

import string
from perceptron import perceptron
import letter
from scratch_training import perceptrons_sublist, letters_list_training
from input import letters_list_testing
from pandas_confusion import ConfusionMatrix
import pprint
import random

# track correct and incorrect output from perceptron
# correct_output is incremented when perceptron correctly
# classifies a letter input
# incorrect_output is incremented when perceptron incorrectly
# classifies letter input
correct_test_output = 0.0
incorrect_test_output = 0.0
accuracy = 0.0
# set up confusion matrix
y_actu = []
y_pred = []
# dictionary for votes for letters (all alphabet letters valued at 0 to count votes)
intermed_votes = {c:i for i, c in enumerate(string.ascii_uppercase, 1)}
#print intermed_votes
votes = dict.fromkeys(intermed_votes.iterkeys(), 0)

# convert list of letters to tuple to use as dictionary key
###letters_tup_testing = tuple(letters_list_testing)

print "***Testing***"

# run all data instances through trained perceptrons
# to test accuracy
# for k, v in perceptrons: #k, v are the two letters in the perceptron representation (perceptron[kv])
#     for letter in letters_list_testing:
#         output = perceptron.test(perceptrons[k+v], letter.attributes)
#         if output == True:
#             #print "true loop: output: ", output
#             #print "correct: ", "k: ", k, "v: ", v
#             correct_test_output = correct_test_output + 1 # increment correct counter if input matches target
#             y_pred.append(k)
#             y_actu.append(k)
#         else:
#             #print letter.value
#             #print "else: output: ", output
#             #print "incorrect: ", "k: ", k, "v: ", v
#             incorrect_test_output = incorrect_test_output + 1
#             y_pred.append(k)
#             y_actu.append(v)

# dictionary of tuples to record actual letter and perceptron result letter
letter_and_guess = []

# for every letter, run through every perceptron
# and record votes for which letter perceptron returns
# shuffle letters
random.shuffle(letters_list_testing)
for letter in letters_list_testing:
    #print letter.value[0]
    actual_letter = str(letter.value[0])
    print "actual letter:", actual_letter
    for m, n in perceptrons_sublist:
        print m, n
        # # set targets for letters
        # if m in letter.value:
        #     # match letter m to target 1
        #     letter.target = 1
        # if n in letter.value:
        #     # match letter n to target -1
        #     letter.target = -1

        # actual_letter = str(letter.value[0])
        # print "actual letter:", actual_letter
        output = perceptrons_sublist[m+n].test(letter.attributes)
        if output == True: # perceptron outputs letter m
            ###pprint.pprint(votes)
            ###pprint.pprint(actual_letter)
            votes[m] += 1
            print "vote for", m
            # add to letter and guess tuple with actual letter and guessed letter
            letter_and_guess.append((actual_letter, m))
        else:
            votes[n] += 1
            print "vote for", n
            # add to letter and guess tuple with actual letter and guessed letter
            letter_and_guess.append((actual_letter, n))
        # tally votes for letter guesses (get max of votes)

        # break ties if more than one letter has equal votes

    # print letter_and_guess
    print votes
    # find the letter with the most votes
    #selected_letter = max(votes, key=lambda i: votes[i])
    # find max values in votes to break tie
    max_value = max(votes.values())
    letter_winner_candidates = [key for key in votes if votes[key] == max_value]
    print "candidates for selected letter:", letter_winner_candidates
    # break ties at random, seed random number with number of keys
    # that have votes matching the max number of votes
    print len(letter_winner_candidates)
    tie_breaker = (random.randint(0, 1000) % len(letter_winner_candidates))
    print "tie breaker index:", tie_breaker
    selected_letter = letter_winner_candidates[tie_breaker]
    print "Winning letter by vote:", selected_letter
    # append to confusion matrix
    y_pred.append(selected_letter)
    y_actu.append(actual_letter)

    # accuracy is the number of correct votes/total votes
    # accuracy = (# correct) / (all points in conf. matrix, including correct)
    # diagonal of matrix / total

# *********************
# print "correct ", correct_test_output
# print "incorrect ", incorrect_test_output
# total = correct_test_output + incorrect_test_output
# print "total: ", total
# accuracy = correct_test_output/total
# print "accuracy: ", accuracy

# create confusion matrix to describe performance
# of perceptron learning algorithm
# using pandas library
##y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
##y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
# confusion_matrix(y_pred, y_actu)
# print confusion_matrix(y_pred, y_actu)

# make confusion matrix out
cm = ConfusionMatrix(y_actu, y_pred)
print("Confusion matrix:\n%s" % cm)
cm.print_stats()

