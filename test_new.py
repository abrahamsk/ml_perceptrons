#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16

import string
from perceptron import perceptron
import letter, random, sys
from train_new import perceptrons
from input import letters_list_testing
from pandas_confusion import ConfusionMatrix

#-----------
# functions
#----------
def collect_votes(instance):
    # dict for collecting votes from perceptron
    perceptron_vote = {}
    # collect votes by running instance through all perceptrons
    for m, n in perceptrons:
        # convert votes from numbers output from perceptron to alpha
        vote_alpha = ""
        #test perceptron for correct output
        vote = perceptrons[m+n].test_instance(instance.attributes)
        if vote == -1:
            # perceptron output -1 means a vote for p_id[0] (= m)
            vote_alpha = m
        else:
            vote_alpha = n

        # record vote from perceptron
        if perceptron_vote.has_key(vote_alpha):
            perceptron_vote[vote_alpha] += 1
        # make key exist if it doesn't yet
        else:
            perceptron_vote[vote_alpha] = 1

    # get max vote for instance after run through all perceptrons
    max_value = max(perceptron_vote.values())
    letter_winner_candidates = [key for key in perceptron_vote if perceptron_vote[key] == max_value]
    # break ties at random, seed random number with number of keys
    # that have votes matching the max number of votes
    tie_breaker = (random.randint(0, 1000) % len(letter_winner_candidates))
    selected_letter = letter_winner_candidates[tie_breaker]
    #print "Winning letter by vote:", selected_letter
    return selected_letter


    #
    # max_value = max(votes.values())
    # letter_winner_candidates = [key for key in votes if votes[key] == max_value]
    # ###print "candidates for selected letter:", letter_winner_candidates
    # # break ties at random, seed random number with number of keys
    # # that have votes matching the max number of votes
    # ###print len(letter_winner_candidates)
    # tie_breaker = (random.randint(0, 1000) % len(letter_winner_candidates))
    # ###print "tie breaker index:", tie_breaker
    # selected_letter = letter_winner_candidates[tie_breaker]
    # print "Winning letter by vote:", selected_letter
    # # append to confusion matrix
    # y_pred.append(selected_letter)
    # y_actu.append(actual_letter)
    #

#read in trained data to perceptrons for testing

# # set up confusion matrix
y_actu = []
y_pred = []

#-----
# main
#-----
# for every letter, run through every perceptron
# and record votes for which letter perceptron returns
letter_increment = 0

for letter in letters_list_testing:
    text = "\rTraining letter "+str(letter_increment)+"/"+str(len(letters_list_testing))
    sys.stdout.write(text)
    letter_increment += 1

    # collect votes to build confusion matrix
    predicted = collect_votes(letter)
    #print letter.value[0], predicted

    # append to confusion matrix
    y_pred.append(predicted)
    y_actu.append(letter.value[0])

# make confusion matrix out
cm = ConfusionMatrix(y_actu, y_pred)
###print("Confusion matrix:\n%s" % cm)
cm.print_stats()

