# Simulação de um pêndulo duplo

Usando `scipy.integrate.odeint` para a solução numérica das equações do movimento.

O módulo `physics.py` contém a classe `DoublePendulum`, responsável pela simulação.  Ela é chamada com os argumentos `L1`, `L2`, `m1` e `m2` (comprimentos e massas dos pêndulos, com `L2` e `m2` relativos à parte inferior do pêndulo)

São duas interfaces com o usuários:

1. `pendulo-duplo-matplotlib.py`: usa o `matplotlib` para a animação. Neste caso, mostra também a trajetória da parte inferior do pêndulo.
2. `pendulo-duplo-vpython.py`: faz a animação em `vpython`. O usuário está livre para adicionar quaisquer elementos do `vpython` que desejar.
