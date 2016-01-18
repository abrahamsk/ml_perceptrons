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

count = 0
accuracy = 0
print "count before loop: ", count
for i in range(0, epochs):
    print "\nEpoch", i, "begins"
    print "accuracy before reset: ", accuracy
    accuracy = 0
    print "accuracy after reset: ", accuracy
    print "i: ", i
    # for letter in letters_list_training:
    #     print letter.value
    #     count += 1
    #     print "count in loop: ", count
    for letter1 in string.ascii_uppercase:
        print letter1
        count += 1
    accuracy += 1
    print "accuracy at end: ", accuracy
    print "Epoch", i, "ends"

print "count after loops: ", count