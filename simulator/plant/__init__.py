from .. import functions
from . import forces
from . import torque

def step(rockstate, envstate, dt):
    """
    :param rockstate: the current state off the rocket (type RocketState)
    :param envstate: the current state of the environment (type EnvironmentState)
    :param dt: the amount of time to step forward in seconds
    :return: The predicted state of the rocket after time dt with appropriate
        effects of the environment and motor applied to it
    """
    # TODO fill these in
    aoa = 0
    mach = 0
    rey = 0
    roll_axis = envstate.ref_roll
    abrakes = rockstate.abrake_current
    force_eq = lambda v: \
            forces.axial(v, aoa, mach, rey, roll_axis, rockstate.abrake_extension) \
            + forces.normal(v, aoa, mach, rey, roll_axis) \
            + forces.thrust(envstate.time) \
            + forces.gravity(position[2], MAX)

    vn, xn = RK_force(force_eq, rockstate.get_velo(), rockstate.position, dt)


def RK4(equation, state, dt, time=0):
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
    yk = state + (1.0/6) * (k1 + 2*k2 + 2*k3 + k4)
    return yk

def RK_force(equation, velocity, position, dt):
    k1v = dt * equation(velocity)
    k1x = dt * velocity
    k2v = dt * equation(velocity + k1v/2)
    k2x = dt * (velocity + k1v/2)
    k3v = dt * equation(velocity + k2v/2)
    k3x = dt * (velocity + k2v/2)
    k4v = dt * equation(velocity + k3v)
    k4x = dt * (velocity + k3v)

    v_next = velocity + (1/6)*(k1v + 2*k2v + 2*k3v + k4v)
    x_next = position + (1/6)*(k1x + 2*k2x + 2*k3x + k4x)
    return v_next, x_next
