from numpy import *
import numpy

from scipy import *
import scipy

from pprint import pprint as pprint

# Read file a
f = open('cho.csv', 'r')
Atmp = f.readlines()
f.close()

A = []
L = []
for l in Atmp:
  fields = l.split()
  nums = []
  l = []
  for f in fields:
    nums.append(float(f))
    l.append(0.0)
  A.append(nums)
  L.append(l)

A = mat(A)
L = mat(L)

n = shape(A)[1]

for k in range(n):
  for i in range(n):
    if k == i:
      temp = 0
      print("ey!")
      for j in range(k):
        temp = temp +L[k,j]**2
      L[k,k] = (A[k,k] - temp)**(1/2)
    else:
      temp = 0
      for j in range(i):
        temp = temp + L[i,j]*L[k,j]
      L[k,i] = (A[k,i] - temp)/L[i,i]

pprint(A)
pprint(L)

