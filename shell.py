import core


def gladiator():
    glad = core.new_gladiator
    gladiator_1 = glad(100, 0, 10, 25)
    gladiator_2 = glad(100, 0, 10, 25)
    while True:
        while True:
            print('\nGladiator 1 your turn!\n')
            print('Gladiator 1', gladiator_1['health'], 'HP', '|||',
                  'Gladiator 1', gladiator_1['rage'], 'rage')
            response = input(
                '\nGladiator 1 what would you like to attack, heal, pass, or quit?\n'
            ).strip().lower()

            if response == 'a' or response == 'attack':
                core.attack(gladiator_1, gladiator_2)
                break
            elif response == 'h' or response == 'heal':
                core.heal(gladiator_1)
                break
            elif response == 'p' or response == 'pass':
                break
            elif response == 'q' or response == 'quit':
                return
        if core.is_dead(gladiator_2):
            print('Gladiator 1 Wins!')
            break
        while True:
            print('\nGladiator 2 your turn!\n')
            print('Gladiator 2', gladiator_2['health'], 'HP', '|||',
                  'Gladiator 2', gladiator_2['rage'], 'rage')
            response = input(
                '\nGladiator 2 what would you like to attack, heal, pass, or quit?\n'
            ).strip().lower()
            print('--------------------------------------------------')
            if response == 'a' or response == 'attack':
                core.attack(gladiator_2, gladiator_1)
                break
            elif response == 'h' or response == 'heal':
                core.heal(gladiator_2)
                break
            elif response == 'p' or response == 'pass':
                break
            elif response == 'q' or response == 'quit':
                return
        if core.is_dead(gladiator_1):
            print('Gladiator 2 Wins!')
            break


def main():
    gladiator()


if __name__ == '__main__':
    main()
