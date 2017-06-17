from cocos.layer import *
from cocos.text import *
from ..Status import status
from src.component import ProgressBar


class ScoreLayer(Layer):
    def __init__(self):
        w, h = director.get_window_size()
        super(ScoreLayer, self).__init__()

        # transparent layer
        self.add(ColorLayer(100, 100, 200, 100, width=w, height=48), z=-1)

        self.position = (0, h - 48)

        progress_bar = self.progress_bar = ProgressBar(width=200, height=20)
        progress_bar.position = 20, 15
        self.add(progress_bar)
        self.score = Label('Score:', font_size=24,
                           font_name='Edit Undo Line BRK',
                           color=(255, 255, 255, 255),
                           anchor_x='left',
                           anchor_y='bottom')
        self.score.position = (w / 2, 8)
        self.add(self.score)

    def draw(self):
        super(ScoreLayer, self).draw()
        self.score.element.text = 'Score: %d' % status.score
