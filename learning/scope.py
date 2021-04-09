""" there are 4 scopes to be aware of:
1. Local scope
2. enclosing scope - scope of a function or object that "encloses" other objects within it
3. global
4. built-in scope
When namespacing something (trying to find the referenced object), these scopes are searched in the order
they appear here. There are two statements that can alter this - global and nonlocal. These statements
change the scope of the reference they modify (nonlocal variable_name). """
def scope_test():
    def do_local():
        spam = "local spam" # This variable is never used, because the function does not return it

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global() # This function makes a global variable, which is overwritten by the nonlocal spam
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)