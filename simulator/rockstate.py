import numpy as np

class RocketState(np.ndarray):
    """
    Stores information about the current state of the rocket
    Just an ndarray with some helfpul access wrappers + coord transforms
    """
    def __new__(): # need to use new bc ndarrays are immutable
        pass
