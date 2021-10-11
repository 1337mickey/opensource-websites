# Keyboard module in Python
import keyboard

# It records all the keys until home is pressed
rk = keyboard.record(until='home')

# It replay back the all keys
keyboard.play(rk, speed_factor=1000)
