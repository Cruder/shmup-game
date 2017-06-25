from cocos.layer import *


class BackgroundLayer(Layer):
    def __init__(self, mediaPath):
        super(BackgroundLayer, self).__init__()

        source = pyglet.media.load(mediaPath)
        format = source.video_format
        if not format:
            print('No video track in this source.')
            return

        self.media_player = pyglet.media.Player()
        self.media_player.queue(source)
        self.media_player.play()

    def draw(self):
        self.media_player.get_texture().blit(0, 0)
