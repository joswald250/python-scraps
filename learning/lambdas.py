""" Lambda Functions - these are throwaway functions which need not be named and typically take up a single
line in your code. They cannot be re-used, and so serve a simple purpose - typically as processing of
inputs for another function or for quick calculations. """

# Assume we have some list:
a = [(1,2), (3,4), (5,6), (3,7)]

# If we wanted to get all the second values from this function, we could do this:
a.sort(key=lambda x:x[1])

# This lambda function takes an input x, and returns the second indexed item of that input.
