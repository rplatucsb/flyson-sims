from .rockstate import RocketState
from .envstate import EnvironmentState

class SimIter:
    envstate = EnvironmentState()
    rockstate = RocketState()

    def __iter__(self):
        # do controls
        # propagate airbrakes
        # propagate environment
        return rockstate

    def next(self):
        raise StopIteration
        return
