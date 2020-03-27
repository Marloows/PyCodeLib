import time

class Timer:

    """
    Timer-Object can be used:
        - as a timer by initialize it, calling script, and calling it again at the end
        - as logger by calling it multiple times
        - as context manager		*in with-statement
        - as a decorator
    """

    # Class default values

    precision = 2   # significant figures to display the timer time

    msg = "\nTimer:\t{} seconds elapsed . . .\n"     # message to be displayed for single call

    msg_mark = "\nMark_{}\t{} seconds elapsed since last mark.\n"   # message to be displayed for repeated call


    def __init__(self, msg = msg, msg_mark = msg_mark, precision = precision):
        
        # Properties
        self.index = 0                  # the index of timer call
        self.time = float()             # last measured cycle
        self.msg = msg                  # formatted message to be displayed     # When the timer is used once
        self.msg_mark = msg_mark        # formatted message to be displayed with index
        self.precision = precision      # How many significant figures to be displayed

        # Timer
        self.marks = [time.perf_counter()]
    


    # calling the T-Object has two effect
        
        # with no arguments it’s a timer click

        # with argument it returns a decorator
            # a decorator is a function that takes a function as an input and returns a function “a wrapper” as 
    def __call__(self, *arg):
        if len(arg) != 0:
            return self.__deco__(*arg)
        self.show_timer_mark()
        return self.time


    # list-like behaviour

    # returns the value stored in self.marks
    def __getitem__(self, index):
        if index < 0:
            return self.marks[-((-index)%(len(self.marks)+1))]
        return self.marks[index%len(self.marks)]    # fail-safe     # idiot-proof
    
    # length of the T-Object is the length self.marks
    def __len__(self):
        return len(self.marks)
    
    # iteration behaviour
    def __iter__(self):
        for t in self.marks:
            yield t



    # Contextmanager 
    # to be called in with-statement for example

    def __enter__(self):
        self.mark()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.mark()
        self.show_timer()



    # Methods


    def mark(self):
        "adds the time to T-Object and rest the clock for the next cycle"

        self.index += 1
        self.marks.append(time.perf_counter())
        self.time = round(self.marks[-1] - self.marks[-2], self.precision)


 
    def reset (self):
        "reset the timer and re-initialize its values"

        self.marks.clear()
        self.mark()
        self.index = 0
    

    
    # functionality

    # Decorator

    def __deco__(self, func):
        "To be use when the T-Object is called to be a decorator"

        def wrapper(*args, **kwargs):
            self.mark()
            revalue = func(*args, **kwargs)
            self.mark()
            self.show_timer()
            return revalue
        return wrapper



    # Print/Display

    
    def show_timer(self):
        "displays the time elapsed since last call according to formatted message"

        print(Timer.show_timer_cls(self.msg, self.time))
    
    # to be also used when exported
    @classmethod
    def show_timer_cls(Timer, msg, time):
        return msg.format(time)


 
    def show_timer_mark(self):
        "marks time and displays the time elapsed since last call"

        self.mark()
        print(Timer.show_timer_mark_cls(self.msg_mark, self.index, self.time))
        

    # to be also used when exported
    @classmethod
    def show_timer_mark_cls(Timer, msg, index, time):
        return msg.format(index, time)


    # Summary/Export

    # message to be displayed for single call
    msg_summary = "Marks_{} occurred after\t{} seconds"

    # message to be displayed for repeated call
    msg_mark_summary = "Marks_{} occurred after\t{} seconds"


    def get_time(self):
        "return a list with time between the timer calls"

        return *(round(self.marks[n] - self.marks[n-1], self.precision) for n in range(1, len(self.marks))),


    def data(self):
        "returns a dictionary with important values"

        summ = dict()
        summ['marks'] = *(mark for mark in self.marks),
        summ['time'] = self.get_time()
        return summ
    

    def summary(self):
        "returns timer summary as str"

        summ = self.data()

        a = Timer.show_timer_mark_cls   # alias

        text = 'Timer Information\n\nTime between calls:\n'
        msg = Timer.msg_summary
        for index, t in enumerate(summ['time']):
            text += '\n\n' + a(msg, index, t)
        
        text += '\n\n\n\nMarks occurred n seconds since python session have started:\n'
        msg = Timer.msg_mark_summary
        for index, m in enumerate(summ['marks']):
            text += '\n\n' +  a(msg, index, m)
        text += 2*'\n'
        return text
    

    # export timer summary to txt file
    def export(self, out_file = 'timer_summary.txt', mode = 'w'):
        "exports timer summary to txt file"

        text = self.summary()
        
        with open(out_file, mode) as file:
            file.write(text)
        
        print('Timer summary has been exported as', out_file)

        return text
    
        # giving out_file as a full path can change the location where the file is saved
        # otherwise it's going be saved in current working directory





# Debuging/Demo

def sleep(s = 1):
    print('\nSleeping for', s, 'Seconds....\n\nzzZzZzZzZzz\n')
    time.sleep(s)
    print('Slept for', s, 'Seconds....\n')

