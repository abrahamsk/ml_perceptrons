###input.py
from perceptron import perceptron
import string

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
print perceptrons['ab']
count = len(perceptrons)
print count
if count == 325:
	print "yay!"
