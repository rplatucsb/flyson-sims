def step(rockstate, envstate, dt):
    """
    :param rockstate: the current state off the rocket (type RocketState)
    :param envstate: the current state of the environment (type EnvironmentState)
    :param dt: the amount of time to step forward in seconds
    :return: The predicted state of the rocket after time dt with appropriate
        effects of the environment and motor applied to it
    """
    raise NotImplementedError

def RK4(equation, state, time, dt):
    """
    :param equation: function in the form y' = f(t,y), that describes the change in some variable
    :param state: the current value of some variable in the rocket state at time t
    :param time: the current time, t
    :param dt: the time step for the integrator
    :return: the new value for the variable at time t + dt
    """
    k1 = dt * equation(time, state)
    k2 = dt * equation(time + (dt/2), state + (k1/2))
    k3 = dt * equation(time + (dt/2), state + (k2/2))
    k4 = dt * equation(time + dt, state + k3)
    yk = (1.0/6) * (k1 + 2*k2 + 2*k3 + k4)
    return yk
