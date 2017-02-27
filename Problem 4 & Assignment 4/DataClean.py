# -*- coding: utf-8 -*-
# Data cleaning for text mining.
import re
from P_S_algo import PorterStemmer
from math import log
from utility import *

def dataclean(sample, stopword):
	fobj = open(sample)
	data = fobj.read().split('\n\n')
	fobj.close()
	Name = []
	Biography = []

	# Get the rough name and corresponding biography
	for i in data:
		Name.append(re.search(r'\n?(.)*(?=\n|.)',i).group())
		Biography.append(re.sub(r'^\n*.*\n','',i)) #
	Name_update = []

	# Clean name
	for i in Name:
		Name_update.append(re.sub(r'(?<=\w)[\s\n]+$','',i))
	Name_update1 = []
	for i in Name_update:
		Name_update1.append(re.sub(r'^[\n\s]+(?=\w)','',i))

	# Clean biography
	Biography_update = []
	for i in Biography:
		Biography_update.append(re.findall(r'[^\W\d]+', i))

	# Convert to lower case
	Biography_update2 = []
	for i in Biography_update:
		Biography_update2.append(map(lambda x:x.lower(), i))

	# Discard all stop words and all words of fewer than 3 characters
	fobj = open(stopword)
	stopword = re.findall(r'[^\W\d]+', fobj.read())
	Biography_update3 = []
	for i in Biography_update2:
		a = []
		for j in i:
			if j not in stopword and len(j)>=3:
				a.append(j)
		Biography_update3.append(a)

	# Discard the words which appear half of the texts or only appears once (I think it
	# may be helpful). 
	# Choose the word which meet the requirement
	term = {}
	for i in Biography_update3:
		for j in set(i):
			term.setdefault(j,0)
			term[j] += 1
	half = len(Name)/float(2)
	for key in term.keys():
		if term[key] > half or term[key] == 1:
			term.pop(key)
	Biography_update4 = [[j for j in i if j in term.keys()] for i in Biography_update3]

	# Stem
	p = PorterStemmer()
	Biography_update5 = [[p.stem(j,0,len(j) - 1) for j in i] for i in Biography_update4]
	return Name_update1,Biography_update5

def matrix_construct(Biography, method = "frequency"):
	# Get the whole words
	if method == "TFIDF":
		whole = []
		term = {}
		for i in Biography:
			whole += i
			for j in set(i):
				term.setdefault(j,0)
				term[j] += 1
		total = len(Biography)
		for k in term.keys():
			term[k] = 1 + log(total/float(term[k]))
		whole = list(set(whole))

		# Generate the matrix by using TFIDF 
		# (Data Science for Bussiness written by Foster Provost & Tom Fawcett)
		matrix = [[0 for i in xrange(len(whole))] for j in xrange(len(Biography))]
		for i in xrange(len(Biography)):
			word = {}
			for j in xrange(len(Biography[i])):
				word.setdefault(Biography[i][j],0)
				word[Biography[i][j]] += 1
			for k in word.keys():
				matrix[i][whole.index(k)] = word[k]*term[k]
	elif method == "frequency":
		whole = []
		for i in Biography:
			whole += i
		whole = list(set(whole))
		matrix = [[0 for i in xrange(len(whole))] for j in xrange(len(Biography))]
		for i in xrange(len(Biography)):
			for j in Biography[i]:
				matrix[i][whole.index(j)] += 1
	return matrix, whole

def Group(bestmatches, matrix, whole, Name, output):
	group = {}
	for i in bestmatches:
		if len(i) > 0:
			avgs = [np.mean([matrix[j][l] for j in i]) for l in xrange(len(matrix[0]))]
			avgs = list(enumerate(avgs))
			avgs.sort(key=lambda x:x[1], reverse=True)
			freqword =(whole[avgs[0][0]], whole[avgs[1][0]])
			Name_G = []
			for j in i:
				Name_G += [Name[j]]
			group.setdefault(freqword,Name_G)
	with open(output,'w+') as f:
		for name in group.keys():
			f.write('%s %s: ' % (name[0], name[1]))
			for member in group[name]:
				if group[name].index(member) < len(group[name])-1:
					f.write('%s, ' % member)
				else:
					f.write('%s\n' % member)

if __name__ == '__main__':
	Name, Biography = dataclean("Sample.txt","stopwords2.txt")
	matrix, whole = matrix_construct(Biography, "frequency")
	bestmatches = kmeans(matrix, 100, cosine, 4)
	Group(bestmatches, matrix, whole, Name, 'output.txt')