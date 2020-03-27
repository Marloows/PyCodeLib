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

exit()  # ends demo


# Further functionality


# Timer reset
# rest the clock and clears the *memory of the timer        ** values stored in T.marks
T.reset()


# T as a list

# index of *calls       ** marks you placed in your code
# each time you call the T-Objcet the time is stored in list T.marks
# you can access these values by indexing the T-Object itself
# T[0] is the time, when the T-Object is created
# T[n] is the nth call and so on
# the difrence bettwen two refrences to T-Object "T[m], T[n]", is the time passed computing between those time-points
# time_elapsed = T[m]-T[n]

# basically, you can treat the T-Object somewhat as list
    # indexing T-Object the same index T.marks      # T[index] = T.marks[index%len(T.marks)]      **idiot-proofed   #IndexError should be eliminated
    # __iter__ is implemented                       # "for x in T" is ok
    # __len__ is also there                         # len(T) = len(T.marks)

