from weapon.weapon import Weapon


class Lance_missiles_anti_surface(Weapon):
    def __init__(self):
        super().__init__(munitions = 50, range = 100)

