from pynput import keyboard

def on_press(key):
    try:
        print(key.char)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

listener = keyboard.Listener(
    on_press=on_press)
listener.start()