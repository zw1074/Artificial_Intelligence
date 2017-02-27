from utility import *
from DAG_Generator import *
import types

N = int(raw_input("Please input the number of tasks (int):"))
Maxsize = int(raw_input("Please input the max size of queue (int):"))

# Generate DAG
DAG_Generator(N, Maxsize)
print 'Generate DAG successfully!\n'

Answer = raw_input('Do you want to show the DAG?(yes/no):')
while Answer != 'yes' and Answer != 'no':
	Answer = raw_input('Please re-type yes or no:')

if Answer == 'yes':
	fobj = open('sample text2.txt')
	print fobj.read()
	fobj.close

raw_input('Press any key to continue')
(TaskN, TargetV, Deadline, Maxsize, NodeInfo, ConnectNode) = ReadFile('sample text2.txt')

print 'The result of this DAG is:(0 for failure and ([list], Total Value, Total Time) for success)\n'
print BFS_ID(TaskN, TargetV, Deadline, Maxsize, NodeInfo, ConnectNode)