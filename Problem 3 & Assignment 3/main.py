from utility import *

RNumber, US, UF, PS, RC, PTS, PTF = readfile('input.txt')
SuccessList, FailureList = condition_probability(PTS,PTF,RNumber)
remainsidlist = range(RNumber)
HashValue = 0
maxchoice, expectation = choice(remainsidlist, 0, 2, SuccessList, FailureList, PS, US, UF, RC, RNumber)
print 'Expected value: %.3f' % expectation
while maxchoice != 'Publish' and maxchoice != 'Reject':
	inputstring = raw_input(maxchoice + ':')
	while inputstring != 'Yes' and inputstring != 'No':
		inputstring = raw_input('Please input a valid string (e.g. Yes):')
	reviewid = int(maxchoice.split(' ')[-1]) - 1
	remainsidlist.remove(reviewid)
	if inputstring == 'Yes':
		HashValue += (3**reviewid)
		maxchoice, expectation = choice(remainsidlist, HashValue, 1, SuccessList, FailureList, PS, US, UF, RC, RNumber)
	else:
		HashValue += (3**reviewid)*2
		maxchoice, expectation = choice(remainsidlist, HashValue, 0, SuccessList, FailureList, PS, US, UF, RC, RNumber)
print maxchoice