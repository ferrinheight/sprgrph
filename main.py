#!/usr/bin/env python

"""
main.py - Main entry point for the spirograph application.
By default, runs the Pygame GUI. Future: add browser (p5.js) mode.
"""

def main():
    """
    Main entry point for the spirograph application.
    By default, runs the Pygame GUI. Future: add browser (p5.js) mode.
    """
    from gui import run_gui
    run_gui()
    # Placeholder for browser version (p5.js)
    # def run_browser():
    #     pass
    # To add: CLI argument to select mode

if __name__ == "__main__":
    main()



