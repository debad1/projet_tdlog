# Unit tests using pytest
import pytest

from battle_field.battle_field import BattleSpace


def test_add_ship():
    space = BattleSpace()
    ship1 = Ship(10, 20, 1, 5)
    ship2 = Ship(30, 40, 0, 8)
    assert space.add_ship(ship1) == True
    assert space.add_ship(ship2) == True
    assert space.add_ship(ship1) == False  # Ship already present
    ship3 = Ship(15, 25, 1, 10)
    assert space.add_ship(ship3) == False  # Total max_hits > 22


def test_receive_hit():
    space = BattleSpace()
    ship1 = Ship(10, 20, 1, 5)
    ship2 = Ship(30, 40, 0, 8)
    space.add_ship(ship1)
    space.add_ship(ship2)
    assert space.receive_hit(10, 20, 1) == True
    assert space.receive_hit(10, 20, 1) == False  # Ship already destroyed
    assert space.receive_hit(30, 40, 0) == True
    assert space.receive_hit(5, 5, 1) == False  # No ship at the coordinates


if __name__ == '__main__':
    pytest.main()