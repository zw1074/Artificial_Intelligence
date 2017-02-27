# Solution for Decision Tree in Review/Publish system
This file will introduce the problem and give the method to solve the problem

## Problem Introduction
The problem wants to find out a way to optimize the Review/Publish process. The detail for this problem is presented [here](http://cs.nyu.edu/courses/fall15/CSCI-GA.2560-001/prog3.pdf).

Input for this problem is like
```
2 50000 -2000 0.2
400 0.9 0.2
100 0.6 0.3
```

Here, in line 1, number of reviewers R. Utility of success. Utility of failure.

In line through `R + 1`. One line per reviewer. Cost of reviewer. `P(R = T|Success)`. `P(R = T|Failure)`.

The output is an interact interface.
```
Expected Value: 8540
Consult reviewer 2: Yes
Publish
```

## How to compile it
### utility.py
This `.py` file contains the basic function for the main program. Every function has the interprete. The basic idea for solving this problem is using the recursion until it reaches the leaf. This is kind of like DFS. However, the problem for this program is that everytime you type in the result of the reviewer it will re-search every brunch below this review. So the the total running time is about O(2^{n+1}).

### main.py
This file is the main program. So to compile this whole program, you just need to type the following script in any bash command line system:
```python
python main.py
```