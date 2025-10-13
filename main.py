#!/usr/bin/env python

"""
main.py - Main entry point for the spirograph application.
By default, runs the Pygame GUI. Future: add browser (p5.js) mode.
"""

try:
    from gui import run_gui
except:
    from .gui import run_gui
from traceback import format_exc

def main():
    try:
        run_gui()
    except:
        print("Unable to start pygame gui")
        print(format_exc())

if __name__ == "__main__":
    main()



