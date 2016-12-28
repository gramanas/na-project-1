from numpy import *
import numpy

from scipy import *
import scipy

from pprint import pprint as pprint

def GS(A, b):
  n = shape(A)[1]
  x = []
  for i in range(n):
    x.append(0.0)

  x = mat(x)
  x = transpose(x)

  while True:
    x_last = copy(x)
    for i in range(n):
      j = 0
      tmp = 0
      while j < i:
        tmp = tmp + A[i,j]*x[i]
        j = j + 1
        
      j = i + 1
      tmp2 = 0
      while j < n:
        tmp2 = tmp2 + A[i,j]*x[i]
        j = j + 1
        
      x[i] = (1/A[i,i])*(b[i] - tmp - tmp2)
    if abs(max(x - x_last)) < 0.00005:
      break
  return(x)

size = 100
A = []
b = []
for i in range(size):
  if i == 0 or i == size - 1:
    b.append(3)
  else:
    b.append(1)
  row = []
  for j in range(size):
    if i == j:
      row.append(5)
    elif i + 1 == j or j + 1 == i:
      row.append(-2)
    else:
      row.append(0)
  A.append(row)

A = mat(A)
b = mat(b)
b = transpose(b)

x = GS(A, b)
pprint(x)


