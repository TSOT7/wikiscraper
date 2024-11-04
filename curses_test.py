import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Print text in the middle of the screen
    height, width = stdscr.getmaxyx()
    text = "Hello, Curses!"
    x = width // 2 - len(text) // 2
    y = height // 2
    stdscr.addstr(y, x, text)

    # Refresh to render text
    stdscr.refresh()

    # Wait for a key press before exiting
    stdscr.getch()

# Start the curses application
curses.wrapper(main)