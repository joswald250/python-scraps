""" List Comprehension - is just a shorthand way of creating a for loop, essentially, with the output 
typically assigned to an object. For example, this for loop: """

squares = []
for x in range(10):
    squares.append(x * x)

""" Gets turned into this list comprehension. You don't have to assign it to a value, though when you 
wouldn't, I dunno. """

squares2 = [x * x for x in range(10)]

# squares and squares2 are equivalent
print(squares)
print(squares2)

# The generalized format is this:

# (values) = [ (expression) for (value) in (collection) ]

""" Conditional List Comprehension - you can add conditions upon the expression by adding an if clause
at the end of the list comprehension statement. The following list comprehension statement will only evaluate
the expression at the beginning if the value of x is evenly divisible by two. """

even_squares = [ x*x for x in range(10) if x%2 == 0]

print(even_squares)

""" You can have multiple if statements in a list comprehension, simply add another if statement after the
first, with no syntax in between (other than whitespace). This is a silly example, but you get the point. """

foursquare = [x*x for x in range(10) if x % 2 == 0 if x % 4 == 0]

print(foursquare)

""" If Else - you can also add other clauses to the list comprehension. However, if so, you must move
the conditional clause to right after the first expression and before the for statement. """

keepunevensquares = [x * x if x % 2 == 0 else x for x in range(10)]

print(keepunevensquares)

""" Nested List Comprehension - it is possible to nest list comprehension statements. These would be used
in the case where a list contains many lists (a list of lists, in other words). The syntax for such a list
is as follows. """

list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]

one_list = [x for y in list_of_lists for x in y]

print(one_list)

""" The above list comprehension takes the list elements (x) of the nested lists (y) in list_of_lists
and returns a list of those list elements (y) that are comprised in (x). """