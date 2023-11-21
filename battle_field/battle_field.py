from vessel.vessel import Vessel


class BattleField:
    def __init__(self):
        self.vessels = []  
    def add_vessel(self, vessel):
        self.vessels.append(vessel)