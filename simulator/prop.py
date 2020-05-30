
class Propagator:

    def env(self):
        return delta_state

    def motors(self, controller):
        return delta_state

    def __call__(self, rs, env, c) -> RocketState, Environment, Controller:
        return RocketState()
