import json
from collections import OrderedDict
import nltk
from nltk.collocations import *
from nltk import word_tokenize
from textblob import TextBlob
import matplotlib.pyplot as plt

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

nltk.download('punkt')

newfile = "tweetdata2.json"
afile = open("twittersentences.txt")
raw = afile.read()
tweets = set()
word_dct = {}
hashtags = {}
sentences = {}
sentence_polarity = {}
graph_values = {}
graph_dict = {}
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

def return_text():
	count = 0
	blob = TextBlob(raw)
	for sentence in blob.sentences:
		sentence_polarity[sentence] = sentence.sentiment.polarity
		graph_values[count] = sentence.sentiment.polarity
		count = count + 1
	print(sentence_polarity)
	return graph_values

#Creates rough features of attribution to the Autism disorder
def grab_personal_pronoun_sentences(sentences):
	personal_sentences = {}
	supporters = []
	represented = []
	indifferent = []
	support = "support"
	rep= "represented"
	indiff= "indifferent"
	for key in sentences:
		if "son" or "daughter" in key:
			supporters.append(key)
		elif "I have" or "my" in key:
			represented.append(key)
		else:
			indifferent.append(key)
	personal_sentences[support] = supporters
	personal_sentences[rep] = represented
	personal_sentences[indiff] = indifferent

z = grab_personal_pronoun_sentences(sentences)
print(z)

return_text()
graph_dict = return_text()
lists = sorted(graph_dict.items()) # sorted by key, return a list of tuples
x, y = zip(*lists) # unpack a list of pairs into two tuples
plt.scatter(x, y)
plt.suptitle("Sentence Polarity",fontsize=28)
plt.xlabel("Sentences", fontsize=24)
plt.ylabel("Polarity",fontsize=24)
plt.show()

plt.scatter(x,ys	# # x = data_dict.keys()
	# y = data_dict.values()
	plt.xlabel("Sentences", fontsize=24)
	ply.ylabel("Polarity",fontsize=24)
	
plt.legend(graph_dict.keys())
plt.show()
for s in tweets:
	print(s)
finder = BigramCollocationFinder.from_words(word_tokenize(raw))
finder2 = TrigramCollocationFinder.from_words(word_tokenize(raw))

#Report all tri-grams that show up 60 times or more
finder.apply_freq_filter(60)
#Report all bi-grams that show up 60 or more times
finder2.apply_freq_filter(60)

# return the 45 n-grams with the highest PMI
print(finder.nbest(bigram_measures.pmi, 45))

# return the 45 n-grams with the highest PMI
print(finder2.nbest(trigram_measures.pmi, 45))

# MaxEntClassifier = nltk.classify.maxent.MaxentClassifier.train(word_dct, 'GIS', trace=3, \
# #                     encoding=None, labels=None, sparse=True, gaussian_prior_sigma=0, max_iter = 10)

# for key in word_dct.keys():
# 	print MaxentClassifier.classify(key)