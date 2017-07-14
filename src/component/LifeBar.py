from cocos.layer import Layer, pyglet
from cocos.sprite import Sprite


class LifeBar(Layer):

    def __init__(self):
        super(Layer, self).__init__()
        self.nb_pixels = 40
        self.set_sprites()
        self.fill_life()

    def draw(self):
        super(LifeBar, self).draw()

    def fill_life(self):
        self.set_heart(1, self.full_heart)
        self.set_heart(2, self.full_heart)
        self.set_heart(3, self.full_heart)

    def set_heart(self, position, elem):
        sprite = Sprite(elem)
        sprite.scale = 2
        sprite.position = self.nb_pixels * position, 15
        self.add(sprite)

    def set_sprites(self):
        heart_models = pyglet.image.load('images/heartsupdated.png')
        hearts_grid = pyglet.image.ImageGrid(heart_models, 3, 1)
        self.full_heart = hearts_grid[2]
        self.half_heart = hearts_grid[1]
        self.empty_heart = hearts_grid[0]
