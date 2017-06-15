from cocos.layer import *
from cocos.text import *
from cocos.actions import *


class MessageLayer(Layer):
    def show_message(self, msg, callback=None, msg_duration=1):
        w, h = director.get_window_size()

        self.msg = Label(msg,
                         font_size=52,
                         font_name='Edit Undo Line BRK',
                         anchor_y='center',
                         anchor_x='center')
        self.msg.position = (w // 2.0, h)

        self.add(self.msg)

        actions = Accelerate(MoveBy((0, -h / 2.0), duration=msg_duration / 2))
        actions += \
            Delay(1) + \
            Accelerate(MoveBy((0, -h / 2.0), duration=msg_duration / 2)) + \
            Hide()

        if callback:
            actions += CallFunc(callback)

        self.msg.do(actions)
