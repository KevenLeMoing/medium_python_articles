# One minute, one tip

All of the code used in this article is available from my Github [repository](https://github.com/KevenLeMoing/medium_python_articles)

Design pattern are elegant solutions to solve repeating software programming problems.
It defines how should structure your classes and how your classes should talk to each other.

I did similar articles for the following list of design pattern (all in Python):
* Memento
* Adapter
* Facade
* Strategy
* Factory Method

### What is this design pattern about ? 

The design pattern "Chain of Responsibility" allows classes to answer a request without knowing other classes possibilities for that specific request.

### Let's implement it !

In order to illustrate this concept, we are going to create a `data_pipeline` object. Depending on the input parameter, the filter will follow specific behaviours: 
* If the input is a `string` that cannot be converted as an `int`, the `data_pipeline` output a the input in upper case.
* If the input is an `int` or a `string` that can be converted as an `int`, the `data_pipeline` convert it to a `float` and output that result.

### Overall comments

Classes that we are created are going to chain with each other.
The first class