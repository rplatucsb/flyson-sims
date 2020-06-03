from .rockstate import RocketState
from .envstate import EnvironmentState
from . import plant
from . import controller

class SimIter:
    """
    The main loop of the simulator, implemented as an iterator for increased
    flexibility.
    """
    envstate = EnvironmentState()
    rockstate = RocketState()
    time = 0
    dt = 0.01  # small timestep

    def __iter__(self):
        return self

    def next(self):
        """
        :return: the state of the rocket at time t + dt
        side effects: advances time to t + dt
        """
        self.rockstate = plant.step(self.rockstate, self.envstate, self.dt)
        abrake_amps = controller.sysinput(self.rockstate)
        self.rockstate = plant.abrakes.step(self.rockstate)
        return self.rockstate
