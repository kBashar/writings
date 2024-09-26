from abc import ABC, abstractmethod

from observer import Observer


class Subject(ABC):

    @abstractmethod
    def addObserver(self, observer: Observer):
        pass

    @abstractmethod
    def removeObserver(self, observer: Observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass
