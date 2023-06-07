# Resfriamento de chapas finas

Usando o método das diferenças finitas com condições de contorno periódicas e de isolamento.

A classe `simulation.DiffFin` implementa o método. Ela requer outras classes, como `simulation.geometry`, `simulation.Diffstamping`, `simulation.mesh` e `simulation.convextion`, responsáveis por cada uma das etapas da montagem (*setup*) da simulação.

A classe `select_material.material_database` permite o uso de um arquivo excel para escolher o material da chapa. Ele é escolhido pelo método `select_material.material_database.select()`.

A interface com o usuário é o arquivo `main.py`. Ela constroi uma janela gráfica com 4 painéis (com `matplotlib.pyplot.add_subplot()`), com um material diferente submetido às mesmas condições. A janela reconhece cliques com o botão esquerdo do mouse, que continua e pausa a simulação alternadamente a cada clique.
