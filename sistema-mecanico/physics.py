import numpy as np
from scipy.integrate import odeint

g = 9.81 # acceleration of gravity (m/s²)

class DoublePendulum:
    
    def __init__(self, L1=1, L2=.5, m1=.3, m2=1):

        # Lenghts (m) and masses (kg)
        self.L1, self.L2 = L1, L2
        self.m1, self.m2 = m1, m2

    def deriv(self, y, t):
        '''Returns the 1st-order ODEsin theta1, z1, theta2, z2.'''
        
        L1, L2 = self.L1, self.L2
        m1, m2 = self.m1, self.m2
        M = m1 + m2
        L = L1 + L2
        
        theta1, z1, theta2, z2 = y

        s1, s2 = np.sin(theta1), np.sin(theta2)
        c12, s12 = np.cos(theta1-theta2), np.sin(theta1-theta2)
        D = m1 + m2*s12**2
        
        theta1dot = z1
        z1dot = (m2 * g * s2 * c12 - m2 * s12 * (L1 * z1**2 * c12 + L2 * z2**2) - M * g * s1) / L1 / D
        theta2dot = z2
        z2dot = (M * (L1 * z1**2 * s12 - g * s2 + g * s1 * c12) + m2 * L2 * z2**2 * s12 * c12) / L2 / D
        return theta1dot, z1dot, theta2dot, z2dot

    def calc_E(self, y):
        '''
            Returns the total energy of the system
        '''
        
        L1, L2 = self.L1, self.L2
        m1, m2 = self.m1, self.m2
        M = m1 + m2
        
        self.L = L1 + L2

        y = np.array(y)
        th1, th1d, th2, th2d = y.T
        V = -M * L1 * g * np.cos(th1) - m2 * L2 * g * np.cos(th2)
        T = 0.5 * m1 * (L1 * th1d)**2 + 0.5 * m2 *((L1*th1d)**2 + (L2*th2d)**2 + 2 * L1 * L2 * th1d * th2d * np.cos(th1-th2))
        return T + V

    def solve(self, y0=[np.pi/2, 0, np.pi/2, 0], tmin=0, tmax=30, dt=.01, TOL=1.e-10):
        
        L1, L2 = self.L1, self.L2
        m1, m2 = self.m1, self.m2

        # times to solve the EDO (s).
        t = np.arange(tmin, tmax+dt, dt)

        # Numerical integration of the equations of motion
        # Initial conditions: theta1, dtheta1/dt, theta2, dtheta2/dt
        y = odeint(self.deriv, y0, t, rtol=TOL)

        # Check the conservation of energy to within a defined tolerance
        EDRIFT = 0.01
        # Total energy total from the initial conditions
        self.E0 = self.calc_E(y0)
        if np.max(np.abs(self.calc_E(y) - self.E0)) > EDRIFT:
            raise(f'Maximum energy drift of {EDRIFT} exceeded.')

        # theta1 and theta2 as functions of time
        theta1, theta2 = y[:, 0], y[:, 2]

        # Converting to cartesian coordinates
        x1 = L1 * np.sin(theta1)
        y1 = -L1 * np.cos(theta1)
        x2 = x1 + L2 * np.sin(theta2)
        y2 = y1 - L2 * np.cos(theta2)

        return t, x1, y1, x2, y2
