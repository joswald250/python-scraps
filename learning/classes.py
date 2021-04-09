""" Classes: The following object whose name is 'joey' is a class object. This means it has the capability 
to have certain data and functions wrapped inside itself (class methods and objects). These class methods/
objects are known as the class suite.
Namespaces: Every class/module/global program, etc... has a namespace
which is a dictionary that maps certain objects (instances in memory) to a name. Classes create a new 
namespace, which you access with dot notation. So joey.boy is a reference, or pointer, to the object 
whose value is 'True' and is defined below.  """
class joey:
    """ Example class """ # This is a docstring - it will be returned by the joey.__doc__ attribute
    boy = True # this is known as a class attribute
    a = 2

    def my_name(self): # This is known as a method
        return "Joey"

    def get_b(self):
        return self.a


""" Inheritance - The class object 'son' inherits from the class 'joey', which means it automatically has most of the objects 
(methods/data) that the class 'joey' does. Thus, a call to 'son.boy' will return the object defined in the 
class 'joey', so long as the 'son' class does not also have an object named 'boy'. A class can 'inherit'
data/methods from multiple 'base classes'. AKA, son could inherit from 'joey' and any number of other classes. """


class son(joey):
    """ Example class inheriting from Joey """
    man = False # Class attributes are share by all instances of the class, any instance of son will have this object
    a = 1

    def __init__(self): # The init, or initialization method, sets an initial state for any instantiated class object
        self.data = "Initialized data"

    def get_a(self):        
        return super().get_b()



""" Class Instantiation - The object named 'gustavus' below is an instance of the class 'son', and 
has access to all of the class objects (both methods and data) in any of the classes which it 
inherits from (son, joey, 'object'). The process of creating a new object based on the class is 
known as 'instantiation'. Thus, I instantiated the son class and assigned it to the variable gustavus below. """

gustavus = son() # Instantiation of class son

print(joey.boy) # Calling attribute
print(son.boy) # Inherited attribute
print(gustavus.boy) # Inherited attribute after initialization
print(gustavus.data) # Data from the __init__ method

# Built-in class attributes 
print(gustavus.__dict__) # The initialized object's namespace
print(gustavus.__doc__)
print(gustavus.__module__)

""" Method Objects - methods require an argument (conventionally 'self') in their definition, but you
don't have to use it when you call them. This is because when we call a method (like the second
example below), we are actually calling the class method and passing the instance object as the 
first argument. You can see the difference below. """

print(gustavus.my_name) # method object - can be stored and called later
print(gustavus.my_name()) # method call - will execute right away

""" Super method - super() is used to essentially look for the method/attribute in a parent class
of the current class you use the super call in. It returns a temporary object of the 'superclass' 
that then allows you to call that superclass's methods. For instance, each class has an attribute 'a',
with the 'joey' class having 'a = 2', and the 'son' class having 'a = 1', see below """

print(joey.a)
print(son.a)

""" Now if we call the inherited method, it will automatically use 'joey' class method "get_b" 
without us having to specifically reference it. Note that it uses the super's method, but the data
(the 'a' attribute that is returned in 'self.a') is actually the attribute of the 'son' class.
This means that since the super's method uses the 'self' variable, and it is the 'son' class calling the method,
it is returning son's 'a' value. A silly example, but these can be very powerful when you
have real classes that inherit significant functions from each other. """

print(str(gustavus.get_a()) + '\n')


""" Advanced - iterators and generators. Any object that is iterated over in a for loop (the WORD in:
for x in WORD:) needs a special couple of methods to make it iterable. The first is the 'iter()' method.
This method simply returns the object itself. The second method is a 'next()' method that simply returns 
the object itself, while also counting from the highest number of the index to the lowest. When the 'next()'
method reaches the last item (index == 0), it raises a 'StopIteration' exception which tells the for loop
to terminate. See below. """

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

""" Generators: a generator is a function that creates an iterator object. They look like normal functions
except they use the 'yield' statement to return data. Every time the 'next()' method is called on the 
iterator object created from a generator, the generator resumes where it left off. The below example
has the same functionality as the iterator created above. """

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)