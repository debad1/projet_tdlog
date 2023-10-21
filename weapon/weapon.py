
#class Weapon:
#    def __init__(self,ammunitions :int,range:int):
#        self.ammunitions=ammunitions
#        self.range=range
#
#    def fire_at(self,x:int,y:int,z:int) :
#        if self.ammunitions<=0:
#            return("NoAmmunitionError")
#        
#        elif self.is_valid_target(x, y, z):
#            self.ammunitions -= 1
#            return f"Firing at target ({x}, {y}, {z})"
        
#        else:
#            return("OutOfRangeError")
#            self.ammunitions -= 1

#    def is_valid_target(self, x, y, z):
#        pass

#class Lance_missiles_antisurface(Weapon):

#    def __init__(self):
#        super().__init__(ammunitions=50,range=100)
#    #def is_valid_target(self, x, y, z):
             
#class AntiAirMissile(Weapon):
#    def __init__(self):
#        super().__init__(ammunition=40, range=20)

#    def is_valid_target(self, x, y, z):
#        return z > 0
#class Lance_torpilles(Weapon):
#    def __init__(self):
#        super().__init__(ammunition=24, range=40)

#    def is_valid_target(self, x, y, z):
#        return z <= 0



            
