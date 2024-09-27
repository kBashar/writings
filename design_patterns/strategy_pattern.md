## Strategy Pattern  

Strategy pattern suggests a simple but very useful paradigm to design OOP systems where there are multiple algorithms/strategies to do a task. The strategy pattern prescribes encapsulating algorithms into a common interface and use that interface to use those algorithms. This gives the client (the part of the code that use the algorithms) the flexibility to  choose any algorithm at runtime.

Let's think of the map app we all have in our phones. Users can find routes from place A to place B through the map, also the app gives us couple of possible modes of trasportations e.g walking, Cycling, Bike riding, Public Bus or Cars and the time they will take to go from A to B. This feature will be a nice candidate to be implemented using strategy pattern. Where mode of transportation are different algorithms/strategies and a common interface will provide with how much time it will take to go from address A to B. 

Let's take a look at another example. A payment processor in an e-commerce site can take payment in multiple ways e.g. using cards, MFS(Mobile Financial System) or cryptocurrency. Designing this payment processor is a prime candidate for strategy pattern. Here mode of payments will be algorithms the pattern talks about and the client will be the payment processor. 

Examples with codes are even better. Here I will use python/psudo-code but this pattern or any design patter for that matter is applicable and implementable in all OOP supported languages. 
So, We are designing a service for processing Payments for an E-Commerce. For started, users can pay through Visa and Master cards. So what would the code structure for payment processing look like?

```python

def visa_pay(self, amount):  # visa card related processing
  print("Doing visa card related processing")
  print(f"Receiving a payment through Visa card of amount {amount}")

def master_pay(self, amount):   # master card related processing
  print("Doing Master card related processing")
  print(f"Receiving a payment through Master card of amount {amount}")

def payment_processor(payment_type: str, amount: float):  # this is our payment processor
  if payment_type == "visa":
    visa_pay(amount)
  else payment_type == "master":
    master_pay(amount)
```

Simple, Right? Now what if as our e-commerce gets more traction, more and more users wants to make payment with their American Express(Amex) cards. What can we do? We can add another function `amex_pay` for amex card processing and change the `payment_processor` a bit to make room for the new payment mode. Not much of a headache(at least for me :D, I am just printing strings to take payments. Don't you wish money was this easy, :P!).


```python

...

def amex_pay(self, amount):
  print("Doing Amex card related processing")
  print(f"Receiving a payment through Amex card of amount {amount}")


def payment_processor(payment_type: str, amount: float):
  if payment_type == "visa":
    visa_pay(amount)
  elif payment_type == "master":
    master_pay(amount)
  elif payment_type == "amex":
    amex_pay(amount)
```

No matter how simple this looks, one thing is clear, every time we add support for a new payment mode we have to change the `payment_processor` method beside adding the code/functionality of the new payment mode. This is not very convenient, nor does it make easy to extend. Our `payment_processor` code is totally dependent on the individual payment modes, even though all of the payment mode related functions takes same arguments and maybe returns same data too, not much different from each other.

In cases such as this, **Strategy Pattern** suggests a better way to organize our code and make it more extensible and portable. The suggestion is, payment modes will have a common interface and the payment processor `payment_processor` will code to that interface instead of individual payment mode functions. So we can add new new payment modes later without changing any code in `payment_processor` part. Our new added payment modes will be supported by the `payment_processor` right of the bat. 

Let's try it out. But before that some python language pre-requisites. if you are familiar with python Abstract class system, you may skip the next section and jump to the code right away.

### Abstract Class in Python
An interface provides a blueprint through abstract functions, and interface implementing classes must make concrete implementation of those abstract functions and thus all classes that implement the same interface will have the same API(a fancy way to say it will have same methods/functions available to call). 
Now Python has no concept of Interface, as we see in Java or other OOP languages, abstract classes in python give us a way to have this same facility. We declare an abstract class with abstract methods. And all concrete classes that are inherited from the abstract class will implement those abstract methods. And thus those classes will have the same methods. 

One last point, to get abstract class we will need to use `abc` module from python standard library. This module supplies two important components we will use, `ABC` and `abstractmethod`. `ABC` is the class that all abstract classes themselves must inherit and `abstractmethod` is a decorator that all abstract methods must adorn themselves with. 

### Code Example of Strategy pattern

Now lets hop into the code-wagon.

```python
from abc import ABC, abstractmethod

# our interface made out of an abstract class.
class PaymentInterface(ABC):

  # all payment mode will implement this abstract method
  @abstractmethod
  def pay(self, amount):
    pass


class VisaPayment(PaymentInterface):   # inherits the PaymentInterface and implements the `pay` method

  def pay(self, amount):
    print("Doing visa card related processing")
    print(f"Receiving a payment through Visa of amount {amount}")


class MasterPayment(PaymentInterface):

  def pay(self, amount):
    print("Doing Master card related processing")
    print(f"Receiving a payment through Master of amount {amount}")


class AmexPayment(PaymentInterface):

  def pay(self, amount):
    print("Doing Amex card related processing")
    print(f"Receiving a payment through Amex of amount {amount}")



def payment_processor(payment_method: PaymentInterface, amount: float):
  payment_method.pay(amount)

```


Nice, our payment_processor looks clean and very unlikely to need change if we add new payment modes, say we want to add a payment mode for Bkash(MFS), we would only need to add the bkash payment processing code in the bkash related class, No change in `payment_processor` function. This is definitely neat and a win for code maintainability.

How do we map names to actual PaymentMethod at runtime? There are several ways to accomplish this, one example could be as following 

```python
class PaymentService:
    def __init__(self):
        self.payment_methods = {
            "visa": VisaPayment(),
            "master": MasterPayment(),
            "amex": AmexPayment()
        }

    def process_payment(self, method: str, amount: float):
        if method not in self.payment_methods:
            raise ValueError(f"Unsupported payment method: {method}")
        
        payment_method = self.payment_methods[method]
        payment_processor(payment_method, amount)
```
In above example, the class initializes a dictionary payment_methods that maps payment method names to their corresponding PaymentInterface implementations. When there is a new Payment method added we will need to add the corresponding PaymentInterface class and an entry in the mapper.
This mapper part is totally dependent on the context of implementation.

### When to use Strategy Pattern  

* You've got a bunch of related algorithms, and you want to switch between them dynamically.
* You want to avoid a monster "if-elif-else" chain in your code. Trust me, future you will thank present you for not creating that mess.

Remember, design patterns are tools, not rules. Use only when you have time and reason to do so.

### Skip the Strategy Pattern when:

* You've only got a couple of algorithms that rarely change.
* The algorithms and their context are super simple. Sometimes, a simple if-else is all you need. Don't overcomplicate things!

### Wrapping Up  

Strategy pattern is a cool code-toolkit, gives us

* **Flexibility:** Let us add new strategies or algorithms without changing or impacting previous client codes.
* **Cleaner Code:** Makes code clean, no more long list of `if-else-if`.
