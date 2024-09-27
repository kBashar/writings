# Observer pattern with Python

Observer pattern or some variations of it ubiquitious. In web frameworks, UI frameworks or event-driven programming systems use this pattern to bridge objects or to establish communication channel between objects. For developers working with these tools, or any developer for that matter, observer pattern could be a great mental model to have to effectivly use and extends these systems. Understanding this pattern helps in implementing reactive and real-time update mechanisms efficiently.

It is a common scenario, Where in a system one object changes and other objects are interested to know about that change. For our ease of discussion let's name these objects first. Objects that are interested to know about the change are called **`observers`** and interesting objects themselves be called **`observable`**. In books and literature on design patterns **`observable`** is also called **`subject`**, we will do the same. So, `Observers` observe the change of state in `Subject`. In terms of relation, this is an one-to-many relation, where subject's change is propagated to many observers. By the way, *change of state* is a fancy way to say some variable's value has changed.
**Observer pattern** suggests us a robust and flexible architecture to implement this **`Observer`** and **`Subject`** relation.  

Lets study some example scenarios where we are most likely to see the observer pattern. 

## Example Scenarios

### Theme chooser

 Nowadays applications, be it desktop or mobile, have at least three theme options, `Light`, `Dark` and `System`. While `Light` and `Dark` do what they are supposed to do, `System` option dance in rythm with the Operating system, i.e. if I set `Dark` theme in my OS display settings, the application will also use `Dark` theme in its UI.
 I personally prefer to select `System` as theme in applications to get an uniform UX across apps. So, when I change the theme from OS settings, definitly most of my applications would like to know about that. 

If we map this scenario with our previously mentioned terms, here applications that want to know about theme change are **`observers`** and the host operating system's settings is observable or **`Subject`**.

### Phone OTP messages

Think of the OTPs coming to our phone inboxes. I want to da a transaction, my bank app sends me an OTP to verify it's actually me making the request and as soon as the message arrives at my inbox the app collects that OTP on its own and fill up the security code. So definitly my bank app knows new message has arrived. And this is not special for bank apps, all kinds apps have this nice automated message reading and form fill up feature. 

Here, we see interested applications are notified on the state change of the message inbox. Here, message inbox is **`subject`** and the apps that are waiting for their own OTP messages are **`observers`**.

### E-Commerce Dashboard

Now, let's consider an E-Commerce dashboard, display cards shows numbers and matrices indicating the business state at any time. Maybe one display card shows the total order count, another gives the average expense amount per parchase And maybe another shows the sales trends based on hourly sales data. 
So, all three of these display cards are dependent on the sales count, i.e. whenever there is a new sale/order the value in these cards should be updated. In line with our two prvious examples, we can say three dsiplay cards **total order count**, **average revenue per order** and **sales trend** are **`observers`** and they are observing **`subject`** **sales count**. 

### Smart Home

This time we will consider a room of a smart home and use this example later in our code example below. 

Imagine, our smart room has different smart devices security cameras, lights, thermostats etc. These devices reacts as the number of persons in the room changes. For demonastration purpose we will consider the simplest version of the interactions. Whenever the number of persons in the room changes, certain devices reacts accordingly:

* Security Cameras activates when there is human presence.
* Smart Lights turn off automatically when there is no one in the room.

In this case:

* Smart room is the **Subject**.
* Devices like the Cameras and Lights are **Observers** that need to update their behavior based on the room's status. Here count of persons in the room is a state/attribute of the room.

Now that we have built the intuition how the **`observers`** and **`subject`** look like in a system, lets find out how they interact. 

## How to update observers on state change of subject

Question is how do we let **`observers`** know the state of the **`subject`** has changed?

We have two options,

1. **`observers`** poll the data at an interval to check if the **`subject`**'s state has changed 
2. **`subject`** push the update to the interested objects(*`observers`**) whenever there is a change in its state. 

Polling makes sense in some scenarios but at most of cases pushing is a better option for us. Let's do a comparison.

### Polling:

**Pros**: Simple to implement, allows observers to check at their own pace.
**Cons**: Inefficient use of resources, may miss rapid changes and real-time updates.

### Pushing:

**Pros**: Real-time updates, efficient use of resources, ensures all changes are captured.
**Cons**: More complex to implement. In cases where realtime update is not a concern it has a potential for overwhelming observers with frequent updates.

As our scenarios need a prompt reaction at changes in **`subject`**'s state change pushing notification is a better option for us. 
And here comes the observer pattern, suggesting us a loosly coupled code organization that let **`subject`** notify its **`observers`** about state changes without knowing much about the **`observer`** class internals. Both **`subject`** and **`observers`** implement certain interfaces and they communicate to each other through those interfaces. 


Now is the good time to take a look at the UML class diagram of **observer pattern**.

## Class Diagram

Observer patterns UML class diagram will clearify the relation and interaction between **`subject`** and **`observers`** more. Lets take a look. 

![Observer pattern UML class diagram][def]

We have two interfaces **Subject** and **Observer**. Other classes are concrete implementation of these Interfaces e.g. ConcreteSubject and ConcreteObserver. While Interfaces will provide us with a blueprint, concrete implementation of these interfaces will actually implement the methods of the Interfaces.

