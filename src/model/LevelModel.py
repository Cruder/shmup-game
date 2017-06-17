import pyglet


__all__ = ['LevelModel']


class LevelModel(pyglet.event.EventDispatcher):
    def __init__(self):
        super(LevelModel, self).__init__()
        self.controller = None
        self.view = None

    def start(self):
        pass

    def time_tick(self, delta):
        print("tick")
        pass

    def set_controller(self, controller):
        self.controller = controller

    def set_view(self, view):
        self.view = view

LevelModel.register_event_type('on_update_time')
LevelModel.register_event_type('on_game_over')
LevelModel.register_event_type('on_level_completed')
