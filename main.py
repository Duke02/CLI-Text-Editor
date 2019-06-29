from window import Window
from time import sleep
import curses

def main(curses_window):
	my_window = Window('~', curses_window)

	is_running = True

	while is_running:
		my_window.update()
		user_input = my_window.get_user_input()
		if user_input == my_window.exit_key:
			is_running = False
		else:
			my_window.add_character(user_input)

if __name__ == "__main__":
	curses.wrapper(main)
