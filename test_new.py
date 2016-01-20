#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16

import letter, random, sys
from train_new import perceptrons
from input import letters_list_testing
from pandas_confusion import ConfusionMatrix
import pandas as pd
pd.set_option('max_rows',500) and pd.set_option('max_columns',500)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

######################
# function definitions
######################
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
    # get max from vote tallies
    max_value = max(perceptron_vote.values())
    # get key (letter name) from dictionary where the number of votes
    # for that letter equals the max number of votes
    letter_winner_candidates = [key for key in perceptron_vote if perceptron_vote[key] == max_value]
    # break ties at random, seed random number with number of keys
    # that have votes matching the max number of votes
    tie_breaker = (random.randint(0, 1000) % len(letter_winner_candidates))
    selected_letter = letter_winner_candidates[tie_breaker]
    #print "Winning letter by vote:", selected_letter
    return selected_letter

#################
# data structures
#################

# set up confusion matrix rows and columns
# list for pandas_confusion confusion matrix stats
y_actu_stats = []
y_pred_stats = []

# series for using pandas confusion matrix
y_actu = pd.Series([], name='Actual')
y_pred = pd.Series([], name='Predicted')

#######
# main
#######
# counter for letters that have been run through perceptrons
letter_increment = 0
# for every letter, run through every perceptron
# and record votes for which letter perceptron returns
for letter in letters_list_testing:
    # text = "\rTesting instance "+str((letter_increment)+1)+"/"+str(len(letters_list_testing))
    # sys.stdout.write(text)

    # collect perceptron votes to build confusion matrix
    # collect_votes runs perceptron for instances of letters in the testing data set
    # returns the winning letter by vote to store into predicted
    predicted = collect_votes(letter)
    #print letter.value[0], predicted

    # append to confusion matrix using pandas
    y_pred = y_pred.append(pd.Series(predicted, index=[letter_increment]))
    y_actu = y_actu.append(pd.Series(letter.value[0], index=[letter_increment]))

    # append pandas_confusion
    y_pred_stats.append(predicted)
    y_actu_stats.append(letter.value[0])

    # increment counter for next letter
    letter_increment += 1

# make confusion matrix using pandas
df_confusion = pd.crosstab(y_actu, y_pred, rownames=['Actual'], colnames=['Predicted'], margins=True)
print df_confusion

# make confusion matrix and print stats using pandas_confusion
cm = ConfusionMatrix(y_actu_stats, y_pred_stats)
# print("Confusion matrix:\n%s" % cm)
cm.print_stats()