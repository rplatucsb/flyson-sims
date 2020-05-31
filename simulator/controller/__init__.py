def sysinput(rockstate):
    """
    Sysinput determines the optimal input to the system based on the current
    measured state of the rocket.

    :param rockstate: state of the rocket
    :return: ndarray(double) 3-vec the desired current through each servo
    """
    raise NotImplementedError
