from os.path import exists, join

import pyglet.resource
import os.path
from cocos import director
from cocos.scene import Scene
from cocos.layer import MultiplexLayer
from .menu import MainMenu
from .layer import BackgroundLayer


def run():
    script_dir = os.path.dirname(os.path.realpath(__file__))

    pyglet.resource.path = [join(script_dir, '../')]
    pyglet.resource.reindex()

    director.director.init(caption="Touhou Game", fullscreen=True)

    scene = Scene()
    scene.add(BackgroundLayer('./videos/Touhou-Animated-Wallpaper.m4v'), z=1)
    scene.add(MultiplexLayer(MainMenu()), z=1)

    director.director.run(scene)
