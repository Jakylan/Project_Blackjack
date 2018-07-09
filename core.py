from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    gladiator = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }


def attack(attacker, defender):
    damage = randint(attacker['damage_low'], attacker['damage_high'])

    if attacker['rage'] > randint(1, 100):
        defender['health'] = defender['health'] - 2 * damage
        attacker['rage'] = 0
    else:
        defender['health'] = defender['health'] - damage
        attacker['rage'] = attacker['rage'] + 15


def heal(gladiator):

    return None


def is_dead(gladiator):
    return None
