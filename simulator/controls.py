from .rocket import RocketState

class Controller:
    history = [RocketState()]
    def __call__(self, rs) -> RocketState:
        return motor_powers
