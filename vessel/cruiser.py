from vessel.vessel import Vessel
from weapon.lance_missiles_anti_air import Lance_missiles_anti_air


class Cruiser(Vessel):
    def __init__(self, coordinates):
        weapon = AntiAirMissile()
        super().__init__(coordinates, max_hits=6, weapon=weapon)

    def go_to(self, x, y, z):
        for vessel in battle_simulator.vessels:
            if not self.is_valid_move(x, y, z):
                return("mouvement invalide")
                sys.exit()
            elif vessel.coordinates == (x, y, z) and (vessel != self):
                return("mouvement invalide")
                sys.exit()
            else:
                self.coordinates=(x,y,z)    

    def is_valid_move(self, x, y, z):
        return (z == 0)
    def is_valid_target(self,x,y,z):
        return self.z > 0 #
    def fire_at(self,x,y,z):
        if self.max_hits==0:
            return("Vessel is destroyed")
        elif self.weapon.ammunitions==0:
            return("No more ammunitions")
        elif self.calculate_distance > self.weapon.range or not self.is_valid_target(x,y,z):
            self.weapon.ammunitions -= 1
            return("Loin de vision or not valid target ")
        else:
            target_vessel = self.get_target_vessel(x, y, z)
            if target_vessel:
                target_vessel.reduce_max_hits(1)
            else:
                return "Target Vessel not found"