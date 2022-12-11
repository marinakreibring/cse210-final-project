# cse210 - Final project
cse210 week6 Developer
# coded by Marina Kreibring (timarina1997@yahoo.com)
# BYU-I fall 2022
This game is a generator of random sentences.
The game consists of 8 classes. 
The Word is a super class, in which the common attributes of subclasses are defined. 
Classes: Determiner, Adjective, Subject, Predicate, Modifier are subclasses of the Word class. They inherite its attributes, but have their own fuctions. 
Director leads the entire process. He gets information from all classes and combines it together. 
Termional_Service class provides read/write text/number services.
Thus, the principles of abstraction, encapsulation, inharitance and polymorphism are respected in this game. Each class has its own responsibility. Each class has private 
variables and performs only its functions. When needed they have public methods. Common attributes and methods and inherited from superclass. Specific behaviors are overidden in subclass' methods.
The program is maintanable, because the classes are clear and I put many comments to the code, so that any user can understand it and develope if needed.
## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- final project       (source code for game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
  +-- README.md         (general info)
```