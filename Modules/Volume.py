from pynput.keyboard import Key,Controller

def volume_up():
    keyboard = Controller()
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)


def volume_down():
    keyboard = Controller()
    keyboard.press(Key.media_volume_down)
    keyboard.release(Key.media_volume_down)
    keyboard.press(Key.media_volume_down)
    keyboard.release(Key.media_volume_down)
