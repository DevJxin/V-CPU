from Gates import CarryIn
from tester import *

bus_a = [[None]*8 for _ in range(9)]

bus_b = [[None]*8 for _ in range(9)] 

Carry = [None]*9

Sum = [[None]*8 for _ in range(8)]

i=0

for x,y,z in Testing():
   bus_a[i] = x
   bus_b[i] = y
   Carry[i] = z
   i+=1