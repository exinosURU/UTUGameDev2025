# lógica central del juego Elevator Action.
# escenas, entidades y reglas de victoria/derrota.


from Elevator_Action.scenes import ElevatorActionScene

class Juego:
    def __init__(self):
        self.escena_actual = ElevatorActionScene()

    def update(self, dt: float):
        self.escena_actual.update(dt)

    def draw(self, screen):
        self.escena_actual.draw(screen)
