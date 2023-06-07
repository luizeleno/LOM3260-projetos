# Modelo de Debye para a capacidade térmica de sólidos

Usando a função `scipy.integrate.quad()` para integrar a função de Debye.

Mais detalhes sobre o problema em <https://computeel.org/LOM3260/material/exercicios/lista3.html#ex5>

A classe `debye.Debye` contém as funções necessárias à integração, em particular, o método `SpecificHeat()`.

O exemplo de interface com o usuário é o arquivo `main.py`. Ele cria um gráfico com três materiais.

Uma base de dados de temperaturas de Debye pode ser incluída de maneira semelhante a feito no projeto de Resfriamento de chapas.
