# Visualização do fractal de Mandelbrot

Usando *arrays* em `numpy` para acelerar os cálculos com números complexos.

O código `mandelbrot-naive.py` é uma primeira abordagem, ingênua, para a obtenção do fractal. Foi baseada no código encontrado em <https://realpython.com/mandelbrot-set-python/>. É mantda aqui por razões históricas, mas não é necessária para o pacote.

Por outro lado, o arquivo `mandelbrot.py` é um módulo mais inteligente, fazendo uso de máscaras com `numpy.where()` para evitar cálculos desnecessários. Com isso, agiliza-se bastante as operações e o tamanho dos arrays complexos que é possível tratar para a mesma configuração de processador e de memória.

A classe `mandelbrot.GUI` fornece uma interface gráfica para visualizar e explorar o fractal de Mandelbrot. Os parâmetros de inicialização são:

1. N: tamanho da malha de NxN valores no plano complexo (padrão: 750)
2. NITERMAX: número máximo de iterações antes de decidir se um número faz parte do fractal (padrão:250)
3. xlim: limites iniciais do eixo real (padrão: (-2, .5))
4. ylim: limites iniciais do eixo imaginário (padrão: (-1.5, 1.5))

Criada a interface gráfica, o controle é feito arrastando o mouse com  obotão esquerdo pressionado, criando uma nova área que será ampliada. Os botões na parte inferior da interface voltam um passo ou reinicializam para a condição inicial.

O arquivo `main.py` é a interface com o usuário.
