from time import sleep
from ewmh import EWMH
from Xlib import display, protocol, X
from Xlib.protocol.request import *
ewmh = EWMH()
disp = display.Display()
poll_interval = 0.025 # s
poll_attempts_limit = 10
def unmaximize(window):
  ewmh.setWmState(window, 0, "_NET_WM_STATE_MAXIMIZED_VERT")
  ewmh.setWmState(window, 0, "_NET_WM_STATE_MAXIMIZED_HORZ")
  for client in all_win:
    unmaximize(client.window)
  ewmh.display.flush()
  for client in all_win:
    client.xwin.unmap() 
  poll_attempts = 0
  for client in all_win:
    while client.xwin.get_attributes().map_state == X.IsViewable \
      and poll_attempts < poll_attempts_limit:
      sleep(poll_interval)
      poll_attempts += 1
  for client in all_win:
    client.xwin.map()   
  poll_attempts = 0
  for client in all_win:
    while client.xwin.get_attributes().map_state != X.IsViewable \
      and poll_attempts < poll_attempts_limit:
      sleep(poll_interval)
      poll_attempts += 1

http://downloads.sourceforge.net/project/python-xlib/python-xlib/0.14/python-xlib-0.14.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fpython-xlib%2Ffiles%2Fpython-xlib%2F0.14%2F&ts=1462563851&use_mirror=liquidtelecom