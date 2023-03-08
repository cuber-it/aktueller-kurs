import curses as wc


def main(stdscr):
    # Set up curses
    wc.curs_set(0) # Hide the cursor
    stdscr.nodelay(1) # Make getch() non-blocking

    # Clear the screen and draw a border
    stdscr.clear()
    stdscr.border()

    # Main loop
    while True:
        # Check for user input
        key = stdscr.getch()

        if key == ord('q'): # Quit if user presses 'q'
            break

        # Clear the screen and draw a border
        stdscr.clear()
        stdscr.border()

        # Draw a message in the middle of the screen
        message = "Press 'q' to quit"
        y, x = stdscr.getmaxyx()
        stdscr.addstr(int(y/2), int(x/2 - len(message)/2), message)

        # Refresh the screen
        stdscr.refresh()

if __name__ == '__main__':
    # Set up the curses screen
    wc.wrapper(main)
