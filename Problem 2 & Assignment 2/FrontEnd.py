def FrontEnd(Input, Outputname,BackEnd):
	fobj = open(Input)
	WholeInfo = fobj.read().split('\n')
	fobj.close()
	StartInfo = WholeInfo[0].split(' ')
	TaskID_S = StartInfo[0:len(StartInfo):2]
	TaskV_S = StartInfo[1:len(StartInfo):2]
	GoalInfo = WholeInfo[1].split(' ')
	TaskID_G = GoalInfo[0:len(GoalInfo):2]
	TaskV_G = GoalInfo[1:len(GoalInfo):2]
	K = int(WholeInfo[2])
	TotalV = list(set(TaskV_S))
	table = {}
	number = 1
	fobj = open(Outputname,'w+')
	# Generate the value and assign dictionary
	for R in TaskID_S:
		for V in TotalV:
			for I in xrange(0,K+1):
				table[(R,V,I,'V')] = number
				number += 1

	for R1 in TaskID_S:
		for R2 in TaskID_S:
			if R2 != R1:
				for I in xrange(0,K):
					table[(R1,R2,I,'A')] = number
					number += 1
	
	# Generate the clause form
	for I in xrange(0,K+1):
		for R in TaskID_S:
			for V1 in TotalV:
				for V2 in TotalV:
					if V2 != V1:
						fobj.write('-%d -%d\n' % (table[(R,V1,I,'V')],table[(R,V2,I,'V')]))
	for I in xrange(0,K):
		for R1 in TaskID_S:
			for R2 in TaskID_S:
				if R2 != R1:
					for V in TotalV:
						fobj.write('-%d -%d %d\n' % (table[(R1,R2,I,'A')],table[(R2,V,I,'V')],table[(R1,V,I+1,'V')])) 
		for R in TaskID_S:
			for V in TotalV:
				fobj.write('-%d ' % table[(R,V,I,'V')])
				for R1 in TaskID_S:
					if R1 != R:
						fobj.write('%d ' % table[(R,R1,I,'A')])
				fobj.write('%d\n' % table[(R,V,I+1,'V')])
		for RA in TaskID_S:
			for RB in TaskID_S:
				if RB != RA:
					for RC in TaskID_S:
						if RC != RB and RC != RA:
							fobj.write('-%d -%d\n-%d -%d\n-%d -%d\n-%d -%d\n' % (table[(RA,RB,I,'A')],table[(RB,RA,I,'A')],table[(RA,RB,I,'A')],table[(RA,RC,I,'A')],table[(RA,RB,I,'A')],table[(RB,RC,I,'A')],table[(RA,RB,I,'A')],table[(RC,RA,I,'A')]))
	for i in xrange(len(TaskID_S)):
		fobj.write('%d\n' % table[(TaskID_S[i],TaskV_S[i],0,'V')])
	for i in xrange(len(TaskID_G)):
		fobj.write('%d\n' % table[(TaskID_G[i],TaskV_G[i],K,'V')])
	fobj.write('0')
	fobj.close()
	fobj = open(BackEnd,'w+')
	for key in table.keys():
		fobj.write('%s %s %s %s %d\n' % (str(key[0]),str(key[1]),str(key[2]),str(key[3]),table[key]))


FrontEnd('Sample.txt', 'Input For DPLL.txt', 'Table.txt')