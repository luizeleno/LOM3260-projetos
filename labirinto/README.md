### 6. Solução de labirintos

Usando a estratégia delineada em <https://computeel.org/LOM3260/material/exercicios/lista1.html#ex31>

A interface com o usuário é o arquivo `main.py`, que usa a classe `MAZEGUI` do módulo `GUI`.

Os parâmetros para MAZEGUI são:
1. nx (int): altura do labirinto (padrão: 25)
1. ny (int): altura do labirinto (padrão: 25)
1. mouse (2 int tuple): posição da entrada
1. cheese (2 int tuple): posição da saída
1. slow (bool): traçar lentamente a marcação e a solução (padrao: False)
