#!/usr/local/bin/python3

import string

path = "./Walden.txt"
with open(path,'r') as text:
	# Remove punctuations, and all words to lower capital
	words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
	# Create a set, it will remove all replicate words
	words_index = set(words)
	# Create a dictionary, word is key, count is value
	counts_dict = {index:words.count(index) for index in words_index}

	for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
		print('{} - {} times'.format(word,counts_dict[word]))
