import timer

# Example
# How to the Timer-Object
# Timer-Click
# multiple clicks


# function for debugging/testing

sleep = timer.sleep     # alias for sleep from timer

Timer = timer.Timer     # alias for Timer from timer


# initialize the timer
T = Timer()


# do something
sleep()     # sleep for one second

# prints the time passed since initialized time
T()

# do something
sleep()     # also sleeps for one second

# show time passed since last marked
T()


# do some other stuff
sleep(2)     # sleep for two second

# show time passed since last marked
T()

print(T.summary())

T.export()
