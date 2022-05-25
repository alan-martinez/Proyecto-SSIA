from abc import ABC, abstractmethod

class Individuo ( ABC ):

    def __init__ ( self, disponible : float = -1 ) :
        self._disponible = disponible

    @abstractmethod
    def recombinar ( self, ind ) -> list : 
        pass

    @abstractmethod
    def mutar ( self ) :
        pass

    @abstractmethod
    def getdisponible ( self ) -> float :
        pass