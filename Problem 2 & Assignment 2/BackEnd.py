def backend(Input,Table):
	fobj = open(Input)
	fobj1 = open(Table)
	if fobj.read(1) == '0':
		print 'No solution'
		return 0
	else:
		fobj.seek(0)
		Info = fobj.read().split('\n')
		fobj.close()
		Info.pop(-1)
		Info1 = fobj1.read().split('\n')
		fobj1.close()
		Info1.pop(-1)
		Info = map(lambda x:x.split(' '), Info)
		Info = map(lambda x:[int(x[0]),x[1]], Info)
		Info1 = map(lambda x:x.split(' '), Info1)
		Info1 = map(lambda x:[x[0],x[1],int(x[2]),x[3],int(x[4])],Info1)
		Infoindex = map(lambda x:x[4], Info1)
		CorrectAssign = []
		for x in Info:
			if x[1] == 'T' and Info1[Infoindex.index(x[0])][3] == 'A':
				CorrectAssign.append(Info1[Infoindex.index(x[0])][:4])
		Dict = {}
		for val in CorrectAssign:
			if Dict.get(val[2]) == None:
				Dict[val[2]] = [val]
			else:
				Dict[val[2]].append(val)
		for time in Dict.keys():
			print 'Cycle %d:' % (time+1),
			for val in Dict[time]:
				print 'R%s = R%s;' % (val[0],val[1]),
			print '\n',