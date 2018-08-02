# Trying to understand functions in functions

from threading import Thread
import time
second = 0
def seconds ():
    
    global second
    second += 1
    return second



def timer (name, delay, repeat):
    print ("Timer:\t", name, " Started")
##    second = 0
    while repeat > 0:
        time.sleep (delay)
        print (name, ":", str(time.ctime(time.time())))
        repeat -= 1
        print (seconds ())
        if repeat == 0:
            global second
            second = 0
        

    print ("Timer: \t", name, "Completed")

##def seconds (name_of_timer, seconds):
##    timer (name, delay, repeat)
##    while timer (repeat) > 10:
##        print (name_of_timer, seconds)
##        seconds += 1


def main ():
    thread1 = Thread (target = timer, args = ("Timer1", 1, 5))
##    seconds ("Timer 1", 1)
    thread2 = Thread (target = timer, args = ("Timer2", 7, 10))
    thread1.start ()
    thread2.start ()

    print ("Main Fx Completed")


    
if __name__ == "__main__":
    main ()

##def seconds (name_of_timer, seconds):
##    for second in seconds:
##        print (name, seconds)































