from unittest import TestCase

from vessel.destroyer import Destroyer


class TestFrigate(TestCase):

    def test_fire_at(self):
        coordinates = (2, 3, 6)
        destroyer = Destroyer(coordinates)
        destroyer.fire_at(2, 3, 4)
        self.assertEqual(23, destroyer.weapon.munitions)
