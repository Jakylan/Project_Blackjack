from random import randint


def new_gladiator(health, rage, damage_low, damage_high, mana):
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

def magic(attacker, defender):
    spells = ['[A]ard', '[I]gni']
    print(spells)
    spell = input('What spell shall you cast?')
    if spell == 'A':
        if attacker ['mana'] >= 5
        defender['health'] -= 10
        defender['mana'] -= 5
    elif spell == 'I':
        if attacker ['mana'] >= 15
        defender['health'] -= 20
        defender['mana'] -= 15


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
