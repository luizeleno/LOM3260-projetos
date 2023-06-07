#https://realpython.com/mandelbrot-set-python/

# A naive solution - very slow!!!

import numpy as np
import matplotlib.pyplot as plt

NITERMAX = 40
N = 200

mandel = np.zeros((N, N))
cx = np.linspace(-2, .5, N)
cy = np.linspace(-1.5, 1.5, N)

for i in range(N):
    for j in range(N):
        c = cx[i] + cy[j] * 1j
        nz = 0j
        while np.absolute(nz) < 2 and mandel[j, i] < NITERMAX:
            # print(i, j)
            nz = nz ** 2 + c
            mandel[j, i] += 1

plt.figure()
plt.imshow(mandel, origin='lower', cmap='jet')
plt.colorbar()
plt.show()

