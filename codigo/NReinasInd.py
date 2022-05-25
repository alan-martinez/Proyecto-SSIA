from codigo.Individuo import Individuo

import numpy as np
import random as rnd

class NReinasInd ( Individuo ) :

    def __init__ ( self, nReinas : int = 0, initRandom : bool = True ) :
        Individuo.__init__( self, -1 )
        self.nReinas = nReinas
        if initRandom:
            base = np.array([ i for i in range(self.nReinas) ])
            self.genes = np.random.permutation ( base )
        else:
            self.genes = np.zeros ( self.nReinas, dtype = int )

    def __getitem__ ( self, index ):
        return self.genes[index]

    def __setitem__ ( self, index, value ) :
        self.genes[index] = value

    def __str__ ( self ) :
        res = '['
        for gene in self.genes:
            res += ' ' + str(gene) 
        return res + ' ]'

    def recombinar ( self, ind : Individuo, verbose : bool = False ) :
        individuos_recombinados = []

        corte = rnd.randint( 1, self.nReinas - 1 )

        if verbose :
            print('Corte: ', str(corte))
            print('Par a  : ', str(self))
            print('Par b  : ', str(ind))

        hijo_a = NReinasInd( self.nReinas, initRandom=False )
        hijo_b = NReinasInd( self.nReinas, initRandom=False )

        hijo_a[ :corte ] = self[ :corte ]
        hijo_a[ corte: ] = ind[ corte: ]

        posiciones_repetidas = []

        for i in range ( corte, self.nReinas ) :
            for j in range ( 0, corte ) :
                if hijo_a[i] == hijo_a[j] :
                    posiciones_repetidas.append(i)

        while len ( posiciones_repetidas ) > 0 :
            for i in range ( self.nReinas ) :
                if i not in hijo_a.genes :
                    index = posiciones_repetidas.pop()
                    hijo_a[index] = i

        hijo_b[ :corte ] = ind[ :corte ]
        hijo_b[ corte: ] = self[ corte: ]

        if verbose :
            print('Hijo a.: ', str(hijo_a))
            print('Hijo b.: ', str(hijo_b))
        
        posiciones_repetidas = []

        for i in range ( corte, self.nReinas ) :
            for j in range ( 0, corte ) :
                if hijo_b[i] == hijo_b[j] :
                    posiciones_repetidas.append(i)

        while len ( posiciones_repetidas ) > 0 :
            for i in range ( self.nReinas ) :
                if i not in hijo_b.genes :
                    index = posiciones_repetidas.pop()
                    hijo_b[index] = i

        if verbose :
            print('Hijo a.: ', str(hijo_a))
            print('Hijo b.: ', str(hijo_b))

        individuos_recombinados.append(hijo_a)
        individuos_recombinados.append(hijo_b)

        return np.array(individuos_recombinados)

    def mutar ( self ) :
        mutante = NReinasInd ( self.nReinas, initRandom=False )
        mutante.genes = self.genes
        index_a, index_b = rnd.randint( 0, self.nReinas - 1 ), rnd.randint( 0, self.nReinas - 1 )
        while index_a == index_b :
            index_a, index_b = rnd.randint( 0, self.nReinas - 1 ), rnd.randint( 0, self.nReinas - 1)
        mutante[ index_a ], mutante[ index_b ] = mutante[ index_b ], mutante[ index_a ]
        return mutante

    def getdisponible ( self )  :
        if self._disponible  == -1 :
            colisiones = 0

            for i in range ( self.nReinas ) :
                for j in range ( i + 1, self.nReinas ) :
                    if self[i] == self[j] :
                        colisiones += 1
                    if self[i] == ( self[j] - abs( j - i ) ) :
                        colisiones += 1
                    if self[i] == ( self[j] + abs( j - i ) ) :
                        colisiones += 1
            
            self._disponible  = colisiones
            
        return self._disponible 