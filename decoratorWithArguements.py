# This decorator function modifies the given function to return a result 
# That is higher by one
def add_one(f):
    # The return function
    def is_returned(x):
        # Modifies the value by one
        return f(x)+1
    # Return a function
    return is_returned

# The decorator modifies the function
@add_one
# Although this function takes no action on the input, the decorator causes the
# return value to be higher
def no_action(x):
    return x
    
# Invoke the function and print the result
print(no_action(2))






