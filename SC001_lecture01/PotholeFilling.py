"""
File: PotholeFilling.py
Name: Jacky:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition karel in (1,2)
    post-condition karel in (7,2)
    """
    #Algorithm
    for i in range(3):
       go_in()
       put_99_beepers()
       go_out()



def turn_right():
    turn_left()
    turn_left()
    turn_left()


def put_99_beepers():
    for i in range(99):
        put_beeper()


def turn_around():
    turn_left()
    turn_left()


def go_out():
    """
    pre-condition karel was originally in the south
    post-condition karel originally faced east
    """
    turn_around()
    move()
    turn_right()
    move()


def go_in():
    """
    pre-condition karel originally faced east
    post-condition After moving and turning, karel faces south
    """
    move()
    turn_right()
    move()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
