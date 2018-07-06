from random import shuffle


def war():
    cards = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12,
        13, 13, 13, 13, 14, 14, 14, 14
    ]
    shuffle(cards)
    top = cards[:26]
    bottom = cards[26:]
    cards_on_table = []
    top_won = []
    bottom_won = []
    while len(top) > 0 and len(bottom) > 0:
        input('Draw!')
        card1 = top.pop()
        card2 = bottom.pop()
        cards_on_table.extend([card1, card2])
        print('you: {}, Computer: {}'.format(card1, card2))
        print('({} cards left)'.format(len(top) + len(top_won)))
        if card1 > card2:
            top_won.extend(cards_on_table[:])
            cards_on_table.clear()
        elif card1 < card2:
            bottom_won.extend(cards_on_table[:])
            cards_on_table.clear()

        else:
            phrase = ['\nI.', 'Declare.', 'WAR!']
            for i in range(3):
                print(phrase[i],
                      '({} cards left)'.format(len(top) + len(top_won)))
                if len(top) == 0:
                    top = top_won[:]
                    top_won = []
                    shuffle(top)
                    print('you shuffled')
                if len(bottom) == 0:
                    bottom = bottom_won[:]
                    bottom_won = []
                    shuffle(bottom)
                if len(top) == 0 or len(bottom) == 0:
                    break

                tie_card_1 = top.pop()
                cards_on_table.append(tie_card_1)
                tie_card_2 = bottom.pop()
                cards_on_table.append(tie_card_2)

        if len(top) == 0:
            top = top_won[:]
            top_won = []
            shuffle(top)
            print('you shuffled')
        if len(bottom) == 0:
            bottom = bottom_won[:]
            bottom_won = []
            shuffle(bottom)

    print(['YOU', 'Computer'][len(top) < len(bottom)], 'WIN!!!')


def main():
    war()


if __name__ == '__main__':
    main()
