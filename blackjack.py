from random import shuffle


def make_deck():
    deck = []
    for _suit in range(4):
        for i in range(2, 11):
            deck.append(i)
        for _facecard in range(3):
            deck.append(10)
        deck.append('Ace')
    shuffle(deck)
    return deck


def deal_cards(hand, deck):
    for i in range(2):
        card = deck.pop()
        hand.append(card)


def hand_value(hand):
    ''' List(cards) -> int

    >>> hand_value([4, 'Ace'])
    15
    '''
    hand_total = 0
    aces = 0
    for card in hand:
        if card == 'Ace':
            aces += 1
        else:
            hand_total = hand_total + card

    if aces == 0:
        return hand_total
    else:
        gap = 11 + (aces - 1)
        if hand_total + gap <= 21:
            return hand_total + gap
        else:
            return hand_total + aces
    # elif aces == 1:
    #     if hand_total <= 10:
    #         return hand_total + 11
    #     else:
    #         return hand_total + 1
    # elif aces == 2:
    #     if hand_total <= 9:
    #         return hand_total + 12
    #     else:
    #         return hand_total + 2
    # elif aces == 3:
    #     if hand_total <= 8:
    #         return hand_total + 13
    #     else:
    #         return hand_total +  3
    # elif aces == 4:
    #     if hand_total <= 7:
    #         return hand_total + 14
    #     else:
    #         return hand_total + 4


def player_choice(hand, deck):
    while True:
        print('Your Cards: {} ({})'.format(hand, hand_value(hand)))
        choice = input('Hit or Stay? ').upper()
        if choice == 'HIT':
            hand.append(deck.pop())
            total = hand_value(hand)
            if total > 21:
                print('Bust!')
                break
            elif total == 21:
                print('Blackjack!')
                break
            continue
        elif choice == 'STAY':
            print('Stayed at {} ({})'.format(hand, hand_value(hand)))
            break
        else:
            print('Invalid Choice')


def dealer_choice(hand, deck):
    while True:
        dealer_value = hand_value(hand)
        print('Dealer Cards: {} ({})'.format(hand, dealer_value))
        input()
        if dealer_value > 21:
            print('Bust!')
            break
        elif dealer_value == 21:
            print('Blackjack!')
            break
        if dealer_value < 17:
            hand.append(deck.pop())
            print('dealer draws!')
            continue
        else:
            print('Stayed at {} ({})'.format(hand, dealer_value))
            break


def show_cards(player_hand, dealer_hand):
    print('You have {}, total: {}'.format(player_hand,
                                          hand_value(player_hand)))
    print('Dealer has [{}, ?]'.format(dealer_hand[0]))


def show_end_cards(player_hand, dealer_hand):
    print('You have {}, total: {}'.format(player_hand,
                                          hand_value(player_hand)))
    print('Dealer has {}, total: {}'.format(dealer_hand,
                                            hand_value(dealer_hand)))


def winner(player, dealer):
    if hand_value(player) > 21:
        print('Bust')
        return

    if hand_value(dealer) > 21:
        print('Bust')
        return

    #check for higher value
    if hand_value(dealer) >= hand_value(player):
        print('Dealer Wins')
    elif hand_value(player) > hand_value(dealer):
        print('Player Wins')


def blackjack():
    deck = make_deck()
    player_hand = []
    dealer_hand = []
    deal_cards(player_hand, deck)
    deal_cards(dealer_hand, deck)
    show_cards(player_hand, dealer_hand)
    # player_value = hand_value(player_hand)
    player_choice(player_hand, deck)
    dealer_choice(dealer_hand, deck)
    show_end_cards(player_hand, dealer_hand)
    winner(player_hand, dealer_hand)


def main():
    blackjack()


if __name__ == '__main__':
    main()
