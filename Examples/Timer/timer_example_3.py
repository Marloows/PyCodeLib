import timer

# Example
# How to the Timer-Object
# Context Manager

# function for debugging/testing

sleep = timer.sleep     # alias for sleep from timer

Timer = timer.Timer     # alias for Timer from timer


# initialize the timer
T = Timer()


# just put it in front of a “with”
with T:
    sleep()     # sleep for a second 


# you can still get the time spent in the "with-statement"	    *as a float variable
# Just reach for the time parameter
time_elapsed = T.time

print('The with-statement-script took', time_elapsed, 'seconds to finish')
