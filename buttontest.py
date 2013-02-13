import curses
import RPi.GPIO as GPIO

GPIO.setup(18, GPIO.IN)
GPIO.setup(22, GPIO.IN)

stdscr=curses.initscr()
stdscr.nodelay(1)
curses.noecho()

while 1:
  stdscr.addstr(0, 0, "Button 1 is")
  stdscr.addstr(0, 20, "Button 2 is")

  if GPIO.input(18):
    stdscr.addstr(0, 12, "DOWN")
  else:
    stdscr.addstr(0, 12, "UP  ")

  if GPIO.input(22):
    stdscr.addstr(0, 32, "UP  ")
  else:
    stdscr.addstr(0, 32, "DOWN")

  stdscr.addstr(1, 0, "")
  stdscr.refresh()

  if stdscr.getch() == ord('q'):     # Press q to quit
    break
