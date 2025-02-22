"""
multithreading: One process can be split into smaller pieces and run each piece
in parallel. This is piece is called thread
library name: threading

multiprocessing: creating multiple processes and run parallely
library name: multiprocessing

Here,
we are discussing, multithreading

IMPORTANT : multithreading in python is NOT-PARALLEL

If it is NOT-PARALLEL then what is the use of multithreading in python?
- if one thread is waiting for some resource
    then
during that waiting, it will execute another thread

So, FINALLY, if we use multithreading then
WE CAN UTILIZE waiting time of other thread

If we want 100% parallel execution then use multiprocessing
"""
print("WITHOUT USING multithreading")
print("-"*20)
# -------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L= [10, 20, 30, 40, 50]
my_square_function(L)
my_cube_function(L)

end_time = time.time()

print("Total Time Taken:", end_time-start_time, ":Seconds")

print("#"*40, end="\n\n")
##########################

print("USING multithreading")
print("-"*20)
# -------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L= [10, 20, 30, 40, 50]

from threading import Thread
thread_1 = Thread(target=my_square_function, args=[L])
thread_2 = Thread(target=my_cube_function, args=[L])

# Start the thread
thread_1.start()
# start() -> just start the thread and proceed to next-line,
# it will not wait for thread_1 complete
thread_2.start()
# start() -> just start the thread and proceed to next-line,
# it will not wait for thread_2 complete

thread_1.join() # WAIT HERE till thread_1 completes
thread_2.join() # WAIT HERE till thread_2 completes


end_time = time.time()

print("Total Time Taken:", end_time-start_time, ":Seconds")

print("#"*40, end="\n\n")
##########################

print("WITH DELAY: WITHOUT USING multithreading")
print("-"*20)
# -------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)

L= [10, 20, 30, 40, 50]
my_square_function(L)
my_cube_function(L)

end_time = time.time()

print("Total Time Taken:", end_time-start_time, ":Seconds")

print("#"*40, end="\n\n")
##########################

print("WITH DELAY: USING multithreading")
print("-"*20)
# -------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L= [10, 20, 30, 40, 50]

from threading import Thread
thread_1 = Thread(target=my_square_function, args=[L])
thread_2 = Thread(target=my_cube_function, args=[L])

# Start the thread
thread_1.start()
# start() -> just start the thread and proceed to next-line,
# it will not wait for thread_1 complete
thread_2.start()
# start() -> just start the thread and proceed to next-line,
# it will not wait for thread_2 complete

thread_1.join() # WAIT HERE till thread_1 completes
thread_2.join() # WAIT HERE till thread_2 completes


end_time = time.time()

print("Total Time Taken:", end_time-start_time, ":Seconds")

print("#"*40, end="\n\n")
##########################
