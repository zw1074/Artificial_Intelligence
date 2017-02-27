# This file will test N = 5 to 200. Each N will be tested 1000 times
from random import *
from math import *
from utility import *

MinNumber = 1  # The experiment will start from this size
MaxNumber = 13  # The experiment will end at this size
ExperimentTime = 1000  # How many times will each size repeat
Ratelist = []
MaxSearch = []
MinSearch = []
AverageSearch = []
for TaskN in range(MinNumber, MaxNumber + 1):
    # Some parameters
    Success = 0
    Search = []
    # Solve the problem
    for x in xrange(ExperimentTime):
        # Solve by BFS with hash table.
        TargetV = uniform(
            TaskN ** 2 * (1 - 2 / sqrt(TaskN)) / 4, TaskN ** 2 * (1 + 2 / sqrt(TaskN)) / 4)
        Deadline = uniform(
            TaskN ** 2 * (1 - 2 / sqrt(TaskN)) / 4, TaskN ** 2 * (1 + 2 / sqrt(TaskN)) / 4)
        Maxsize = TaskN
        NodeInfo = []
        for i in xrange(0, TaskN):
            NodeInfo.append([i, randint(0, TaskN), randint(0, TaskN)])
        ConnectInfo = []
        P = range(0, TaskN)
        for I in range(0, TaskN):
            J = randint(I, TaskN - 1)
            M = P[I]
            P[I] = P[J]
            P[J] = M
        for I in range(0, TaskN - 1):
            for J in range(I + 1, TaskN):
                if random() > 0.5:
                    ConnectInfo.append([P[I], P[J]])
        ConnectNode = SelectNode(ConnectInfo)
        K = BFS_withhash(
            TaskN, TargetV, Deadline, Maxsize, NodeInfo, ConnectNode)
        if K[0]:
            Success += 1
            Search.append(K[3])
        else:
            Search.append(K[1])
    MaxSearch.append(max(Search))
    MinSearch.append(min(Search))
    AverageSearch.append(sum(Search) / float(len(Search)))
    Ratelist.append(Success / float(ExperimentTime))

fobj = open("result.txt", 'w')
fobj.write("The fraction of task whose number is from %d to %d is:\n" %
           (MinNumber, MaxNumber))
fobj.write(str(Ratelist))
fobj.write("\n")
fobj.write("The maximum search state for task number from %d to %d is:\n" % (
    MinNumber, MaxNumber))
fobj.write(str(MaxSearch))
fobj.write("\n")
fobj.write("The minimum search state for task number from %d to %d is:\n" % (
    MinNumber, MaxNumber))
fobj.write(str(MinSearch))
fobj.write("\n")
fobj.write("The average search state for task number from %d to %d is:\n" % (
    MinNumber, MaxNumber))
fobj.write(str(AverageSearch))
