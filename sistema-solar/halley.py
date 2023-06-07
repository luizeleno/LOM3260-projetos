import ephem

# cometa Halley - dados da Wikipedia
# https://en.wikipedia.org/wiki/Halley%27s_Comet

def create():
    halley = ephem.EllipticalBody()
    halley._inc = 161.96
    halley._om = 112.05
    halley._Om = 59.396
    halley._a = 17.866
    halley._M = 0.07323
    halley._e = 0.96658
    halley_epoch_M = '2061-08-04'
    halley_epoch = '2061-08-04'
    halley.name = 'Cometa Halley'
    return halley
