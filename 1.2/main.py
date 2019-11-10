# Grundlagen der elektrischen Messtechnik
# Abgabe 1

import numpy as np
from numpy import pi

# 1.2.1

x = np.linspace(1, 1000, num=1000)
x = np.arange(1, 1000)

# 1.2.2

# Mittels list comprehension
x2 = x[(x >= 10) & (x <= 50)]

# 1.2.3
# Da x2 eine Kopie ist wird x nicht modifiziert:

print(x[0])
x2[0] = 0
print(x[0])

# 1.2.4

y = np.arange(start=0.2, stop=200.0, step=0.2)
skalarprod = np.dot(x, y)

# 1.2.5

elementweise = x * y

# 1.2.6

sumx = np.sum(x)

# 1.2.7

randmtrx = np.random.rand(3, 4)

# 1.2.8

extmtrx = np.append(randmtrx, [np.repeat(1,4)], 0)

# 1.2.9

transp = np.transpose(extmtrx)
invers = np.linalg.inv(extmtrx)
determ = np.linalg.det(extmtrx)

# 1.2.10

f = 50
n = 30
t = np.linspace(0, 1/f, n)
y = np.sin(t * f * n * 2 * pi) * 5

# 1.2.11

import matplotlib.pyplot as plot

plot.plot(t, y)
plot.xlabel("Zeit")
plot.ylabel("Spannung")

# 1.2.12

maxidx = np.argmax(y)
maxtime = t[maxidx]

plot.plot(maxtime, y[maxidx], 'rx', markersize=14)

plot.show()

# 1.2.13

np.save("t", t)
np.save("y", y)

# test:

t_load = np.load("t.npy")
y_load = np.load("y.npy")

assert(np.array_equal(t_load, t))
assert(np.array_equal(y_load, y))

# 1.2.14

p, (a1, a2) = plot.subplots(2)

a1.plot(t, y)
a1.plot(maxtime, y[maxidx], 'rx', markersize=14)
a1.grid(True)

noise = np.random.randn(n)
a2.plot(t, noise)
a2.grid(True)

plot.show()

# 1.2.15

p.savefig("out.pdf")
