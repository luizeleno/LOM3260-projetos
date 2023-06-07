import pandas

class fluid:

    def __init__(self, h=10000, name='água corrente'):

        self.name = name
        self.h = h

class fluid_database:

    def __init__(self, xls='fluids.xls'):

        self.dataframe = pandas.read_excel(xls, index_col='Fluido')

    def select(self, name):

        try:

            h = self.dataframe.loc[name, 'h']
            return fluid(h, name)

        except KeyError as key:

            print(f'*** KeyError: unknown fluid ({key}) ***')
            raise
