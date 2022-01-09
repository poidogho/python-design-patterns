# python-design-patterns

Exploring python design patterns - creational, structural, behavioural patterns

## Factory pattern

```sh
# Generally used when you are not sure what your objects will look like

```

## Abstract Factory

```sh
# Used when we expect multiple but related objects
# Objects dont need to be known until run time

```

### Abstract Factory Scenario By Example

```sh
# We need a pet store that creates several for for several pets
```

### Abstract Factory Solution of Scenario

```sh
# We need a object for each of the pets that will be represented in the store
# We then have a factory class for each of the objects that will have methods to get the initial object and also creating the food of the objectin question
# a pet store object that will be initialized with any of the factory created
# this way several factories and objects can be created and initialized only at runtime
```

## Singleton Pattern

```sh
# Used when only one object of a class has to be instantiated
# Creating a global variable in an OOP way

```

### Singleton Pattern Scenario by example

```sh
# We need an object that will continually log the position and employees of orezime global
# This object will be global and will continue to grow as new employees are added
```

### Singleton Solution of Scenario

```sh
# Refer to the singleton folder to see simple implemetation code
```

## Decorator Pattern

```sh
# Used to add new features to an object without using subclassing
# Dynamic changes
```

### Decorator Pattern Scenario

```sh
# Have a simple function that prints a name
# We ll add a decorator that just adds <decorate> to the a text
```

## Proxy Pattern

```sh
# Used when its expensive to create an object
# responsibility of creating such object is now shifted to a proxy class
```

### Proxy Pattern Scenario

```sh
# Have an object called Producer who is not always available
# A proxy class will be responsible for creating this Producer object
```

## Adapter Pattern

```sh
# Converts an interface of a class into another class that a client expectss
# Usually helps 2 incompatible interfaces
```

### Adapter Pattern Problem example

```sh
# Assume 2 different language objects eg- french and english
# Both object have speakFrench() and speakEnglish() methods
# client uses speak() method
```

### Adapter Pattern Solution example

```sh
# Create an adapter that translates the language
```
