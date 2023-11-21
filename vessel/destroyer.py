from vessel.vessel import Vessel
from weapon.lance_torpilles import Lance_torpilles


class Destroyer(Vessel):
    def __init__(self, coordinates):
        super().__init__(coordinates = coordinates, max_hits = 4, weapon = Lance_torpilles())

    def go_to(self, x, y, z):
        if z == 1:
            self.coordinates = (x, y, z)
        else:
            return "Invalid coordinates"

    def fire_at(self, x, y, z):
        if self.max_hits == 0:
            return "The Vessel is destroyed and cannot fire"

        if self.calculate_distance(x, y, z) > self.weapon.range:
            return "The target is out of range"

        if self.weapon.munitions > 0:
            self.weapon.munitions -= 1
            self.max_hits -= 1
            return f"Successful shot at the target at position ({x}, {y}, {z})"
        else:
            return "No munitions."

class Me:
    pass