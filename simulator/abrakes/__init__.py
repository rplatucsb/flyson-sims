

def step(rockstate):
    """
    :param rockstate: the current state of the rocket
    :return: a rocket state after the propagation of motor current into airbrake
        extension
    """
    # FIXME It could be the case that this needs the environment force to calc,
    # in which case it should be moved to plant
    raise NotImplementedError
