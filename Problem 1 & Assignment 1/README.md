# Solve a DAG problem
This file will introduce the idea of how to solve a **DAG** problem and how to compile it.

## Problem and Idea
The problem is how to solve a **DAG** via ID with BFS Method. Detail can be found in [here](http://cs.nyu.edu/courses/fall15/CSCI-GA.2560-001/prog1.html). It will be stored in `sample text.txt`. For illustration, here is a sample:
```python
5 12 7 3
0 3 3
1 6 2
2 4 3
3 1 6
4 4 1
0 1
2 3
4 1
4 3
```
Explanation for this sample can be found in [here](http://cs.nyu.edu/courses/fall15/CSCI-GA.2560-001/prog1.html).

The solution for this is:
> [0 4 1] 13 6

The idea is to generate a tree-structure state space. By using different search method -- **DFS** and **BFS**, we can get the answer.

## How to compile it
I write the solution by Python, there are several .py files. I would like to show these functions.

### utility.py
This file store many functions. Noticed that the function `BFS_withhash()` is not used in `main.py`. I still want to add it because it is processed extremely fast, Although the memory it requests are high. :)

### main.py
This file will read the content of `sample text.txt`, then will print the solution. To compile it, just make sure you have python 2.7 compiler, and then use
```terminal
python main.py
```
to compile it. 

### Custom.py
This file can let you custom the size of **DAG**. It will ask you several question, then use the generation way from [Problem Set 1](http://cs.nyu.edu/courses/fall15/CSCI-GA.2560-001/prog1.html). To compile, just type
```terminal
python Custom.py
```

### experiment.py
This file will make an experiment which is called from [Problem Set 1](http://cs.nyu.edu/courses/fall15/CSCI-GA.2560-001/prog1.html). The result will be printed in `result.txt`. You can modify the file to control the size of experiment.
```python
MinNumber = 1 # The experiment will start from this size
MaxNumber = 13 # The experiment will end at this size
ExperimentTime = 1000 # How many times will each size repeat
```