**Subject** has one attribute and three methods. While the attribute **`observers`** is a list of **Observer** instances, the methods do followings
1. **`addObserver`**: let an observer register itself for notifications from the **Subject**. After an **Observer** being added to the subject's observer list it will be notfied on the state changes of the **Subject**.
2. **`removeObserver`**: if the observer does not want to listen to the changes of the **Subject**, it can remove itself from the list of observers and it will not be bothered anymore.
3. **`notifyObservers`**: the function that will do the work of notifying the subject's **observers**.

Any and all classes that want to act as a **Subject** must implement above methods. 

Now lets consider the **Observer** interface. It has one method **`update`**. Concrete observer classes will have to implement this method.

1. **update**: this method will be called from the **Subject**'s **`notifyObservers`** method to let the observer know of an attribute/state change in **Subject**. This is our channel of notification.


Now that we have seen the code organization lets move on to the actual code. 

## Example Code for Observer pattern

Before coding let's restate our goal, design a smart home system that will have rooms with security camera and lights. These light and camera will be responsive to the presence of human in the room. If there is human in the room the camera will start monitoring while light will be lighting. So, both Camera and light are interested to know when there is a change in number of persons in the room. 

From above discussion it might be already clear to us observers are **`Light`** and **`Camera`**. And they will observe the state of the room. **`Room`** is our subject. Whenever state of the room changes, light and camera will be notified. 

So, our examples will be in python. Python doesn't have the concept of Interface. We can achieve the same using its Abstract Class concept. A brief on abstract class is [here](https://medium.com/@kbashar/strategy-pattern-with-python-1aeb5ec00208), look for the **Abstract Class in Python** section of the article. We will skip Abstract class related discussion here, as the article already got quite large. 

### Interfaces aka Abstract classes
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

### Concrete Classes

We have one **`Subject`** class **`Room`**. This class will implement all three methods of the **`Subject`** interface and two other methods to change and access its state. The implementation is kept simple and in-line comments are added. Hope this will be easy to follow.

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

    def setPerson(self, person: int):  # change the state
        self._number_of_persons = person

        # state has changed lets notify the observers
        self.notifyObservers()

    def getPerson(self):  # access the state
        return self._number_of_persons

```

Apart from implementing 3 methods (`addObserver`, `removeObserver` and `notifyObservers`) from the **`Subject`** abstract class it has two extra methods i.e. `setPerson` and `getPerson`. These methods let outside code update or fetch the state of the **`Room`**. These are not mandatory for the pattern but necessary for the class to function in our context.


Now let's code concrete observers. We have two observers `Light` and `Camera` classes, they will  first register themselves to the **`Room`** subject's observers list through `addObserver` and implement the **`update`** method logic to response to the change in state of the **`Room`**. 

```python
class Light(Observer):

    def __init__(self, room: Room):
        print("Initializing Lights!")
        self._room = room

        # register itself for door state change observation
        self._room.addObserver(self)

    def update(self):  # state of the room has changed

        # access the state from the subject
        number_of_persons = self._room.getPerson()

        # take some actions based on changed states
        if number_of_persons == 0:
            print(f"Light: Shutting down. {number_of_persons} persons in the room.")
        else:
            print(f"Light: Keep running. {number_of_persons} persons in the room.")
```


```python
class Camera(Observer):
    def __init__(self, room: Room):
        print("Initializing Security Camera!")
        self._room = room

        # register itself for door state change observation
        self._room.addObserver(self)

    def update(self):  # state of the room has changed
        # access the state from the subject
        number_of_persons = self._room.getPerson()

        # take some actions based on changed states
        if number_of_persons == 0:
            print(f"Camera: Shutting down. {number_of_persons} persons in the room.")
        else:
            print(f"Camera: Keep running. {number_of_persons} persons in the room.")
```  

Now lets add the calling code. For demonastration purpose we will put this code in main calling thread. 
First we initialize the **`Room`** instance and use that instance to initialize the **`Light`** and **`Camera`** instances. To update the the number of persons in the room we call `room.setState()` method and in turn this will notify and update the state of `light` and `camera`. 

```python

if __name__ == "__main__":
    room = Room()

    light = Light(room)
    camera = Camera(room)

    room.setPerson(1)
    room.setPerson(0)
    room.setPerson(5)

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
```

Full code is available here in [this github repo](https://github.com/kBashar/writings/tree/main/design_patterns/observer_pattern).

## Wrapping up  

Observer pattern is a handy toolkit to design and work with reactive systems. Definitely mastering a patterns comes not only from understanding the idea behind it but using and implementing it in systems as well. Mastering this pattern will help us to build scalable and modular software systems. Before wrapping up couple of  points,

1. When working in multi-threading system we should code keep thread safety in mind during implementing observer pattern.
2. If real-time update is not necessary observer pattern might not be a good fit. 
3. There are variations of this pattern, not all of them use the same OOP structure but the essence is same. 
4. Observer pattern is slightly different from publish-subscribe pattern as there is no message bus component here, message is sent directly to the observer.




[def]: ./imgs/observer_class_diagram.png



