import pyglet
from cocos.director import director
from cocos.menu import *
from cocos.scenes.transitions import *


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__('Touhou')

        self.font_title['font_name'] = 'Edit Undo Line BRK'
        self.font_title['font_size'] = 72
        self.font_title['color'] = (204, 164, 164, 255)

        self.font_item['font_name'] = 'Edit Undo Line BRK',
        self.font_item['color'] = (32, 16, 32, 255)
        self.font_item['font_size'] = 32
        self.font_item_selected['font_name'] = 'Edit Undo Line BRK'
        self.font_item_selected['color'] = (32, 100, 32, 255)
        self.font_item_selected['font_size'] = 46

        # example: menus can be vertical aligned and horizontal aligned
        self.menu_anchor_y = CENTER
        self.menu_anchor_x = CENTER

        items = [MenuItem('New Game', self.on_new_game),
                 MenuItem('Quit', self.on_quit)]

        self.create_menu(items, shake(), shake_back())

    def on_new_game(self):
        import src.view
        director.push(FlipAngular3DTransition(src.view.get_newgame(), 1.5))

    def on_quit(self):
        pyglet.app.exit()
