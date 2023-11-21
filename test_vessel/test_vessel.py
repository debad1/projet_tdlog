from unittest import TestCase

from vessel.vessel import Vessel
from weapon.weapon import Weapon


class TestVessel(TestCase):

    def test_fire_at(self):
        coordinates = (2, 3, 6)
        weapon = Weapon(30, 5)
        vessel = Vessel(coordinates, 40, weapon)
        vessel.fire_at(2, 3, 4)
        self.assertEqual(29, weapon.munitions)

    def test_fire_at_out_of_range(self):
        coordinates = (2, 3, 6)
        weapon = Weapon(30, 5)
        vessel = Vessel(coordinates, 40, weapon)
        return_value = vessel.fire_at(40, 50, 4)
        self.assertEqual(29, weapon.munitions)
        self.assertEqual("Loin de vision or not valid target", return_value)
