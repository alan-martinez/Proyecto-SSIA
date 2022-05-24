from core.IndividuoFactory import  IndividuoFactory
from core.NReinasInd import NReinasInd

class NRainhaIndFactory ( IndividuoFactory ) :

    def __init__ ( self, nRainhas : int ) :
        self.__nRainhas = nRainhas

    def getNRainhas ( self ):
        return self.__nRainhas

    def getIndividuo ( self ) :
        return NReinasInd(self.__nRainhas)