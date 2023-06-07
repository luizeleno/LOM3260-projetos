import pandas

class material:

    def __init__(self, TD=2500, name='meu material'):

        self.name = name
        self.TD = TD
        
class material_database:

    def __init__(self, xls='materiais.xls'):

        self.dataframe = pandas.read_excel(xls, index_col='Material')

    def select(self, name):

        try:

            TD = self.dataframe.loc[name, 'TD']
            return material(TD, name)

        except KeyError as key:

            print(f'*** KeyError: unknown material ({key}) ***')
            raise
