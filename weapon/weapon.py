class Weapon:
    def __init__(self, munitions: int, range: int):
        self.munitions = munitions
        self.range = range

    def fire_at(self, x: int, y: int, z: int):
        pass

    def is_valid_target(self, x, y, z):
        pass


class Lance_missiles_antisurface(Weapon):
    pass


class AntiAirMissile(Weapon):
    pass


class Lance_torpilles(Weapon):
    pass
