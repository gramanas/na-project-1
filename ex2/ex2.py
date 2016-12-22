from numpy import *
import numpy

from scipy import *
import scipy

import random
  
import matplotlib.pyplot as plt

def f(t):
  return 94*cos(t)**3 - 24*cos(t) + 177*sin(t)**2 - 108*sin(t)**4 - 72*(cos(t)**3)*(sin(t)**2) - 65

def f_der(t):
  return (3/2)*(sin(t)+6*sin(2*t)-15*sin(3*t))*((1-2*cos(t))**2)

def f_der_2(t):
  return -(3/2)*(2*cos(t) - 1)*(cos(t) + 24*cos(2*t) - 69*cos(3*t) + 75*cos(4*t) + 1)

t = arange(0,3.001,step=.001)

plt.plot(t, f(t), c='r')
#plt.plot(t, f_der(t), c='g')
#plt.plot(t, f_der_2(t), c='b')
plt.grid(True)
plt.show()

def bisect(a, b):
  a_1, b_1 = a, b
  root = random.uniform(a, b)

  # number of times to repeat to achieve 6 points accuracy
  N = int(ceil((log(b - a) - log(0.0000005)) / log(2)))

  for i in range(0, N):
    if (f(a) < 0 and f(root) > 0) or (f(a) > 0 and f(root) < 0):
      b = root
    elif (f(b) < 0 and f(root) > 0) or (f(b) > 0 and f(root) < 0):
      a = root
    root = random.uniform(a, b)

  return root, N, a_1, b_1

def new_raph(start):
  temp_l = [start, start - (f(start)/f_der(start))
            - (1/2)*((f(start)**2)*f_der_2(start))/(f_der(start)**3)]

  N = 1
  while 0.0000005*abs(temp_l[N]) < abs(temp_l[N-1] - temp_l[N]):
    temp =  temp_l[N] - (f(temp_l[N])/f_der(temp_l[N]))
    - (1/2)*((f(temp_l[N])**2)*f_der_2(temp_l[N]))/(f_der(temp_l[N])**3)
    temp_l.append(temp)
    N = N + 1

  root = temp_l[N] 

  #N-1 because the N=N+1 happens at the very end of the while loop
  return root, N - 1, start

def intersection(a, b, c):
  x = [a, b, c]

  N = 0
  while 0.0000005*abs(x[N%3]) < abs(x[N%3] - x[(N-1)%3]):
    r = f(x[(N+2)%3])/f(x[(N+1)%3])
    q = f(x[(N)%3])/f(x[(N+1)%3])
    s = f(x[(N+2)%3])/f(x[(N)%3])
    tmp = x[(N+2)%3] - (r*(r - q)*(x[(N+2)%3]-x[(N+1)%3])+(1 - r)*s*(x[(N+2)%3] - x[(N)%3]))/(q - 1)*(r - 1)*(s - 1)
    x[N%3] = tmp
    N = N + 1

  root = x[(N)%3]

  #N-1 for the same reason as the N-R method
  return root, N - 1, a, b 

#############
# Bisection #
#############
print("\n++++ Bisection ++++\n")

root, loops, a, b = bisect(0.8,0.9)
print("Root in [%.2f,%.2f] after %d loops: f(%.6f) = %.6f\n"
      % (a, b, loops, root, f(root)))

root, loops, a, b = bisect(0.95,1.10)
print("Root in [%.2f,%.2f] after %d loops: f(%.6f) = %.6f\n"
      % (a, b, loops, root, f(root)))

root, loops, a, b = bisect(2.3,2.8)
print("Root in [%.2f,%.2f] after %d loops: f(%.6f) = %.6f"
      % (a, b, loops, root, f(root)))

####################
# Newton - Raphson #
####################
print("\n++++ Newton - Raphson ++++\n")

root, loops, start = new_raph(0.8)
print("Starting at %.2f:\nafter %d iterations the root is: f(%.6f) = %.6f\n"
      % (start, loops, root, f(root)))
  
root, loops, start = new_raph(1)
print("Starting at %.2f:\nafter %d iterations the root is: f(%.6f) = %.6f"
      % (start, loops, root, f(root)))

root, loops, start = new_raph(2.5)
print("Starting at %.2f:\nafter %d iterations the root is: f(%.6f) = %.6f"
      % (start, loops, root, f(root)))

#################
# Interpolation #
#################
print("\n++++ Interpolation ++++\n")

root, loops, a, b = intersection(0,1,2)
print("Root found in [%.2f,%.2f] after %d iterations:" % (a, b, loops))
print("f(%.6f) = %.6f\n" % (root, f(root)))

# root, loops, a, b = intersection(1.7,2.1)
# print("Root found in [%.2f,%.2f] after %d iterations:" % (a, b, loops))
# print("f(%.6f) = %.6f" % (root, f(root)))


