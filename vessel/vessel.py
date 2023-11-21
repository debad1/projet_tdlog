from weapon.weapon import Weapon
import math
import sys


class Vessel:
    def __init__(self,coordinates:tuple ,max_hits:int , weapon:Weapon,battle_simulator):
        self.coordinates=coordinates
        self.max_hits=max_hits
        self.weapon=weapon
        self.hits= 0
        self.battle_simulator = battle_simulator
    def reduce_max_hits(self):
        if self.max_hits > 0:
            self.max_hits -= 1
        else :
            return("error")
    def go_to(self,x,y,z):
        self.coordinates = (x, y, z)

    def get_coordinates(self,x:int,y:int,z:int):
        return(self.coordinates)
    def get_target_vessel(self, x, y, z):
        # Parcourez la liste des Vessels pour trouver la cible en fonction des coordonnées
        for vessel in battle_simulator.vessels:  # Assurez-vous que battle_simulator est accessible
            if (vessel.coordinates == (x, y, z)) and (vessel != self):
                return vessel
        return None
    def is_valid_target(self,x,y,z):
        pass
    def fire_at(self,x,y,z):
        if self.max_hits==0:
            return("Vessel is destroyed")
        elif self.weapon.ammunitions==0:
            return("No more ammunitions")
        elif self.calculate_distance(x,y,z) > self.weapon.range or not self.is_valid_target(x,y,z):
            self.weapon.ammunitions -= 1
            return("Loin de vision or not valid target ")
        else:
            # Réduire le max_hits de la Vessel attaquée
            target_vessel = self.get_target_vessel(x, y, z)
            if target_vessel:
                target_vessel.reduce_max_hits()
            else:
                return "Target Vessel not found"
            
    def calculate_distance(self, x, y, z):
        x1, y1, z1 = self.coordinates
        return (sqrt((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2))