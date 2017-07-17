from cocos.layer import Layer, pyglet
from cocos.sprite import Sprite


class LifeBar(Layer):

    def __init__(self):
        super(Layer, self).__init__()
        self.nb_pixels = 40
        self.MAX_LIFE = 6
        self.nb_life = self.MAX_LIFE
        self.set_sprites()
        self.fill_life(self.full_heart)

    def draw(self):
        super(LifeBar, self).draw()

    def fill_life(self, heart_state):
        for i in range(0, (self.MAX_LIFE // 2)):
            self.set_heart((i + 1), heart_state)

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

    def add_life(self, life_points):
        if self.nb_life + life_points > self.MAX_LIFE:
            self.nb_life = self.MAX_LIFE
        elif self.nb_life + life_points < 0:
            self.nb_life = 0
        else:
            self.nb_life += life_points
        self.update_hearts()

    def update_hearts(self):
        self.fill_life(self.empty_heart)
        nb_full = self.nb_life // 2
        position = 1
        # put full hearts
        for i in range(1, (nb_full + 1)):
            self.set_heart(position, self.full_heart)
            position += 1
        # put potential half heart
        if self.nb_life % 2 != 0:
            self.set_heart(position, self.half_heart)
