__all__ = ['status']


class Status(object):
    def __init__(self):
        # current score
        self.score = 0

    def reset(self):
        self.score = 0

status = Status()
