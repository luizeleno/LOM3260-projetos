import select_fluid

fluid_name = input("Qual é o fluido? ")

db = select_fluid.fluid_database('fluidos.xls')

try:
    fluido = db.select(fluid_name)
except KeyError:
    print('Não conheço esse fluido')
    raise

print(fluido.h)
