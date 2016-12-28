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
  for f in fields:
    nums.append(float(f))
  A.append(nums)

A = mat(A)

def cholesky(A):
  n = shape(A)[1]

  L = empty([n,n])
  L = mat(L)
  
  for k in range(n):
    for i in range(n):
      if k == i:
        temp = 0
        for j in range(k):
          temp = temp + L[k,j]**2
        L[k,k] = (A[k,k] - temp)**(1/2)
      else:
        temp = 0
        for j in range(i):
          temp = temp + L[i,j]*L[k,j]
        L[k,i] = (A[k,i] - temp)/L[i,i]
      if k < i:
        L[k,i] = 0

  return(L)

pprint(cholesky(A))
