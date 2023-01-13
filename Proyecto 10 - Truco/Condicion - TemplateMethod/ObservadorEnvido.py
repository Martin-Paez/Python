from Canto import Canto
from abc import ABCMeta, abstractmethod

class ObservadorEnvido (metaclass = ABCMeta):

    @abstractmethod
    def envidoCantado(self):
        pass