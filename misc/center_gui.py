import ctypes
import os


def center_screen(gui_dim):
    # centers the pygame gui in the middle of the screen
    screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
    x, y = screensize[0] // 2 - gui_dim[0] // 2, (screensize[1] - gui_dim[1]) // 2
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

