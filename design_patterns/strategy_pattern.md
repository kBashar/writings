## Strategy Pattern  

Strategy pattern suggests a simple but very useful paradigm to design systems where there are multiple ways/algorithms/strategies to accomplish a goal. For example, a payment processor can take payment in multiple ways e.g. using cards, MFS, cryptocurrency or through bank drafts. 
Strategy pattern prescribes, to encapsulate these algorithms into a common interface. And this interface is then used by the client, the payment processor in our above example, when doing the actual work instead of using a specific algorithm. This gives the client the flexibility to  chose any algorithm at the runtime.

Lets take a look at some examples. For me examples are doorway from knowledge to intuition. Hope this helps. 

We are designing a service for processing Payments for a E-Commerce. User can pay through Visa, Master or Amex cards. So what would the code for payment processing look like?

```python

def visa_pay(self, amount):
  print("Doing visa card related processing")
  print(f"Receiving a payment through Visa of amount {amount}")

def master_pay(self, amount):
  print("Doing Master card related processing")
  print(f"Receiving a payment through Master of amount {amount}")

def payment_process(payment_type: str, amount: float):
  if payment_type == "visa":
    visa_pay(amount)
  else payment_type == "master":
    master_pay(amount)
```

Simple, Right? Now what if as our e-commerce gets more traction and business people wants to open the platform to more people, we are to Amex(American Express) based payment services in our payment processor. What can we do? We can add another function `amex_pay` for amex card processing and change the `payment_process` a bit to make room for the new payment method. Not much of a headache(at least for me :D, I am just printing strings to take payments. Don't you wish money was this easy, :P!).


```python

def visa_pay(self, amount):
  print("Doing visa card related processing")
  print(f"Receiving a payment through Visa of amount {amount}")

def master_pay(self, amount):
  print("Doing Master card related processing")
  print(f"Receiving a payment through Master of amount {amount}")

def amex_pay(self, amount):
  print("Doing Amex card related processing")
  print(f"Receiving a payment through Amex of amount {amount}")


def payment_process(payment_type: str, amount: float):
  if payment_type == "visa":
    visa_pay(amount)
  elif payment_type == "master":
    master_pay(amount)
  else payment_type == "amex":
    amex_pay(amount)
```
No matter how simple this looks, one thing is clear, every time we are to add a new payment method we need to change the `payment_process` method beside adding the code/functionality of the new payment method. This is not very convenient, nor does it make easy to extend. Our `payment_process` code is totally dependent on the individual payment methods.

**Strategy Pattern** suggests a better way to organize our code to be more extensible and portable. The Suggestion is, the payment methods will have a common interface and the payment processor `payment_process` will code to that interface instead of individual payment method's functions.

Let's try it. But before that some python language pre-requisites. 

Python has no concept of Interface, as we see in Java or other OOP languages. What an interface do is provide a contract/blueprint that implementing classes must implement and thus all classes that implement the interface methods will have same API/interface. While Java supports single inheritance, it supports multiple interface implementations.
Abstract classes in python gives us a way to have this same facility. We declare an abstract class with abstract methods. And all concrete classes(not abstract classes themselves) that will be subclassed/derived from this abstract class should implement those abstract methods. 
Interesting thing is as python supports Multi inheritance a python class can implement multiple abstract classes. So, we have almost all of the Java like interface in Python.

One last point, to get abstract class we will need to use `abc` module. This modules supplies two most important artifacts we will use, `ABC` and `abstractmethod`. `ABC` is the class that all abstract class must inherit and `abstractmethod` is a decorator that all abstract methods must adorn themselves with. 


```python
from abc import ABC, abstractmethod

# our interface
class PaymentInterface(ABC):

  # all payment methods will implement this method
  @abstractmethod
  def pay(self, amount):
    pass


class VisaPayment(PaymentInterface):

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



def payment_process(payment_method: PaymentInterface, amount: float):
  payment_method.pay(amount)

```


Nice, our payment_process looks clean and very unlikely to need change if we add new payment methods, say we want to add a payment method for Bkash(MFS), we would only need to add the bkash payment processing code in the bkash related class, No change in `payment_process` function. This is definitely neat. This flexibility goes a long way when our applications are complex and a group of algorithms/strategies(in our case payment methods) is used in different areas of the application. 
