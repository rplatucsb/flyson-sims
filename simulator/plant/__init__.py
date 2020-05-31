def step(rockstate, envstate, dt):
    """
    :param rockstate: the current state off the rocket (type RocketState)
    :param envstate: the current state of the environment (type EnvironmentState)
    :param dt: the amount of time to step forward in seconds
    :return: The predicted state of the rocket after time dt with appropriate
        effects of the environment and motor applied to it
    """
    raise NotImplementedError
