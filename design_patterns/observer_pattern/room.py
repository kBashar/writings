from subject import Subject
from observer import Observer


class Room(Subject):

    def __init__(self):
        self._observers = list()

        self._number_of_persons = 0
        print("Initiated an empty room!")

    def addObserver(self, observer: Observer):
        self._observers.append(observer)

    def removeObserver(self, observer: Observer):
        self._observers.remove(observer)

    def notifyObservers(self):
        for observer in self._observers:
            observer.update()

    # class specific methods

    def setPerson(self, person: int):
        self._number_of_persons = person

        # state has changed lets notify the observers
        self.notifyObservers()

    def getPerson(self):
        return self._number_of_persons
