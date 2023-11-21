from unittest import TestCase

from vessel.aircraft import Aircraft


class TestFrigate(TestCase):

    def test_fire_at(self):
        coordinates = (2, 3, 6)
        aircraft = Aircraft(coordinates)
        aircraft.fire_at(2, 3, 4)
        self.assertEqual(49, aircraft.weapon.munitions)
        print("bon")
