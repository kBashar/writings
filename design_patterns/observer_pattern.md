It is a common scenario, Where in a system one object changes and other objects are interested to know about that change. Examples are avadant in software systems. 

### Example Scenarios

For our ease of discussion let's name these objects first. Objects that are interested to know about the change are called `observers` and interesting objects can be called `Observable`. In books and literature about design patterns this `observable` is also called `subject`.

 For example, applications now have at least three choices in application theme change plane, "Light", "Dark" and "System". If an application has its theme set to `system` it would definitly like to know when user changes the theme in host(where the application lives on) operating system. 
 I personally prefer to select `system` as theme in applications, to get an uniform UX across apps. So, when I change the theme from OS settings, definitly most of my applications would like to know that. 

Interested applications are notified on the system wide theme change. So, here applications that wants to know about theme change are **`observers`** and the host Operating System's settings object is **`observable`**.

We can think of the OTPs. My bank app sends me an OTP and as soon as the message arrives it collects that OTP on its own and fill up the security code. So definitly my app gets notified by the OS. And this is not special for bank apps, many apps have this nice automated message reading and form fill up. 

Here, we see interested applications are notified on the state change of the message box. Here, message box is **`observable`** and the apps that are waiting for their own OTP messages are **`observers`**.


Now, let's consider an E-Commerce dashboard, It hosts many numbers and matrices indicating the business state at any time in diferent display cards. Among others one display card shows the total Order count, another shows the average expense amount per parchase And maybe another to show the sales trending based on hourly sales data. 
So, all three of these display cards are dependent on the sales count, i.e. whenever there is a new sale/order the value in these cards should be updated. In line with our two prvious examples, we can say three dsiplay cards **total order count**, **average revenue per order** and **sales stat** are **`observers`**. Here, **`observable`** will be the **sales count** object. 

### How to update Observers on state change of Observable

Question is how do we let **`observers`** know the state of the **`subject`** has changed?

Do we poll at an interval to check if the object's state has changed or do you push the update to the interested objects whenever there is a change. 

Polling makes sense in some scenario but at most of the pushing is a better option
