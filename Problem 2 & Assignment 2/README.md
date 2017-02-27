# Solution for Parallel Program Optimization Problem
This file will introduce the problem and give the way that how to compile it.

## Problem Introduction
Parallel program optimization problem wants to find a way for the cores to transmit the data in a certain time. The detail for this problem is presented [here](http://cs.nyu.edu/courses/fall15/CSCI-GA.2560-001/prog2.html).

Input for this problem is like:
```python
1 A 2 B 3 C 4 D
2 A 3 A 4 C
2
```

which means:

**Start:** R1 = A, R2 = B, R3 = C, R4 = D.

**End:** R2 = A, R3 = A, R4 = C.

K = 2

The solution for this
```
Cycle 1: R2 = R1; R4 = R3. 
Cycle 2: R3 = R1.
```
## How to compile it
In this *python* program, I have written some python files.

### FrontEnd.py
This module mainly defines a function called `FrontEnd(Input, Outputname, BackEnd)`. `Input` is the input file name for `FrontEnd`. In this case is `Sample.txt`. And `Outputname` will give the output which is also an input for `DPLL.py`. And `BackEnd` will give the number information for `BackEnd.py`. In it, it is like
```bash
2 3 1 A 62
2 C 2 V 19
1 C 1 V 6
2 C 1 V 18
4 E 2 V 47
3 A 2 V 27
1 C 3 V 8
4 2 0 A 79
2 A 1 V 14
```
`2 3 1 A 62` means number '62' matches `Assign(2,3,1)`, and `1 C 1 V 6` means number '6' matches `Value(1,C,1)`.

### DPLL.py
This module defines a function called `dp(Input,Output)`. `Input` is the output file name from `FrontEnd.py`. And `Output` is the input file name for `BackEnd.py`

### BackEnd.py
This module defines a function called `backend(Input,Table)`. `Input` is the output file name from `DPLL.py`. And `Table` is the output file name from `FrontEnd.py`. Then it will print the solution on the screen.

### main.py
This file combines the three module above. And then it gives the solution, you can change the problem in `Sample.txt`. To compile it, just tpye in `-bash`:
```
python main.py
```