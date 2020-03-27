import timer

# Example
# How to the Timer-Object
# Timer-Click


# function for debugging/testing

sleep = timer.sleep     # alias for sleep from timer

Timer = timer.Timer     # alias for Timer from timer



# initialize the timer
T = Timer()

# do something
sleep()     # sleep for one second

# prints the time passed since initialized time
T()



exit()  # ends the basic deme

# first demo is just the most basic function of the T-Object
# "exit" is there, just to make the first demo easier to follow



# the code below explores the various ways one can get more info out of the T-Object





# you can save the time it took to finish by saving the return value of calling the T-Object
T = Timer()             # initialize
sleep()                 # do something
time_elapsed = T()      # prints a message to the console and returns T.time


# Or by asking for the parameter time after calling the T-Object
T = Timer()             # initialize
sleep()                 # do something
T()                     # prints a message to the console       * return value going to be thrown out
time_elapsed = T.time   # time span between initializetion and last call


# Or just reach for the time of the timer calls
T = Timer()                     # initialize
sleep()                         # do something
T()                             # prints a message to the console       * return value going to be thrown out
time_elapsed = T[-1] - T[-2]    # last call of the T-Object minus the one before that




# other ways to accesses the Timer class
    # import timer
	# Timer = timer.Timer		# alias

	# from timer import Timer	# partial import 

	# from timer import *		# import everything from timer
        # runs the script from timer as if called from this module
            # if __name__ == '__main__' is still false





# **Tips
    # Try Visual Studio Code, it's quite good and for free

    # if you are VS-Code, you can easily see the definition of an *Object

        # Just right-click on the Object, which definition you want to see,
        # and chose  "Go To Definition" from the pop-up menu

        # Or place the blinking-cursor on the Object, and press “F12”

    # **Object in this context includes classes, function,
    # and even normal objects 
	    