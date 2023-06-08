from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Listener
import time
import threading

class ClickMouse(threading.Thread):
    def __init__(self):
        super(ClickMouse, self).__init__()
        self.mouse = MouseController()
        self.clicking = False
        self.running = True

    def run(self):
       	print('AutoClicker is running.')
       	while self.running:
       	    if self.clicking:
                self.mouse.click(Button.left, 1)
                print('AutoClicker is clicking.')
                time.sleep(0.05) # pause for 0.5 seconds

    def stop_clicking(self):
        self.running = False
        print('AutoClicker has stopped.')

def on_press(key):
    if key == Key.f2: # using function keys to start and stop auto clicking
        if auto_clicker.clicking:
        	print('AutoClicker has stopped clicking.')
        	auto_clicker.clicking = False
        else:
        	print('AutoClicker has started clicking.')
        	auto_clicker.clicking = True
    elif key == Key.f3: # using function keys to stop the program
        auto_clicker.stop_clicking()
        listener.stop()

if __name__ == "__main__":
    auto_clicker = ClickMouse()
    auto_clicker.start()  # Start the auto clicker thread
    with Listener(on_press=on_press) as listener:
    	print('Listener is running.')
    	listener.join()
    auto_clicker.join()