from core.IndividuoFactory import IndividuoFactory
from core.Tablero import Tablero

import numpy as np
import random as rnd

class FGA :

    @classmethod
    def executar ( cls, 
                   nPop        : int, 
                   nGeracoes   : int, 
                   nElite      : int, 
                   indFactory  : IndividuoFactory,
                   verbose     : bool = False,
                   printResult : bool = True,
                   gerarHtml   : bool = False ) -> int :
        """
        Método estático que executa o FGA para o problema das N rainhas, onde:

        Parâmetros:
            - nPop       = (requerido) Número de individuos en la población
            - nGeneraciones  = (obligatorio) Número de generaciones que se ejecutará el software
                            cortar al máximo (si hay algún individuo que ya haya
                            al objetivo -- 0 colisiones, FGA deja de funcionar)
            - nElite     = (requerido) Número de individuos que aprobarán
                            la próxima generación.
            - indFactory = (obligatorio) Objeto de tipo IndividuoFactory, utilizado 
                            para generar la población base de cada generación.
            - verbose    = (opcional, por defecto es falso) Si es verdadero, imprime
                            el número y mejor individuo de cada generación así como
                            tu evaluación
            - printResult = (opcional, por defecto es verdadero) Si es verdadero, imprime el
                            resultado obtenido si el algoritmo converge a la condición
                            detener.
            - gerarHtml   = (opcional, por defecto es falso) Si es verdadero, genera un html
                            con el tablero del mejor individuo, si y cuando el algoritmo converge.

        Retorna: 
            Un número entero con el número de la generación en la que convergió el algoritmo. Si
            retorno es igual a -1, el FGA no ha convergido.
        """
        
        if verbose :
            print('executando...')

        # Cria a população inicial
        pop = np.array([ indFactory.getIndividuo() for _ in range(nPop) ])

        for g in range ( nGeracoes ) :
            filhos = []

            # Adicionando população inicial à lista de população total
            filhos.extend(pop)

            # Gerando nPop indivíduos recombinados
            for i in range ( 1, nPop, 2 ):
                filhos_recombinados = pop[i - 1].recombinar(pop[i])
                filhos.extend(filhos_recombinados)

            # Gerando nPop indivíduos mutantes            
            for i in range ( 0, nPop ):
                filhos.append(pop[i].mutar())

            def getAvaliacoes ( individuos ) :
                """
                Retorna uma lista de avaliações dos indivíduos
                """
                return [ individuo.getAvaliacao() for individuo in individuos ]

            # Ordena os filhos por ordem de avaliação
            filhos.sort ( key=lambda ind:ind.getAvaliacao())

            newPop = []

            if nElite > nPop :
                raise Exception('El número de élite debe ser menor que la población.')

            avaliacoes = getAvaliacoes ( filhos )

            def roleta_viciada ( ) :
                """
                Devuelve el índice de la ruleta adicta realizada bajo la lista de evaluación.
                """
                somatorio = sum ( 1. / i if i != 0 else 0 for i in avaliacoes )
                roleta = rnd.uniform( 0, somatorio )
                soma = 0.0
                i = 0
                while soma < roleta and i < len ( avaliacoes ) :
                    soma += avaliacoes[i]
                    i += 1
                return i if i < len ( avaliacoes ) else ( len( avaliacoes ) - 1 )
            
            if verbose :
                print(f'{bcolors.FAIL}Generacion {bcolors.BOLD}' 
                        + str(g + 1) + f'{bcolors.OKGREEN} | Mejor Ind. {bcolors.OKBLUE}' 
                        + str(filhos[0]) + f'{bcolors.OKGREEN} | aprobacion: {bcolors.OKBLUE}' 
                        + str(filhos[0].getAvaliacao()) + f'{bcolors.ENDC}' )

            # Adiciona a elite, removendo a da lista de filhos
            elitistas = filhos[:nElite]
            del filhos[:nElite]
            del avaliacoes[:nElite]
            newPop.extend(elitistas)

            # Adiciona individuos da lista de filhos utilizando a roleta
            # viciada até que o número de indivíduos seja atingido.
            while len(newPop) < nPop :
                i = roleta_viciada ()
                newPop.append(filhos[i])
                del filhos[i]
                del avaliacoes[i]

            pop = newPop
            
            # Checa se algum indivíduo possui avaliação 0 e para caso haja
            for aval, ind in zip ([ ind.getAvaliacao() for ind in pop ], pop ) :
                if aval == 0 :
                    if printResult :
                        print('------- Convergido -----------')
                        print('Generacion ' + str(g + 1) + f' | Mejor Ind.: {bcolors.OKGREEN}{bcolors.BOLD}' 
                              + str(ind) + f'{bcolors.ENDC} | aprobacion: ' + str(aval))
                        print('-----------------------------')
                    if gerarHtml :
                        tab = Tablero(ind)
                        pathToFile = tab.gerarImagem()
                        import webbrowser
                        webbrowser.open(pathToFile, new=2)
                    if verbose :
                        print('...ejecucion finalizada')
                    return g + 1
        if verbose :
            print('...ejecucion finalizada')
        
        return -1

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'