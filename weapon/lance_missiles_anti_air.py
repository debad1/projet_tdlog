from weapon.weapon import Weapon


class Lance_missiles_anti_air(Weapon):
    def __init__(self):
        super().__init__(munitions = 40, range = 20)


