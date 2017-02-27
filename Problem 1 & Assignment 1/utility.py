#=================================
# This file defines functions I 
# will use in the main file.
#=================================

def SelectNode(ConnectInfo):
    Dict = {}
    for x in ConnectInfo:
        if Dict.get(x[1]) == None:
            Dict[x[1]] = [x[0]]
        else:
            Dict[x[1]].append(x[0])
    return Dict


def HashFunction(NodeList):
    return sum(map(lambda x: 2 ** x, NodeList))


def HashFunction_inverse(Value):
    List = []
    k = 0
    while Value:
        if Value % 2 == 1:
            List.append(k)
        k += 1
        Value /= 2
    return List


def ReadFile(filename):
    fobj = open(filename)
    WholeInfo = fobj.read().split('\n')
    # Get the General Info
    Linesize = len(WholeInfo) - 1
    WholeGeneral = WholeInfo[0].split(' ')
    TaskN = int(WholeGeneral[0])
    TargetV = float(WholeGeneral[1])
    Deadline = float(WholeGeneral[2])
    Maxsize = int(WholeGeneral[3])  # Max size of queue
    # TaskN*3 Matrix
    NodeInfo = map(lambda x: map(int, x.split(' ')), WholeInfo[1:TaskN + 1])
    ConnectInfo = map(lambda x: map(int, x.split(' ')), WholeInfo[
                      TaskN + 1:Linesize])  # Rest*2 Matrix
    ConnectNode = SelectNode(ConnectInfo)  # Dict contains Info of Node
    return (TaskN, TargetV, Deadline, Maxsize, NodeInfo, ConnectNode)


def findlast(ConnectNode, CurrentNode, Maxsize, NodeInfo, Deadline):
    if CurrentNode:
        if len(NodeInfo) > max(CurrentNode):
            CurrentValue = sum(map(lambda x: NodeInfo[x][2], CurrentNode))
        else:
            CurrentValue = 0
    else:
        CurrentValue = 0
    if len(CurrentNode) == Maxsize or CurrentValue > Deadline:
        return 0  # means this list has got its maximum length
    else:
        Addnodes = []
        NodeID = map(lambda x: NodeInfo[x][0], range(0, len(NodeInfo)))
        Hasconnnection = ConnectNode.keys()  # ID that has connection on them
        flag = 0  # Has queue updated
        for x in NodeID:
            if (x not in Hasconnnection) & (x not in CurrentNode):
                Addnodes.append(CurrentNode + [x])
                flag = 1
            elif (x in Hasconnnection) & (x not in CurrentNode):
                if len(ConnectNode[x]) == 1:
                    if ConnectNode[x][0] in CurrentNode:
                        Addnodes.append(CurrentNode + [x])
                        flag = 1
                elif min(map(lambda m: (ConnectNode[x][m] in CurrentNode), range(0, len(ConnectNode[x])))):
                    Addnodes.append(CurrentNode + [x])
                    flag = 1
        if flag == 0:
            return 0  # 0 means this current node list is the end
        else:
            return Addnodes


def findlast_Hash(queue, CurrentNumber, ConnectNode, Maxsize, NodeInfo, Deadline):
    CurrentNode = HashFunction_inverse(CurrentNumber)
    CurrentValue = sum(map(lambda x: NodeInfo[x][2], CurrentNode))
    if len(CurrentNode) == Maxsize and CurrentValue > Deadline:
        return 0  # means this list has got its maximum length
    else:
        Addnote = []
        NodeID = map(lambda x: NodeInfo[x][0], range(0, len(NodeInfo)))
        Hasconnnection = ConnectNode.keys()  # ID that has connection on them
        flag = 0  # Has queue updated?
        for x in NodeID:
            AfterNumber = CurrentNumber + 2 ** x
            if (x not in Hasconnnection) & (x not in CurrentNode) & (AfterNumber not in queue):
                Addnote.append(AfterNumber)
                flag = 1
            elif (x in Hasconnnection) & (x not in CurrentNode) & (AfterNumber not in queue):
                if len(ConnectNode[x]) == 1:
                    if ConnectNode[x][0] in CurrentNode:
                        Addnote.append(AfterNumber)
                        flag = 1
                elif min(map(lambda m: (ConnectNode[x][m] in CurrentNode), range(0, len(ConnectNode[x])))):
                    Addnote.append(AfterNumber)
                    flag = 1
        if flag == 0:
            return 0  # 0 means this current node list is the end
        else:
            return Addnote


def Test_Goal(NodeInfo, CurrentNode, TargetV, Deadline):
    CurrentValue = sum(map(lambda x: NodeInfo[x][1], CurrentNode))
    CurrentTime = sum(map(lambda x: NodeInfo[x][2], CurrentNode))
    if CurrentValue >= TargetV and CurrentTime <= Deadline:
        return True
    else:
        return False

