import random
import numpy as np
import math


def L2(vector1, vector2):
	'''
	L2 matric
	'''
	return math.sqrt(sum([(vector1[i] - vector2[i])**2 for i in xrange(len(vector1))]))

def pearson(vector1, vector2):
	'''
	Pearson correlation
	'''
	n = len(vector1)
	Domain = sum([vector1[i]*vector2[i] for i in xrange(n)]) - sum(vector1)*sum(vector2)/float(n)
	Domninant = math.sqrt((sum([pow(x,2) for x in vector1]) - pow(sum(vector1),2)/float(n))*(sum([pow(x,2) for x in vector2]) - pow(sum(vector2),2)/float(n)))
	if Domninant == 0:
		return 0
	return Domain/Domninant

def cosine(vector1, vector2):
	'''
	cosine matric
	'''
	Domain = sum([vector1[i] * vector2[i] for i in xrange(len(vector1))])
	Domninant = math.sqrt(sum([i**2 for i in vector1])) * math.sqrt(sum([i**2 for i in vector2]))
	if Domninant == 0:
		return 0
	return Domain/float(Domninant)

def kmeans(matrix, iteration, distance = L2, k=4):
	'''
	matrix: 2-d matrix. The structure is like [a_1, a_2, ... , a_n], 
	which means n vectors. Each vector has same length.
	'''

	# Determine the minimum and maximum range.
	ranges = [(min([row[i] for row in matrix]), max([row[i] for row in matrix])) for i in xrange(len(matrix[0]))]

	# Create k random cluster
	clusters = [[random.random()*(ranges[i][1] - ranges[i][0]) + ranges[i][0] for i in xrange(len(matrix[0]))] for j in xrange(k)]
	lastmatches = None
	for t in xrange(iteration):
		print "Iteration %d" % t
		bestmatches = [[] for i in xrange(k)]

		# Find which centroid is the cloest for each vector.
		for j in xrange(len(matrix)):
			row = matrix[j]
			bestmatch = 0
			for i in xrange(k):
				d = distance(clusters[i],row)
				if d<distance(clusters[bestmatch], row): 
					bestmatch=i
			bestmatches[bestmatch].append(j)

		# If the results are the same as last time, this is complete
		if bestmatches == lastmatches:
			break
		lastmatches = bestmatches

		# Move the centroids to the average of their members
		for i in xrange(k):
			if len(bestmatches[i]) >0:
				avgs = [np.mean([matrix[j][l] for j in bestmatches[i]]) for l in xrange(len(matrix[0]))]
				clusters[i] = avgs

	return bestmatches

