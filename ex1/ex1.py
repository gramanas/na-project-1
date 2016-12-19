from numpy import *
import numpy

from scipy import *
import scipy

import matplotlib.pyplot as plt

t = arange(0,3.001,step=.001)

def f(t):
  return (14*t)*(e**(t-2)) - 12*(e**(t-2)) - 7*(t**3) + 20*(t**2) - 26*t + 12

# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.plot(t, f(t))
# plt.grid(True)
# plt.show()

def dixotomisi(a, b):
  root = (a + b) / 2

  # number of times to repeat to achieve 6 points accuracy
  N = int(ceil((log(b - a) - log(0.000005)) / log(2))) + 20

  for i in range(0, N):
    if (f(a) < 0 and f(root) > 0) or (f(a) > 0 and f(root) < 0):
      b = root
    elif (f(b) < 0 and f(root) > 0) or (f(b) > 0 and f(root) < 0):
      a = root
    root = (a + b) / 2

  return ("f(%.6f) = %.6f" % (root, f(root)))

print("Root in [0,1.5]: %s" % (dixotomisi(0,1.5)))
print("Root in [1.5,3]: %s" % (dixotomisi(1.5,3)))

def f_der(t):
  return (14*t)*(e**(t-2)) + 2*(e**(t-2)) - 21*(t**2) + 40*t - 26

def f_der_2(t):
  return (14*t)*(e**(t-2)) - 16*(e**(t-2)) - 42*t + 40

# plt.xlabel("x")
# plt.ylabel("f'(x)")
# plt.plot(t, f(t), c='r')
# plt.plot(t, f_der(t), c='g')
# plt.plot(t, f_der_2(t), c='b')
# plt.grid(True)
# plt.show()

temp_l = [3]

def new_raph():
  pff =  temp_l[i] - (f(temp_l[i])/f_der(temp_l[i]))
  temp_l.append(pff)

i = 0
while round(f(temp_l[-1]), 20) != 0.000000: 
  new_raph()
  i = i + 1
  print(temp_l[i])
print(i)
