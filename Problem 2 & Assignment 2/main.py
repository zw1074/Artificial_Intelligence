from FrontEnd import *
from DPLL import *
from BackEnd import *

FrontEnd('Sample.txt', 'Input For DPLL.txt', 'Table.txt')

dp('Input For DPLL.txt', 'Input For Backend.txt')

Input = 'Input For Backend.txt'
Table = 'Table.txt'
backend(Input,Table)