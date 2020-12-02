# For learning purposesWe need a function to be used for decoration
def decorateWithStars(f):
    # The decorator needs to return a function
    def is_returned():
        # The returned function can take actions, and alter the original,
        # Or it can leave the function un-changed
        print("*****")
        # The decorator function can choose whether to invoke the decorated
        f()
        print("*****")
    return is_returned

# The decorator sytax is equivalent to writing:
# def helloWorld():
#     print('Hello World')
# helloWorld = invokeWithinStars(helloWorld) 
@decorateWithStars
def helloWorld():
    print('Hello World')

# Invoke the hello world function
helloWorld()