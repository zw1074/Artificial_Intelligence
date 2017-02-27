import copy

def is_literal(S):
	accord = []
	literal = []
	for s in S:
		for x in s:
			if abs(x) not in literal and -abs(x) not in literal and abs(x) not in accord:
				literal.append(x)
			elif abs(x) in literal:
				if abs(x) + x == 0:
					literal.remove(abs(x))
					accord += [abs(x)]
			elif -abs(x) in literal:
				if -abs(x) + x == 0:
					literal.remove(-abs(x))
					accord += [abs(x)]
	if literal == []:
		return 0
	else:
		return literal[0]

def is_singleton(S):
	for s in S:
		if len(s) == 1:
			return s[0]
	return 0

def pick(V):
	for A in V.keys():
		if V[A] == []:
			return A

def prepegate(Atom,S):
	OldS = copy.deepcopy(S)
	NewS = []
	for s in OldS:
		if Atom not in s and -Atom not in s:
			NewS.append(s)
		elif -Atom in s:
			s.remove(-Atom)
			NewS.append(s)
	return NewS

def dp1(Atoms,S,V):
	literal = is_literal(S)
	s = is_singleton(S)
	if S == []:
		for A in Atoms:
			if V[A] == []:
				V[A] = [T]
		return V
	elif [] in S:
		return 'NIL'
	while s or literal:
		if S == []:
			for A in Atoms:
				if V[A] == []:
					V[A] = ['T']
			return V
		elif [] in S:
			return 'NIL'
		# If it exists easy case.
		if literal:
			if literal < 0:
				V[abs(literal)] = ['F']
			else:
				V[literal] = ['T']
			S = prepegate(literal,S)
			literal = is_literal(S)
		elif s:
			if s < 0:
				V[abs(s)] = ['F']
			else:
				V[s] = ['T']
			S = prepegate(s,S)
			s = is_singleton(S)

	if S == []:
		for A in Atoms:
			if V[A] == []:
				V[A] = ['T']
		return V
	elif [] in S:
		return 'NIL'
	TryAtom = pick(V)
	V[TryAtom] = ['T']
	S1 = prepegate(TryAtom,S)
	OldV = copy.deepcopy(V)
	VNEW = dp1(Atoms,S1,OldV)
	if VNEW != 'NIL':
		return VNEW
	V[TryAtom] = ['F']
	S1 = prepegate(-TryAtom,S)
	return dp1(Atoms,S1,V)

def dp(Input,Output):
	fobj = open(Input)
	Info = fobj.read().split('\n')
	fobj.close()
	Info.pop(-1)
	InfoList = map(lambda x:x.split(' '), Info)
	InfoList = map(lambda x:map(lambda y:int(y),x),InfoList)
	Atoms = []
	for x in InfoList:
		Atoms = list(set(Atoms + map(lambda y:abs(y),x)))
	V = {}
	for A in Atoms:
		V[A] = []
	fobj = open(Output,'w+')
	a = dp1(Atoms,InfoList,V)
	if a == 'NIL':
		fobj.write('0')
		return 0
	else:
		for key in a.keys():
			fobj.write('%d %s\n' % (key,a[key][0]))
		fobj.write('0')
		return 0

dp('Example.txt', 'Input For Backend.txt')