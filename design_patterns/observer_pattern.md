It is a common scenario, Where in a system one object changes and other objects are interested to know about that change. Examples are avadant in software systems. 
For our ease of discussion let's name these objects first. Objects that are interested to know about the change are called `observers` and interesting objects can be called `Observable`. In books and literature about design patterns this `observable` is also called `subject`. So, `Observers` observe the change of state in `Subject`. We can see this is an one-to-many relation, where subject's change is propagated to many observers. 

Lets study some example scenario where we are most likely to use the observer pattern. 

### Example Scenarios

 For example, applications now have at least three choices in application theme change plane, "Light", "Dark" and "System". If an application has its theme set to `system` it would definitly like to know when user changes the theme in host(where the application lives on) operating system. 
 I personally prefer to select `system` as theme in applications, to get an uniform UX across apps. So, when I change the theme from OS settings, definitly most of my applications would like to know that. 

If we align this scenario with our previously mentioned nomencuture, here applications that wants to know about theme change are **`observers`** and the host Operating System's theme configuration object is observable or **`Subject`**.

We can think of the OTPs coming to our phone inbox. My bank app sends me an OTP and as soon as the message arrives it collects that OTP on its own and fill up the security code. So definitly my app gets notified by the OS on new message arrival. And this is not special for bank apps, all kinds apps have this nice automated message reading and form fill up feature. 

We see interested applications are notified on the state change of the message inbox. Here, message box is **`Subject`** and the apps that are waiting for their own OTP messages are **`observers`**.

Now, let's consider an E-Commerce dashboard, It hosts many numbers and matrices indicating the business state at any time in diferent display cards. Among others one display card shows the total Order count, another shows the average expense amount per parchase And maybe another to show the sales trending based on hourly sales data. 
So, all three of these display cards are dependent on the sales count, i.e. whenever there is a new sale/order the value in these cards should be updated. In line with our two prvious examples, we can say three dsiplay cards **total order count**, **average revenue per order** and **sales stat** are **`observers`** and they are observing **`Subject`** **sales count** object. 

Imagine a Smart Home system where different smart devices (thermostats, security cameras, lights, etc.) interact with a central hub. This hub monitors various environmental factors like motion, temperature, or door locks. We will later code this example to demonastrate the observer design pattern some section below.

Let's take a Smart Door Lock as the Subject and other smart devices as Observers. Whenever the door is locked or unlocked, certain devices are interested in this change:

* Security Cameras might activate when the door is unlocked.
* Smart Lights could turn off automatically when the door is locked and no one is home.

In this case:

* Smart Door Lock is the **Subject**.
* Devices like the Cameras, and Lights are **Observers** that need to update their behavior based on the door's status.


Now that we have built the intuition how the **`observers`** and **`subject`** look like, lets find out how they interact. 

### How to update Observers on state change of Subject

Question is how do we let **`observers`** know the state of the **`Subject`** has changed?

Do we poll at an interval to check if the object's state has changed or do we push the update to the interested objects whenever there is a change. 

Polling makes sense in some scenario but at most of cases pushing is a better option. Because, imagine parts of our application continuously polling other parts of the application for data change where data changes rarley or in irregualr interval. This might be potential waste of our resources. Rather a better approch will be **`Subject`** notifies its observers whenever there is a change in its state. 

Observer pattern mainly suggests us a code organization that let **`Subject`** notify its **`Observers`** about state changes without knowing much about the **`Observer`** class or its internals. Both **`Subject`** and **`Observers`** implement certain interfaces and they communicate to each other through those interfaces. 

### Class Diagram

Observer patterns UML class diagram will clearify the relation and interaction more. Lets take a look. 


![Observer pattern UML class diagram][def]


We have two interfaces **Subject** and **Observer**. Other classes are concrete implementation of these Interfaces e.g. ConcreteSubject and ConcreteObserver. While Interfaces will provide us with a blueprint, concrete implementation of these interfaces will actually implement the methods of the Interface.

**Subject** has one attribute and three methods. While the attribute **`observers`** is a list of **Observer** instances, the methods do followings
1. **`addObserver`**: let an observer register itself for notifications from the **Subject**. After an **Observer** being added to the subjects observer list it will be notfied on the state changes of the **Subject**.
2. **`removeObserver`**: if the observer does not want to listen to the changes of the **Subject**, it can remove itself from the list of observers and it will not be bothered anymore.
3. **`notifyObservers`**: the function that will do the work of notifying the subject's **observers**.

