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

  N = 0
  while round(f(root),6) != 0:
    if (f(a) < 0 and f(root) > 0) or (f(a) > 0 and f(root) < 0):
      b = root
    elif (f(b) < 0 and f(root) > 0) or (f(b) > 0 and f(root) < 0):
      a = root
    root = random.uniform(a, b)
    N = N +1

  return root, N, a_1, b_1

def new_raph(start):
  temp_l = [start, start - (f(start)/f_der(start))
            - (1/2)*((f(start)**2)*f_der_2(start))/(f_der(start)**3)]

  N = 1
  while round(f(temp_l[-1]),6) != 0:
    temp =  temp_l[N] - (f(temp_l[N])/f_der(temp_l[N]))
    - (1/2)*((f(temp_l[N])**2)*f_der_2(temp_l[N]))/(f_der(temp_l[N])**3)
    temp_l.append(temp)
    N = N + 1

  root = temp_l[-1] 

  return root, N, start

def interpolation(a, b, c):
  x = [a, b, c]

  N = 0
  root = x[0]
  while round(f(root),6) != 0:
    r = f(x[(N+2)%3])/f(x[(N+1)%3])
    q = f(x[(N)%3])/f(x[(N+1)%3])
    s = f(x[(N+2)%3])/f(x[(N)%3])
    tmp = x[(N+2)%3] - (r*(r - q)*(x[(N+2)%3]-x[(N+1)%3]) +
                        (1 - r)*s*(x[(N+2)%3] - x[(N)%3]))/((q - 1)*(r - 1)*(s - 1))
    x[N%3] = tmp
    N = N + 1
    root = x[(N)%3]

  return root, N - 1, a, b, c

#############
# Bisection #
#############
print("\n++++ almost-Bisection ++++\n")

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
print("\n++++ almost-Newton - Raphson ++++\n")

root, loops, start = new_raph(0.8)
print("Starting at %.2f:\nafter %d iterations the root is: f(%.6f) = %.6f\n"
      % (start, loops, root, f(root)))
  
root, loops, start = new_raph(1)
print("Starting at %.2f:\nafter %d iterations the root is: f(%.6f) = %.6f\n"
      % (start, loops, root, f(root)))

root, loops, start = new_raph(2.5)
print("Starting at %.2f:\nafter %d iterations the root is: f(%.6f) = %.6f"
      % (start, loops, root, f(root)))

#################
# Interpolation #
#################
print("\n++++ almost-Interpolation ++++\n")

root, loops, a, b, c = interpolation(1,2,3)
print("Starting points: [%.2f, %.2f, %.2f]. After %d iterations:" % (a, b, c, loops))
print("f(%.6f) = %.6f\n" % (root, f(root)))

root, loops, a, b, c = interpolation(.7,.8,.9)
print("Starting points: [%.2f, %.2f, %.2f]. After %d iterations:" % (a, b, c, loops))
print("f(%.6f) = %.6f\n" % (root, f(root)))

root, loops, a, b, c = interpolation(2.2,2.3,2.4)
print("Starting points: [%.2f, %.2f, %.2f]. After %d iterations:" % (a, b, c, loops))
print("f(%.6f) = %.6f\n" % (root, f(root)))

for i in range(10):
  root, loops, a, b = bisect(0,3)
  print("%d: Root in [%.2f,%.2f] after %d loops: f(%.6f) = %.6f"
        % (i, a, b, loops, root, f(root)))

