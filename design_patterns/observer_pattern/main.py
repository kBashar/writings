from room import Room
from light import Light
from camera import SecurityCamera

if __name__ == "__main__":
    room = Room()

    light = Light(room)
    camera = SecurityCamera(room)

    room.setPerson(1)
    room.setPerson(0)
    room.setPerson(5)
    room.setPerson(2)