Any and all classes that want to act as a **Subject** will implement above methods. 

Now lets consider the **Observer** interface. It has one method **`update`**. Concrete observer classes will have to implement this method.

1. **update**: this method will be called from the **Subject**'s **`notifyObservers`** method to let the observer know of a data/state change in **Subject**. This is our channel of notification. More 


### Example Code for Observer pattern

So, our examples will be in python. Python doesn't have the idea of Interface. We can achieve the same using its Abstract Class concept. A brief on abstract class is [here]() and you may check this. We will skip Abstract class related discussion here. 

So, first we will design our **`Subject`** and **`Observer`** Interfaces aka Abstract classes. 

```python 
from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self):
        pass


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

```
These classes are blueprint for our concrete classes. All abstract methods will be implemented there. 

Our goal is to design a smart home system that will have rooms with security camera and lights. These light and camera will be responsive to the presence of human in the room. If there is human in the room the camera will start monitoring while light will be lighting. So, both Camera and light are interested to know when there is a change in number of persons in the room. 

From above discussion it might be already clear to us observers are **`Light`** and **`Camera`**. And they will observe the state of the room. **`Room`** is our subject. Whenever state of the room changes, light and camera will be notified. 

Let's implement these class in accordance with the abstract classes we have defined earlier. The implementation is kept simple and comments are added. Hope this will be easy to follow.

```python

class Room(Subject):

    def __init__(self):
        self._observers = list()  # initialize the observers list

        self._number_of_persons = 0  # initialize the room with no person inside the room.
        print("Initiated an empty room!")

    def addObserver(self, observer: Observer):  # adds observer to the list
        self._observers.append(observer)

    def removeObserver(self, observer: Observer): # removes observer from the list
        self._observers.remove(observer)

    def notifyObservers(self):  # iterate through all listed observers and call their update method to notify them. 
        for observer in self._observers:
            observer.update()

    # class specific methods

    def setPerson(self, person: int):
        self._number_of_persons = person

        # state has changed lets notify the observers
        self.notifyObservers()

    def getPerson(self):
        return self._number_of_persons

```

Apart from implementing 3 methods (`addObserver`, `removeObserver` and `notifyObservers`) from the **`Subject`** abstract class it has two extra methods i.e. `setPerson` and `getPerson`. These methods let outside code update or fetch the state of the **`Room`**. These are not mandatory for the pattern but necessary for the class to function in our context.


Now let's code observers. We have two observers `Light` and `Camera` classes, that will need to first register themselves to the Room subject and implement the **`update`** method logic to response to the change in state of the room. 

```python
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
```


```python
class SecurityCamera(Observer):
    def __init__(self, room: Room):
        print("Initializing Security Camera!")
        self._room = room

        # register itself for door state change observation
        self._room.addObserver(self)

    def update(self):
        # state of the room has changed
        number_of_persons = self._room.getPerson()

        # take some actions based on changed states
        if number_of_persons == 0:
            print(f"Camera: Shutting down. {number_of_persons} persons in the room.")
        else:
            print(f"Camera: Keep running. {number_of_persons} persons in the room.")
```  

Now lets add the calling code. For demonastration purpose we will put this code in main calling thread. 
First we initialize the **`Room`** instance and with that instance initialize the **`Light`** and **`SecurityCamera`** instances. To update the the number of persons in the room we call `room.setState()` method and in turn this will notify and update the state of `light` and `camera`. 

```python

if __name__ == "__main__":
    room = Room()

    light = Light(room)
    camera = SecurityCamera(room)

    room.setPerson(1)
    room.setPerson(0)
    room.setPerson(5)
    room.setPerson(2)

```

Upon running the code output will be like following

```
Initiated an empty room!
Initializing Lights!
Initializing Security Camera!
Light: Keep running. 1 persons in the room.
Camera: Keep running. 1 persons in the room.
Light: Shutting down. 0 persons in the room.
Camera: Shutting down. 0 persons in the room.
Light: Keep running. 5 persons in the room.
Camera: Keep running. 5 persons in the room.
Light: Keep running. 2 persons in the room.
Camera: Keep running. 2 persons in the room.
```

Full code is available here in [this github repo](https://github.com/kBashar/writings/tree/main/design_patterns/observer_pattern).


[def]: ./imgs/observer_class_diagram.png



