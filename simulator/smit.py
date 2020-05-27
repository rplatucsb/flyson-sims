from .rocket import RocketState
from .env import Environment
class SimIter:

    env = Environment()
    rockstate = RocketState()

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration
        return
