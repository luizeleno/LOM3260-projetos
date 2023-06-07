import mandelbrot

mandelbrot.GUI(N=750, NITERMAX=250, xlim=(-2, 1), ylim=(-1, 1))

#import numpy as np
#import matplotlib.pyplot as plt

#N = 201
#NITERMAX = 10
#c = .7885 * np.exp(np.pi / 2 * 1j)

#x = np.linspace(-1, 1, N)
#y = np.linspace(-1, 1, N)

#julia = np.zeros((N, N))

#for i in range(N):
    #for j in range(N):
        #z = x[i] + y[j] * 1j
        #for k in range(NITERMAX):
            #z = z * z + c
            #if np.absolute(z) > 2:
                #julia[i, j] += 1

#plt.figure()

#plt.imshow(julia)

#plt.show()
