# epochs = 5
#
# for i in range(0, epochs):
#     print i
#
# for i in range(0, epochs):
#     print "Epoch", i, "begins! "

# import string
#
# votes = {c:i for i, c in enumerate(string.ascii_uppercase, 1)}
# votes = dict.fromkeys(votes.iterkeys(), 0)
# print votes['A']

import random
from input import letters_list_training

# print letters_list_training
random.shuffle(letters_list_training)
print letters_list_training
for letter in letters_list_training:
    print letter.value[0]