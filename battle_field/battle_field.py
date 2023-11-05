from vessel.vessel import Vessel


class BattleSpace:
    def __init__(self):
        self.space = {}

    def add_ship(self, ship):
        if (ship.x, ship.y, ship.z) in self.space:
            return False
        total_hits = sum(s.max_hits for s in self.space.values()) + ship.max_hits
        if total_hits <= 22:
            self.space[(ship.x, ship.y, ship.z)] = ship
            return True
        return False

    def receive_hit(self, x, y, z):
        if (x, y, z) in self.space:
            ship = self.space[(x, y, z)]
            ship.hits += 1
            if ship.hits >= ship.max_hits:
                del self.space[(x, y, z)]
            return True
        return False
