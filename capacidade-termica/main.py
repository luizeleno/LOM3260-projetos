import numpy as np
import debye as db
import matplotlib.pyplot as plt

# TODO: Interface para achar a TD, Tmin e Tmax


mat = db.Debye(TD)

NT = 0, 500, 501
T = np.linspace(Tmin, Tmax, NT)

plt.figure()

plt.xlabel('T (K)')
plt.ylabel('$c_v (J/K/mol)$')

plt.plot(T, mat.SpecificHeat(T), label=f'Chumbo ($\\theta_D={mat.TD}$K)')

plt.legend()
plt.show()
