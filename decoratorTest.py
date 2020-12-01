def invokeWithinStars(f):
    def is_returned():
        print("*****")
        f()
        print("*****")
    return is_returned

@invokeWithinStars
def helloWorld():
    print('Hello World')

helloWorld()