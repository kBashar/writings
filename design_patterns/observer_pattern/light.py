from observer import Observer
from room import Room


class Light(Observer):

    def __init__(self, room: Room):
        print("Initializing Lights!")
        self._room = room

        # register itself for door state change observation
        self._room.addObserver(self)

    def update(self):

        # state of the room has changed
        number_of_persons = self._room.getPerson()

        # take some actions based on changed states
        if number_of_persons == 0:
            print(f"Light: Shutting down. {number_of_persons} persons in the room.")
        else:
            print(f"Light: Keep running. {number_of_persons} persons in the room.")
