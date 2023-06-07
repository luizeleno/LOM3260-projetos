import pandas

class material:

    def __init__(self, k=398, rho=8970, cp=380, name='material'):

        self.name = name
        self.k, self.rho, self.cp = k, rho, cp
        self.a = k / rho / cp

class material_database:

    def __init__(self, xls='materiais.xls'):

        self.dataframe = pandas.read_excel(xls, index_col='Material')

    def select(self, name):

        try:

            k = self.dataframe.loc[name, 'k']
            rho = self.dataframe.loc[name, 'rho']
            cp = self.dataframe.loc[name, 'cp']
            return material(k, rho, cp, name)

        except KeyError as key:

            print(f'*** KeyError: unknown material ({key}) ***')
            raise
