# Resolviendo N-Queens con Algoritmo Genético

Trabajo de la disciplina Inteligencia Artificial (2020) de la clase de Ingeniería Informática CEFET-MG. Hecho en **Python3**

## Como correr

Para ejecutar el software, primero debe instalar las dependencias. La única dependencia de este programa es `numpy`. Así que simplemente instálalo con `pip` así:

```
pip instalar numpy
```

Para ejecutar, simplemente llame al programa de esta manera:

```
python3 principal.py
```

### Interfaz de línea de comandos

El programa se hizo para que los parámetros se pasen a través del argumento de la línea de comandos. Los argumentos se pasan en este formato:

```
uso: main.py [-h] [-np NUM_POP] [-ne NUM_ELITE] [-ng NUM_GER]
               [-nr NUM_RAINHAS] [-v] [-im]

FGA para resolver el problema de N-Queens

argumentos opcionales:
  -h, --help Imprime este mensaje y sale.
  -np NUM_POP, --num-pop NUM_POP
                        Número de individuos en la población.
  -ne NUM_ELITE, --num-elite NUM_ELITE
                        Número de individuos seleccionados por elitismo.
  -ng NUM_GER, --num-ger NUM_GER
                        Número máximo de generaciones que se ejecutará el FGA.
  -nr NUM_REINAS, --num-reinas NUM_REINAS
                        Número de reinas que se colocarán.
  -v, --verbose Si pasa, omita el número y el mejor individuo de
                        cada generación así como su evaluación
  -im, --generate-image Si se pasa, genera un html con la imagen del tablero y
                        se abre en el navegador.

```

### Ejemplo:

- `python main.py -np 40 -ne 8 -ng 2000 -nr 12 -im`. El código correrá con una población de 40 individuos, 8 élites, 2000 generaciones y 12 reinas, generando al final la imagen del tablero resuelto si converge el FGA.

- `python main.py -np 20 -ne 2 -ng 100 -nr 8`. El código se ejecutará con una población de 20 individuos, 2 élites, 100 generaciones y 8 reinas.

- `Python principal.py`. El código se ejecutará con una población de 20 individuos, 2 élites, 1000 generaciones y 8 reinas.

### Tablero generado:

<img ancho=500 src='./activos/tabuleiro.png'>

-----

Autor: [Leonam Teixeira de Vasconcelos](https://leonamtv.github.io/leonamtv/)