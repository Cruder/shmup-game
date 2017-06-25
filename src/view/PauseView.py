import cocos
from cocos.director import director
from cocos.scene import Scene
from src.layer import HUD
from cocos.menu import *
import pyglet

from src.model import LevelModel
from src.controller import GameController

__all__ = ['game_pause']


class PauseView(Menu):
    is_event_handler = True  # enable director.window events

    def __init__(self):
        super(PauseView, self).__init__('Pause')
        # model.set_view(self)

        items = [MenuItem('Continue', self.on_continue_game),
                 MenuItem('Quit', self.on_quit)]

        self.create_menu(items, shake(), shake_back())

    def on_continue_game(self):
        director.pop()

    def on_quit(self):
        director.pop()
        director.pop()


def game_pause():
    scene = Scene()
    view = PauseView()
    scene.add(view, z=2, name="view")
    return scene
