from weapon.weapon import Weapon


class Lance_torpilles(Weapon):
    def __init__(self):
        super().__init__(munitions = 24, range = 40)

