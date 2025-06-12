import numpy as np
import matplotlib.pyplot as plt

def b(n):#coeffecients of sine
  return 2*(1-(-1)**n)/(np.pi*n)

def sqr_wave_approx(t, n):
  sum = 0
  for i in range(n+1):
    if i%2 != 0:
      sum += b(i)*np.sin(i*t)
  return sum

def sqr_wave_true(t):
  t = t % (2*np.pi)
  return np.where(t < np.pi, 1, -1)

t = np.linspace(-np.pi, np.pi, 100000)
plt.plot(t, sqr_wave_true(t), label = 'Actual function')

for i in (1000, 2000, 3000):
  plt.plot(t, sqr_wave_approx(t, i), label = f'{i} terms')


plt.axvline(x = .001, ls = '--')  
plt.grid()
plt.legend()
plt.show()
