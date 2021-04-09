def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whoo():
    print("Whee!")


from decorators import do_twice

@do_twice
def say_whee():
	print('Whee!')

say_whee()