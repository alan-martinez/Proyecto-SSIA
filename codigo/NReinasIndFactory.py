from codigo.IndividuoFactory import  IndividuoFactory
from codigo.NReinasInd import NReinasInd

class NReinasIndFactory ( IndividuoFactory ) :

    def __init__ ( self, nRainhas : int ) :
        self.__nReinas = nRainhas

    def getNRainhas ( self ):
        return self.__nReinas

    def getIndividuo ( self ) :
        return NReinasInd(self.__nReinas)