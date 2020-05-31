from .rockstate import RocketState
from .envstate import EnvironmentState

import motor
import controller
import airbrakes

class SimIter:
    """
    The main loop of the simulator, implemented as an iterator for increased
    flexibility.
    """
    envstate = EnvironmentState()
    rockstate = RocketState()
    time = 0
    dt = 0 # small timestep

    def __iter__(self):
        # do controls
        # propagate airbrakes
        # propagate environment
        
        self.rockstate = plant.step(self.rockstate, self.envstate, self.dt)
        abrake_amps = controller.sysinput(self.rockstate)
        self.rockstate = abrakes.step(self.rockstate)
        return self.rockstate

    def next(self):
        """
        :return: the state of the rocket at time t + dt
        side effects: advances time to t + dt
        """
        raise StopIteration
        return
