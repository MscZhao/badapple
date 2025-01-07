from enum import Enum
import time

#
ESC_BASE = "\033["


class EraseMode(Enum):
    ALL = 2
    HEAD = 1
    TAIL = 0


def printnn(str):
    print(str, end="", flush=True)


class Cursor:

    @classmethod
    def up(cls, l):
        printnn(f"{ESC_BASE}{l}A")
    @classmethod
    def down(cls, l):
        printnn(f"{ESC_BASE}{l}B")
    @classmethod
    def hide(cls):
        printnn(f"{ESC_BASE}?25l")
    @classmethod
    def show(cls):
        printnn(f"{ESC_BASE}?25h")

def clear_line(mode: EraseMode = EraseMode.ALL):
    printnn(f"{ESC_BASE}{mode.value}K")

def clear_display():
    printnn("\033[J")

diff = 0

step = 58

line_num = 1

printnn("\n"*step)

with open("badapple.txt", 'r') as f1:
    while True:
        line = f1.readline()
        if not line:
            break
        diff = line_num % step
        if diff != 0:
            diff = step + 1 - diff
        else:
            diff = 1 
        Cursor.up(diff)
        clear_line()
        printnn(line.rstrip('\n') + "\r")
        Cursor.down(diff)
        line_num = line_num + 1
        time.sleep(0.0015)

Cursor.up(step)
clear_display()