from vessel.vessel import Vessel
from weapon.lance_missiles_anti_air import Lance_missiles_anti_air


class Cruiser(Vessel):
    def __init__(self, coordinates):
        weapon = Lance_missiles_anti_air()
        super().__init__(coordinates, max_hits = 6, weapon = weapon)

    def go_to(self, x, y, z):
        if not self.is_valid_move(x, y, z):
            return "movement invalid"
        self.coordinates = (x, y, z)

    def is_valid_move(self, x, y, z):
        return z == 0

    def is_valid_target(self, x, y, z):
        return self.z > 0

    def fire_at(self, x, y, z):
        if self.max_hits == 0:
            return "Vessel is destroyed"
        elif self.weapon.munitions == 0:
            return "No more munitions"
        elif self.calculate_distance(x, y, z) > self.weapon.range or not self.is_valid_target(x, y, z):
            self.weapon.munitions -= 1
            return "Loin de vision or not valid target "
        else:
            pass  # on doit diminuer de max_hits de vessel attaqué
