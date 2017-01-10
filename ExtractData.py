import nltk
import json
from nltk.collocations import *
from collections import OrderedDict
from nltk.corpus import brown
import matplotlib.pyplot as plt

newfile = "tweetdata2.json"
sentenceFile = "twittersentences.txt"
tweets = set()
word_dct = {}
sentences = {}
hashtags = {}
# Load in data as JSON and store into a temporary dct for analytics work
def upload_data(file):
	data_set = set()
	with open(file) as f:
		for line in f.readlines():
			try:
				tweet = load_json_from_line(line)
				data_set.add(str(tweet))
			except ValueError, KeyError:
				continue
	return data_set

#Load the tweet text data line by line from the json decoder
def load_json_from_line(line):
	data = json.loads(line)
	if "text" in data:
		tweet = data["text"]
	if "text" not in data:
		tweet = ""
	return tweet

#Create a crude dictionary of words from the dataset
def create_word_dictionary(tweets):
	dct = {}
	hashtags = {}
	for s in tweets:
		s = s.lower()
		for word in s.split():
			if word not in dct:
				dct[word] = 0
			dct[word] += 1
	return OrderedDict(sorted(dct.items(), key=lambda x: x[1]))

#Parse the word dictionary and create and independent dictionary of hashtags.
def prune_for_hashtags(word_dct):
	hashtags = {}
	for key in word_dct.keys():
		if '#' in key:
			print(key)
			hashtags[key] = word_dct[key]
	return hashtags

#Prune the word dictionary of known hashtags
def prune_word_dict(word_dct):
	for key in word_dct.keys():
		try:
			if '#' in key:
				del word_dct[key]
			if '@' in key:
				del word_dct[key]
			if 'http' in key:
				del word_dct[key]
		except KeyError:
			continue
	return word_dct

def graph_causes(word_dct):
	causes = [1,2]
	labels = ['vaccine', 'mitochondrial']
	y = [93, 265]
	width = 1/1.5
	plt.bar(causes, y, width, align="center")
	plt.xticks(causes, labels, fontsize=20)
	plt.suptitle("Suggested Causes",fontsize=28)
	plt.xlabel("Causes", fontsize=24)
	plt.ylabel("Occurrences",fontsize=24)
	plt.show()

tweets = upload_data(newfile)
word_dct = create_word_dictionary(tweets)
print(word_dct)

print(len(tweets))
print(sum(prune_word_dict(word_dct).values()))
dct = {}
dct = prune_for_hashtags(word_dct)
print(dct)
print(hashtags)
print(sum(hashtags.values()))
graph_causes(word_dct)
# print(prune_word_dict(word_dct))

