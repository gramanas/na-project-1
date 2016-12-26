from numpy import *
import numpy

from scipy import *
import scipy

from pprint import pprint as pprint

# Read file a
f = open('a.csv', 'r')
Atmp = f.readlines()
f.close()

A = []
L = []
U = []
nn = 1
for l in Atmp:
  fields = l.split()
  nums = []
  fn = 1
  Ln = []
  Un = []
  for f in fields:
    nums.append(float(f))
    if nn == fn:
      Ln.append(1.0)
    else:
      Ln.append(0.0)
    fn = fn + 1
  A.append(nums)
  L.append(Ln)
  U.append(nums)
  nn = nn + 1

A = mat(A)
L = mat(L)
U = mat(U)

# Read file b
f = open('b.csv', 'r')
btmp = f.readlines()
f.close()

b = []
x = []
for l in btmp:
  b.append(float(l))
  x.append(0)

b = mat(b)
x = mat(x)

# Get n
n = shape(A)[1]

#find L and U
for i in range(n):
  for j in range(i+1,n):
    L[j,i] = U[j,i]/U[i,i]
    U[j,:] = U[j,:] - U[i,:]*(U[j,i]/U[i,i])

b = transpose(b)

y = []
for i in range(n):
  temp = 0
  j = 0
  while i > j:
    temp = temp + y[j]*float(L[i,j])
    j = j + 1
  y.append(float(b[i]) - temp)

y = mat(y)
y = transpose(y)

x = []
for i in range(n-1,-1,-1):
  temp = 0
  j = n-1
  while j != i:
    temp = temp + U[i,j]*x[(n-1)-j]
    j = j - 1    
  x.append((float(y[i]) - temp)/float(U[i,i]))

#reverse x
x = x[::-1]

x = mat(x)
x = transpose(x)

print("\nA: ")
pprint(A)
print("b: ")
pprint(b)
print("U: ")
pprint(U)
print("L: ")
pprint(L)
print("y: ")
pprint(y)
print("x: ")
pprint(x)
print("A*x:")
pprint(A*x)
