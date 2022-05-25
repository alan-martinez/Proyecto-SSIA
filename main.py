from codigo.FGA import FGA
from codigo.NReinasIndFactory import NReinasIndFactory
from codigo.Tablero import Tablero

import argparse

parser = argparse.ArgumentParser(description='FGA para resolver el problema de N-Reinas', add_help=False)

num_pop = 20
num_elite = 2
num_rainhas = 8
num_ger = 1000
verbose = True
print_result = True
gerar_imagem = False

# Criando interface de argumentos
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Muestra este mensaje y sal.')
parser.add_argument('-np', '--num-pop', action='store', nargs=1, help='Número de individuos en la población.')
parser.add_argument('-ne', '--num-elite', action='store', nargs=1, help='Número de individuos seleccionados por elitismo.')
parser.add_argument('-ng', '--num-ger', action='store', nargs=1, help='Número máximo de generaciones que se ejecutará el FGA.')
parser.add_argument('-nr', '--num-rainhas', action='store', nargs=1, help='Número de reinas que se colocarán.')
parser.add_argument('-v', '--verbose', action='store_false', help='Si pasa, omita el número y mejor individuo de cada generación, así como su calificación')
parser.add_argument('-im', '--gerar-imagem', action='store_true', help='Si se pasa, genera un html con la imagen del tablero y se abre en el navegador.')

args = parser.parse_args()

if args.num_pop :
    num_pop = int(args.num_pop[0])
if args.num_elite :
    num_elite = int(args.num_elite[0])
if args.num_rainhas :
    num_rainhas = int(args.num_rainhas[0])
if args.num_ger :
    num_ger = int(args.num_ger[0])
if args.gerar_imagem :
    gerar_imagem = args.gerar_imagem
if args.verbose :
    verbose = args.verbose

FGA.executar ( nPop=num_pop,
               nGeracoes=num_ger,
               nElite=num_elite,
               indFactory=NReinasIndFactory(num_rainhas),
               verbose=verbose,
               printResult=print_result,
               gerarHtml=gerar_imagem )

