from cocos.layer import Layer
from pyglet.window import key
from pyglet.window.key import KeyStateHandler


class GameController(Layer):
    is_event_handler = True  #: enable pyglet's events

    def __init__(self, model):
        super(GameController, self).__init__()
        self.model = model
        self.keys = KeyStateHandler()

    def on_key_press(self, symbol, modifiers):
        self.keys[symbol] = True
        print("Key pressed !")
        print(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.keys[symbol] = False
        print("Key released !")
        print(symbol, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.keys[key.LEFT]:
            print("left !")
