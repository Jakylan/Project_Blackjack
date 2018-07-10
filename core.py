from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    gladiator = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }
    return gladiator


def attack(attacker, defender):
    damage = randint(attacker['damage_low'], attacker['damage_high'])

    if attacker['rage'] > randint(1, 100):
        defender['health'] = defender['health'] - 2 * damage
        attacker['rage'] = 0
    else:
        defender['health'] = defender['health'] - damage
        attacker['rage'] = attacker['rage'] + 15


def heal(gladiator):
    if gladiator['rage'] >= 10:
        gladiator['rage'] = gladiator['rage'] - 10
        health = gladiator['health'] + 5
        gladiator['health'] = min(100, health)
    else:
        gladiator['rage'] = 0


def is_dead(gladiator):
    if gladiator['health'] <= 0:
        return True
    return False
