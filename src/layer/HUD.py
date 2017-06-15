from cocos.layer import *
from .MessageLayer import MessageLayer
from .ScoreLayer import ScoreLayer


class HUD(Layer):
    def __init__(self):
        super(HUD, self).__init__()
        self.score_layer = ScoreLayer()
        self.add(self.score_layer)
        self.add(MessageLayer(), name='msg')

    def show_message(self, msg, callback=None, msg_duration=1):
        self.get('msg').show_message(msg, callback, msg_duration)

    def set_objectives(self, objectives):
        self.score_layer.set_objectives(objectives)

    def update_time(self, time_percent):
        self.score_layer.progress_bar.set_progress(time_percent)
