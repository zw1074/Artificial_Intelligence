import itertools
import copy

def readfile(inputname):
	'''
	Reads the input text file.
	'''
	fobj = open(inputname)
	info = fobj.readlines()
	info = map(lambda x: x.split(' '), info)
	RNumber = int(info[0][0]) # Number of reviewers
	US = float(info[0][1]) # Utility of success
	UF = float(info[0][2]) # Utility of failure
	PS = float(info[0][3]) # Probability of success
	RC = map(lambda x: float(x[0]), info[1:]) # Cost of reviewer
	PTS = map(lambda x: float(x[1]), info[1:]) # P(R=T|Success)
	PTF = map(lambda x: float(x[2]), info[1:]) # P(R=T|Failure)
	return RNumber, US, UF, PS, RC, PTS, PTF

def Hashfunction(Combination, PossibleValue, PTS, PTF):
	'''
	Function will take the reviewer combination and the every T or F possible value.
	Then return combinations value (HashValue), P(Reviewers|S) and P(Reviewers|F)

	Variables:
	Combination: list of reviewer ids. (e.g. [2,4,5])
	PossibleValue: list of possible value of reviewer ids. The length must be 2**len(Combination).
	PTS: list of P(R = T|S)
	PTF: list of P(R = T|F)
	'''
	HashValue = 0
	Success = 1
	Failure = 1
	for i in xrange(len(Combination)):
		HashValue += (3**Combination[i])*PossibleValue[i]
		if PossibleValue[i] == 1:
			Success *= PTS[Combination[i]]
			Failure *= PTF[Combination[i]]
		else:
			Success *= 1 - PTS[Combination[i]]
			Failure *= 1 - PTF[Combination[i]]
	return HashValue, Success, Failure

def condition_probability(PTS,PTF,RNumber):
	'''
	Give the condition probability for every possible 
	combinations and possible value of every reviewers.
	'''
	SuccessList = {}
	FailureList = {}
	for i in xrange(RNumber):
		Combination = list(itertools.combinations(range(RNumber),i+1))
		PossibleValue = list(itertools.product([1,2],repeat = i+1))
		for j in Combination:
			for k in PossibleValue:
				HashValue, Success, Failure = Hashfunction(j, k, PTS, PTF)
				SuccessList[HashValue] = Success
				FailureList[HashValue] = Failure
	return SuccessList, FailureList

def Hash_inverse(HashValue):
	'''
	Interprete the HashValue to a list of reviewers.
	'''
	reviewresult = {}
	k = 0
	while HashValue:
		if HashValue % 3 == 1:
			reviewresult[k] = 1 # means true
		elif HashValue % 3 == 2:
			reviewresult[k] = 2 # means false
		k += 1
		HashValue /= 3
	return reviewresult

# return expectation and choice
def choice(remainsidlist, HashValue, lastreview, SuccessList, FailureList, PS, US, UF, RC, RNumber):
	'''
	Give the optimize choice based on every chance node's expected value
	'''
	maxexpectation = UF - sum(map(lambda i: RC[i], xrange(RNumber)))
	if lastreview == 1:
		for i in remainsidlist:
			expectation = chance(remainsidlist, i, 'Review', HashValue, SuccessList, FailureList, PS, US, UF, RC, RNumber)
			if expectation > maxexpectation:
				maxchoice = 'Cousult reviewer' + ' ' + str(i+1)
				maxexpectation = expectation
		expectation = chance(remainsidlist, 0, 'Publish', HashValue, SuccessList, FailureList, PS, US, UF, RC, RNumber)
		if expectation > maxexpectation:
			maxchoice = 'Publish'
			maxexpectation = expectation
	elif lastreview == 0:
		for i in remainsidlist:
			expectation = chance(remainsidlist, i, 'Review', HashValue, SuccessList, FailureList, PS, US, UF, RC, RNumber)
			if expectation > maxexpectation:
				maxchoice = 'Cousult reviewer' + ' ' + str(i+1)
				maxexpectation = expectation
		expectation = chance(remainsidlist, 0, 'Reject', HashValue, SuccessList, FailureList, PS, US, UF, RC, RNumber)
		if expectation > maxexpectation:
			maxchoice = 'Reject'
			maxexpectation = expectation
	else:
		for i in remainsidlist:
			expectation = chance(remainsidlist, i, 'Review', HashValue, SuccessList, FailureList, PS, US, UF, RC, RNumber)
			if expectation > maxexpectation:
				maxchoice = 'Cousult reviewer' + ' ' + str(i+1)
				maxexpectation = expectation
		expectation = chance(remainsidlist, 0, 'Reject', HashValue, SuccessList, FailureList, PS, US, UF, RC, RNumber)
		if expectation > maxexpectation:
			maxchoice = 'Reject'
			maxexpectation = expectation
		expectation = chance(remainsidlist, 0, 'Publish', HashValue, SuccessList, FailureList, PS, US, UF, RC, RNumber)
		if expectation > maxexpectation:
			maxchoice = 'Publish'
			maxexpectation = expectation
	return maxchoice,maxexpectation

def chance(oldremainsidlist, reviewid, lastchoice, HashValue, SuccessList, FailureList, PS, US, UF, RC, RNumber):
	'''
	Return the expected value of every choice node.
	'''
	remainsidlist = copy.deepcopy(oldremainsidlist)
	if HashValue == 0:
		cost = 0
		SuccessP = PS
		FailureP = 1 - PS
		Domain = 1
		old_review = None
	else:
		SuccessP = SuccessList[HashValue]*PS/(SuccessList[HashValue]*PS + FailureList[HashValue]*(1 - PS))
		FailureP = 1 - SuccessP
		old_review = Hash_inverse(HashValue).keys()
		cost = sum(map(lambda i: RC[i], old_review))
		Domain = SuccessList[HashValue]*PS + FailureList[HashValue]*(1 - PS)
	if lastchoice == 'Publish':
		Expectation = SuccessP * US + FailureP * UF - cost
	elif lastchoice == 'Review':
		HashValueY = HashValue + 3**reviewid
		HashValueN = HashValue + (3**reviewid)*2
		remainsidlist.remove(reviewid)
		YesP = (SuccessList[HashValueY]*PS + FailureList[HashValueY]*(1 - PS))/Domain
		NoP = 1 - YesP
		Expectation = YesP*choice(remainsidlist, HashValueY, 1, SuccessList, FailureList, PS, US, UF, RC, RNumber)[1] + NoP*choice(remainsidlist, HashValueN, 0, SuccessList, FailureList, PS, US, UF, RC, RNumber)[1]
	elif lastchoice == 'Reject':
		Expectation = -cost
	return Expectation