def BFS_withhash(TaskN, TargetV, Deadline, Maxsize, NodeInfo, ConnectNode):
    search = 0
    queue = []
    K = findlast(ConnectNode, [], Maxsize, NodeInfo, Deadline)
    if K:
        queue = map(HashFunction, K)
    if queue == []:
        return 0, len(NodeInfo)
    while queue:
        CurrentNumber = queue[0]
        del queue[0]
        search += 1
        if Test_Goal(NodeInfo, HashFunction_inverse(CurrentNumber), TargetV, Deadline):
            CurrentNode = HashFunction_inverse(CurrentNumber)
            TimeUse = sum(map(lambda x: NodeInfo[x][2], CurrentNode))
            Value = sum(map(lambda x: NodeInfo[x][1], CurrentNode))
            NewInfo = map(lambda x: NodeInfo[x], CurrentNode)
            NodeList = []
            NodeList = findlast(ConnectNode, NodeList, Maxsize, NewInfo, Deadline)
            while findlast(ConnectNode, NodeList[0], Maxsize, NewInfo, Deadline):
                NodeList = findlast(ConnectNode, NodeList[0], Maxsize, NewInfo, Deadline)
            return NodeList[0], Value, TimeUse, search
        else:
            Addnote = findlast_Hash(
                queue, CurrentNumber, ConnectNode, Maxsize, NodeInfo, Deadline)
            if Addnote:
                queue += Addnote
    return 0, search

def DFSForID(TargetV, Deadline, Maxsize, NodeInfo, ConnectNode, CurrentNode):
    if len(CurrentNode) == Maxsize:
        return 0
    else:
        # Add Node to queue
        queue = findlast(ConnectNode, CurrentNode, Maxsize, NodeInfo, Deadline)
        while queue:
            CurrentNode = queue[-1]
            del queue[-1]
            if Test_Goal(NodeInfo, CurrentNode, TargetV, Deadline):
                TimeUse = sum(map(lambda x: NodeInfo[x][2], CurrentNode))
                Value = sum(map(lambda x: NodeInfo[x][1], CurrentNode))
                return CurrentNode, Value, TimeUse
            else:
                Addnote = findlast(ConnectNode, CurrentNode, Maxsize, NodeInfo, Deadline)
                if Addnote:
                    queue += Addnote
        return 0

def Transaction(CurrentNumber, TaskN, NodeInfo, ConnectNode, Deadline):
    CurrentNode = HashFunction_inverse(CurrentNumber)
    NewInfo = map(lambda x: NodeInfo[x], CurrentNode)
    NodeList = []
    NodeList = findlast(ConnectNode, NodeList, TaskN, NewInfo, Deadline)
    while findlast(ConnectNode, NodeList[0], TaskN, NewInfo, Deadline):
        NodeList = findlast(ConnectNode, NodeList[0], TaskN, NewInfo, Deadline)
    return NodeList[0]

def BFS_ID(TaskN, TargetV, Deadline, Maxsize, NodeInfo, ConnectNode):
    K = findlast(ConnectNode, [], Maxsize, NodeInfo, Deadline)
    queue = []
    if K:
        queue = map(HashFunction, K)
    if queue == []:
        return 0
    if len(queue)>Maxsize:
        queue = queue[:Maxsize]
    else:
        k = len(queue)
        while k < Maxsize:
            CurrentNumber = queue[0]
            del queue[0]
            if queue == [] and findlast_Hash(queue, CurrentNumber, ConnectNode, TaskN, NodeInfo, Deadline) == 0:
                if Test_Goal(NodeInfo, HashFunction_inverse(CurrentNumber), TargetV, Deadline):
                    CurrentNode = HashFunction_inverse(CurrentNumber)
                    TimeUse = sum(map(lambda x: NodeInfo[x][2], CurrentNode))
                    Value = sum(map(lambda x: NodeInfo[x][1], CurrentNode))
                    NewInfo = map(lambda x: NodeInfo[x], CurrentNode)
                    NodeList = []
                    NodeList = findlast(ConnectNode, NodeList, Maxsize, NewInfo, Deadline)
                    while findlast(ConnectNode, NodeList[0], Maxsize, NewInfo, Deadline):
                        NodeList = findlast(ConnectNode, NodeList[0], Maxsize, NewInfo, Deadline)
                    return NodeList[0], Value, TimeUse
                else:
                    return 0
            else:
                if Test_Goal(NodeInfo, HashFunction_inverse(CurrentNumber), TargetV, Deadline):
                    CurrentNode = HashFunction_inverse(CurrentNumber)
                    TimeUse = sum(map(lambda x: NodeInfo[x][2], CurrentNode))
                    Value = sum(map(lambda x: NodeInfo[x][1], CurrentNode))
                    NewInfo = map(lambda x: NodeInfo[x], CurrentNode)
                    NodeList = []
                    NodeList = findlast(ConnectNode, NodeList, TaskN, NewInfo, Deadline)
                    while findlast(ConnectNode, NodeList[0], TaskN, NewInfo, Deadline):
                        NodeList = findlast(ConnectNode, NodeList[0], TaskN, NewInfo, Deadline)
                    return NodeList[0], Value, TimeUse
                else:
                    Addnode = findlast_Hash(queue, CurrentNumber, ConnectNode, TaskN, NodeInfo, Deadline)
                    if Addnode:
                        queue += Addnode
                        if len(queue) > Maxsize:
                            queue = queue[:Maxsize]
                    k = len(queue)
    queue = map(lambda x: Transaction(x, TaskN, NodeInfo, ConnectNode, Deadline), queue)
    N = len(queue[-1])
    while N <= TaskN:
        for x in xrange(1,len(queue) + 1):
            CurrentNode = queue[-x]
            Output = DFSForID(TargetV, Deadline, N, NodeInfo, ConnectNode, CurrentNode)
            if Output:
                return Output
        N += 1
    return 0