from core import *


def test_new_gladiator():
    assert new_gladiator(100, 0, 10, 25) == {
        'health': 100,
        'rage': 0,
        'damage_low': 10,
        'damage_high': 25,
    }


def test_is_dead():
    gladiator = new_gladiator(100, 0, 10, 25)
    assert is_dead(gladiator) == False

    gladiator['health'] = 0
    assert is_dead(gladiator) == True


def test_heal():
    user_b = new_gladiator(50, 25, 20, 55)
    heal(user_b)
    assert user_b == {
        'health': 55,
        'rage': 15,
        'damage_low': 20,
        'damage_high': 55
    }


def test_heal_no_rage():
    user_b = new_gladiator(50, 5, 20, 55)
    heal(user_b)
    assert user_b == {
        'health': 50,
        'rage': 0,
        'damage_low': 20,
        'damage_high': 55
    }


def test_attack_no_highlow():
    attacker = new_gladiator(100, 0, 15, 15)
    defender = new_gladiator(100, 0, 15, 15)
    attack(attacker, defender)

    assert attacker['rage'] == 15
    assert defender['health'] == 85


def test_attack_rage():
    attacker = new_gladiator(100, 100, 15, 15)
    defender = new_gladiator(100, 0, 15, 15)
    attack(attacker, defender)

    assert attacker['rage'] == 0
    assert defender['health'] == 70


def test_attack_highlow():
    attacker = new_gladiator(100, 0, 15, 30)
    defender = new_gladiator(100, 0, 15, 15)
    attack(attacker, defender)

    assert attacker['rage'] == 15
    assert defender['health'] <= 85 and defender['health'] >= 70
