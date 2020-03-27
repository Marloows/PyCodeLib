from timer import Timer

from timer import sleep

# Example
# How to the Timer-Object
# Decorator


# initialize the timer
T = Timer()


# each time the func is called, the time it took to run will be displayed
@T
def func(bis = 2):
    sleep(bis)

func()

func(1)

func(3)

# this offers the full functionality of the T-Object
    # somewhat simpler way is below 

exit()      # que demo




# Disclaimer!!
# Only in case you don't want the full summary of the T-Object
# Otherwise use it as shown in the code above

    # *The reason for the is, one can't access the decorator once the function has been implemented
        # **At least no way that I am aware of :)


# you can create a new T-Object to be a decorator
@Timer()    # create a new T-Object, which returns a decorator to be used as timer for the function each time it's called
def f():
    pass

# you can change the parameter of T-Object by giving the Timer constructor some values to work with
@Timer(msg = "\nFunc-Time {}\n")
def f_():
    pass
