import random
from time import sleep  # we will be using sleep to slow down the game for more realistic experience


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J', 'A'] * 4  # 4 suits of 13 cards each


def printer(person, cards):
    print(f"{person}: ", end="")
    for card in cards:
        print(card, end=" ")
    print()


def sum_of_cards(cards):
    total = 0
    for card in cards:
        if card in ['K', 'Q', 'J']:
            total += 10
        elif card == 'A':   # an Ace can be 1 or 11 based on our choice
            if total + 11 <= 21:
                total += 11
            else:
                total += 1
        else:
            total += card
    return total


def main():
    blackjack_art = """
      ____  _            _    _            _    
     |  _ \\| |          | |  (_)          | |   
     | |_) | | __ _  ___| | ___  __ _  ___| | __
     |  _ <| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
     | |_) | | (_| | (__|   <| | (_| | (__|   < 
     |____/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
                           _/ |                
                          |__/                 
    """
    print(blackjack_art)    # ascii art

    # choices function is used to select random cards from the deck with repetition
    player = random.sample(deck, k=2)
    dealer = random.sample(deck, k=2)

    # we will no longer have the dealt cards in the deck
    for i in range(2):
        deck.remove(player[i])
        deck.remove(dealer[i])

    print("Dealing Cards...")
    sleep(1)
    printer("Player", player)
    print("Dealer: X", dealer[1])

    while True:
        action = input("Do you want to hit (h) or stand (s)? ").lower()
        if action == "h":
            print("Dealing Card...")
            sleep(1)
            new_card = random.choice(deck)  # we will deal a new card if player chooses to hit
            player.append(new_card)
            deck.remove(new_card)
            printer("Player", player)

            sleep(1)
            if sum_of_cards(player) > 21:
                # \033[1m is used to make the text bold and \033[0m is used to reset the text style
                print("\033[1mPlayer busted! Dealer wins! 😓\033[0m")
                break

        elif action == "s":
            print("Revealing Dealer's Cards...")
            sleep(1)
            printer("Dealer", dealer)
            sleep(1)

            while sum_of_cards(dealer) < 17:
                print("Dealing Card to dealer...")
                sleep(1)
                new_card = random.choice(deck)
                dealer.append(new_card)
                deck.remove(new_card)
                printer("Dealer", dealer)

                sleep(1)
                if sum_of_cards(dealer) > 21:
                    print("\033[1mDealer busted! Player wins! 💸\033[0m")
                    break

            if sum_of_cards(dealer) > 21:
                break

            print("Checking results...")
            sleep(1)

            if sum_of_cards(player) > sum_of_cards(dealer):
                print("\033[1mPlayer wins! 💸\033[0m")
            elif sum_of_cards(player) < sum_of_cards(dealer):
                print("\033[1mDealer wins! 😓\033[0m")
            else:
                print("\033[1mIt's a tie! 🤝\033[0m")

            break

        else:
            print("Enter either h for hit or s for stand !")


if __name__ == "__main__":
    main()
