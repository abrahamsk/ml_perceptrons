# epochs = 5
#
# for i in range(0, epochs):
#     print i
#
# for i in range(0, epochs):
#     print "Epoch", i, "begins! "

import string

votes = {c:i for i, c in enumerate(string.ascii_uppercase, 1)}
votes = dict.fromkeys(votes.iterkeys(), 0)
print votes['A']