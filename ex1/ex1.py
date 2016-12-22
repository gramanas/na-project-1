from numpy import *
import numpy

from scipy import *
import scipy

import matplotlib.pyplot as plt

t = arange(0,3.001,step=.001)

def f(t):
  return (14*t)*(e**(t-2)) - 12*(e**(t-2)) - 7*(t**3) + 20*(t**2) - 26*t + 12

def f_der(t):
  return (14*t)*(e**(t-2)) + 2*(e**(t-2)) - 21*(t**2) + 40*t - 26

def f_der_2(t):
  return (14*t)*(e**(t-2)) - 16*(e**(t-2)) - 42*t + 40

plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(t, f(t))
plt.grid(True)
plt.show()

def bisect(a, b):
  a_1, b_1 = a, b
  root = (a + b) / 2

  # number of times to repeat to achieve 6 points accuracy
  N = int(ceil((log(b - a) - log(0.0000005)) / log(2)))

  for i in range(0, N):
    if (f(a) < 0 and f(root) > 0) or (f(a) > 0 and f(root) < 0):
      b = root
    elif (f(b) < 0 and f(root) > 0) or (f(b) > 0 and f(root) < 0):
      a = root
    root = (a + b) / 2

  return root, N, a_1, b_1

def new_raph(start):
  temp_l = [start, start - (f(start)/f_der(start))]

  N = 1
  while round(f(temp_l[-1]), 6) != 0.000000:
    temp =  temp_l[N] - (f(temp_l[N])/f_der(temp_l[N]))
    temp_l.append(temp)
    N = N + 1

  root = temp_l[N] 

  return root, N, start

def interpolation(a, b):
  temp_l = [a, b, b - ((f(b)*(b - a))/f(b) - f(a))]

  N = 1
  while round(f(temp_l[-1]), 6) != 0.000000:
    temp =  temp_l[N] - (f(temp_l[N])*
                         (temp_l[N] - temp_l[N-1]))/(f(temp_l[N]) - f(temp_l[N-1]))
    temp_l.append(temp)
    N = N + 1

  root = temp_l[-1]

  return root, N, a, b 

#############
# Bisection #
#############
print("\n++++ Bisection ++++\n")

root, loops, a, b = bisect(0,1.5)
print("Root in [%.2f,%.2f] after %d loops: f(%.6f) = %.6f\n"
      % (a, b, loops, root, f(root)))

root, loops, a, b = bisect(1.5,3)
print("Root in [%.2f,%.2f] after %d loops: f(%.6f) = %.6f"
      % (a, b, loops, root, f(root)))

####################
# Newton - Raphson #
####################
print("\n++++ Newton - Raphson ++++\n")

root, loops, start = new_raph(1)
print("Starting at %.2f:\nafter %d iterations the root is: f(%.6f) = %.6f\n"
      % (start, loops, root, f(root)))
  
root, loops, start = new_raph(3)
print("Starting at %.2f:\nafter %d iterations the root is: f(%.6f) = %.6f"
      % (start, loops, root, f(root)))

#################
# Interpolation #
#################
print("\n++++ Interpolation ++++\n")

root, loops, a, b = interpolation(0.7,0.9)
print("Root found in [%.2f,%.2f] after %d iterations:" % (a, b, loops))
print("f(%.6f) = %.6f\n" % (root, f(root)))

root, loops, a, b = interpolation(1.7,2.1)
print("Root found in [%.2f,%.2f] after %d iterations:" % (a, b, loops))
print("f(%.6f) = %.6f" % (root, f(root)))
