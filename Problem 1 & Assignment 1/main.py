from utility import *

(TaskN, TargetV, Deadline, Maxsize, NodeInfo, ConnectNode) = ReadFile('sample text.txt')

print 'The result of this DAG is:(0 for failure and ([list], Total Value, Total Time) for success)'
print BFS_ID(TaskN, TargetV, Deadline, Maxsize, NodeInfo, ConnectNode)