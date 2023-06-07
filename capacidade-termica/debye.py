import numpy
import scipy.integrate

R = 8.31451  # universal gas constant (J/K/mol)

class Debye:
    '''
        use: 
            create instante of object: M = Debye(TD)
            TD: Debye temperature of selected material
        
            calculate specific heat: cv = M.SpecificHeat(T)
            
            T can be float, int or numpy.array
        
    '''

    def __init__(self, TDebye):
        self.TD = TDebye

    def I_D(self, u):
        expu = numpy.exp(u)
        return u**4 * expu / (expu - 1) ** 2

    def integral(self, x):
            # integral usind scipy.optimize method quad()
            I, err = scipy.integrate.quad(self.I_D, 0, x)
            return I

    def D(self, x):
        # numpy.vectorize() allows the use of non-scalar arguments, such as arrays
        I_vec = numpy.vectorize(self.integral)
        I = I_vec(x)
        return 9 / x**3 * I

    def SpecificHeat(self, T):
        x = self.TD / T
        return R * self.D(x)
