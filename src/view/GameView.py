import cocos
from cocos.director import director
from cocos.scene import Scene
from src.layer import HUD

from src.model import LevelModel
from src.controller import GameController
import pyglet

__all__ = ['get_newgame']


class GameView(cocos.layer.ColorLayer):
    def __init__(self, model, hud):
        super(GameView, self).__init__(64, 64, 224, 0)
        model.set_view(self)
        self.hud = hud
        self.model = model
        self.model.push_handlers(self.on_update_time
                                 , self.on_game_over
                                 , self.on_level_completed)
        self.model.start()
        self.hud.show_message('GET READY')

    def on_update_time(self, time_percent):
        print("Update time?")
        self.hud.update_time(time_percent)

    def on_game_over(self):
        self.hud.show_message('GAME OVER', msg_duration=3, callback=lambda: director.pop())

    def on_level_completed(self):
        self.hud.show_message('LEVEL COMPLETED', msg_duration=3, callback=lambda: self.model.set_next_level())


def get_newgame():
    scene = Scene()
    model = LevelModel()
    controller = GameController(model)
    # view
    hud = HUD()
    view = GameView(model, hud)

    # set controller in model
    model.set_controller(controller)

    scene.add(controller, z=1, name="controller")
    scene.add(view,       z=2, name="view")
    scene.add(hud,        z=3, name="hud")

    return scene
