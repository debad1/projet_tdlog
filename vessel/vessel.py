import random as rd
from weapon import Weapon
import math
import sqrt 
class Vessel:
    def __init__(self,coordinates:tuple ,max_hits:int , weapon:Weapon):
        self.coordinates=coordinates
        self.max_hits=max_hits
        self.weapon=weapon
        self.hits= 0

    def go_to(self,x,y,z):
        self.coordinates = (x, y, z)
        
    def get_coordinates(self,x:int,y:int,z:int):
        return(self.coordinates)
    def is_valid_target(self,x,y,z):
        pass
    def fire_at(self,x,y,z):
        if self.max_hits==0:
            return("Vessel is destroyed")
        elif self.weapon.ammunitions==0:
            return("No more ammunitions")
        elif self.calculate_distance > self.weapon.range or not self.is_valid_target(x,y,z):
            self.weapon.ammunitions -= 1
            return("Loin de vision or not valid target ")
        else:
            pass    
    def calculate_distance(self, x, y, z):
        x1, y1, z1 = self.coordinates
        return (sqrt((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2))
    
class Cruiser(Vessel):
    def __init__(self, coordinates):
        weapon = AntiAirMissile()
        super().__init__(coordinates, max_hits=6, weapon=weapon)

    def go_to(self, x, y, z):
        if not self.is_valid_move(x, y, z):
            return("mouvement invalide")
        self.coordinates = (x, y, z)    

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
            pass # on doit diminuer de max_hits de vessel attaqué 
class Submarine(Vessel):
    def __init__(self, coordinates):
        weapon = Lance_torpilles()
        super().__init__(coordinates, max_hits=2, weapon=weapon)

    def is_valid_move(self, x, y, z):
        return z == 0 or z == -1
    def go_to(self, x, y, z):
        if not self.is_valid_move(x, y, z):
            return("mouvement invalide")
        self.coordinates = (x, y, z)
    def is_valid_target(self,x,y,z):
        self.z <= 0    
    def fire_at(self,x,y,z):
        if self.max_hits==0:
            return("Vessel is destroyed")
        elif self.weapon.ammunitions==0:
            return("No more ammunitions")
        elif self.calculate_distance > self.weapon.range or not self.is_valid_target(x,y,z):
            self.weapon.ammunitions -= 1
            return("Loin de vision or not valid target ")
        else:
            pass 
        # on doit diminuer de max_hits de vessel attaqué  

#o	Missile anti-air : z > 0
#o	Torpille : z <= 0
