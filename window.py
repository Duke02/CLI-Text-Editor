import curses
from curses.textpad import Textbox

class Window:
	def __init__(self, exit_key, curses_window):
		self.screen = curses.initscr()
		self.height, self.width = self.screen.getmaxyx()
		self.window = curses_window
		self.window.nodelay(False)
		self.textbox = Textbox(self.window)
		self.exit_key = exit_key

	def get_user_input(self):
		return self.screen.getkey()

	def close(self):
		curses.endwin()

	def update(self):
		self.screen.refresh()

	def timeout(self, amount):
		self.window.timeout(amount)

	def add_character(self, char):
		cursor_y, cursor_x = self.window.getyx()
		self.screen.addstr(cursor_y, cursor_x, char)
