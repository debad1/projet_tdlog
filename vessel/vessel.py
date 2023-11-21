from weapon.weapon import Weapon
from math import sqrt


class Vessel:
    def __init__(self, coordinates: tuple, max_hits: int, weapon: Weapon):
        self.coordinates = coordinates
        self.max_hits = max_hits
        self.weapon = weapon
        self.hits = 0

    def go_to(self, x, y, z):
        self.coordinates = (x, y, z)

    def get_coordinates(self):
        return self.coordinates

    def is_valid_target(self, x, y, z):
        pass

    def fire_at(self, x, y, z):
        if self.max_hits == 0:
            return "Vessel is destroyed"
        elif self.weapon.munitions == 0:
            return "No more munitions"
        elif self.calculate_distance(x, y, z) > self.weapon.range or not self.is_valid_target(x, y, z):
            self.weapon.munitions -= 1
            return "Loin de vision or not valid target"

    def calculate_distance(self, x, y, z):
        x1, y1, z1 = self.coordinates
        return sqrt((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2)

    def get_target_vessel(self, x, y, z):
        # Parcourez la liste des Vessels pour trouver la cible en fonction des coordonnées
        for vessel in battle_simulator.vessels:  # Assurez-vous que battle_simulator est accessible
            if (vessel.coordinates == (x, y, z)) and (vessel != self):
                return vessel
        return None

