from unittest import TestCase

from vessel.frigate import Frigate


class TestFrigate(TestCase):

    def test_fire_at(self):
        coordinates = (2, 3, 6)
        frigate = Frigate(coordinates)
        frigate.fire_at(2, 3, 4)
        self.assertEqual(49, frigate.weapon.munitions)
