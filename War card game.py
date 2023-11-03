import random

def main():
    '''
    This function creates a full deck of cards, shuffles the deck and returns it.
    Pre-Condition: random module is imported
    Post-Condition: shuffled deck of cards (as strings with unicode suit symbols) is returned
    '''
    DECK = 52
    SUITS = ["\u2663","\u2664", "\u2665", "\u2666"] # the suits (clubs, spades, hearts, diamonds)
    card_list = []
    card = '' #empty string
    suit_num = 0 #index variable that will be used for the suits list
    for i in range(len(SUITS)): #For loop to loop through each suit
        for card in range(int(DECK/len(SUITS))): #Go through each card value in current suit
            card = card + 2
            if card < 10:
                card1 = str(card) + ' ' + SUITS[suit_num] #Prints the card values
            elif card == 10:
                card1 = "T" + ' ' + SUITS[suit_num]
            elif card == 11:
                card1 = "J" + ' ' + SUITS[suit_num]
            elif card == 12:
                card1 = "Q" + ' ' + SUITS[suit_num]
            elif card == 13:
                card1 = "K" + ' ' + SUITS[suit_num]
            elif card == 14:
                card1 = "A" + ' ' + SUITS[suit_num]
            card_list.append(card1)
        suit_num = suit_num + 1 #Increments the index variable by 1
    random.shuffle(card_list) #shuffles the list
    pretty_print(card_list) #sends the list to be printed nicely
    p1_list = card_list[:26] #creates the deck for player 1
    p2_list = card_list[26:] #creates the deck for player 2
    play(p1_list,p2_list) #sends both lists to the play function

def pretty_print(list1: list):
    i = 0
    for _ in range(len(list1)//4):
        for _ in range(4):
            print(list1[i], "\t", end="")
            i += 1
        print("\n")
    for _ in range(len(list1)%4):
        print(list1[i], "\t", end="")
        i += 1
    print("\n")
    
        
def compare_cards(num1: list,num2: list) -> str:
    '''
    This function compares two passed in card strings and returns 0, 1, or 2
         0 means card1 >︎ card2, 1 means card1 == card2, 2 means card1 < card2
    Pre-Condition: card strings contain value (2-9, or T,J,Q,K,A) in first char
        The first card is from Player 1, the second card is from Player 2
    Post-Condition: Cards are printed out to console (with 1 level indent).
        0, 1, or 2 is returned.
    '''	
    CARD_ORDER = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    int1 = num1.split(" ")
    int2 = num2.split(" ")
    index1 = int1[0]
    index2 = int2[0]
    number1 = CARD_ORDER.index(index1)
    number2 = CARD_ORDER.index(index2)
    if number1 > number2:
        result = "player 1 won!"
    if number1 < number2:
        result = "player 2 won!"
    if number1 == number2:
        result = "It is a tie!"
    return result #returns the result

def play(p1_list: list,p2_list: list):
    '''
    This function handles game play, with an indefinite loop for game rounds
    Pre-Condition: two decks are passed in containing a set of cards as strings
        with the first char in each card having a value (2-9, or T,J,Q,K,A)
    Post-Condition: Results of each round are printed out to console.
        The decks are altered by play. A winner is declared.
    '''
    war_deck1 = []
    war_deck2 = []
    i = 0
    print("Decks have been delt")
    print("Player 1 deck")
    pretty_print(p1_list)
    print("Player 2 deck")
    pretty_print(p2_list)
    round_num = 0
    for _ in range(10):
        round_num += 1
        print("Round number", round_num)
        result = compare_cards(p1_list[0],p2_list[0])
        if result != "It is a tie!":
            print("\t","Player 1 plays:",p1_list[0])
            print("\t","Player 2 plays:",p2_list[0])
            if result == "player 1 won!":
                p1_list.append(p1_list[0])
                p1_list.append(p2_list[0])
                print("\t", "\t", result, "Player 1 now has ", len(p1_list), " cards")
            elif result == "player 2 won!":
                p2_list.append(p1_list[0])
                p2_list.append(p2_list[0])
                print("\t", "\t", result, "Player 2 now has ", len(p2_list), " cards")
            p1_list = p1_list[1:]
            p2_list = p2_list[1:]
            print("\n")
        else:
            print("\t","Player 1 plays:",p1_list[0])
            print("\t","Player 2 plays:",p2_list[0])
            print("****WAR!****")
            war_deck1 = p1_list[:5]
            war_deck2 = p2_list[:5]
            print("\t","Player 1 plays:",war_deck1[4])
            print("\t","Player 2 plays:",war_deck2[4])
            p1_list = p1_list[5:]
            p2_list = p2_list[5:]
            result = compare_cards(war_deck1[4],war_deck2[4])
            if result == "player 1 won!":
                p1_list += war_deck1
                p1_list += war_deck2
                print("\t", "\t", result, "Player 1 now has ", len(p1_list), " cards")
            elif result == "player 2 won!":
                p2_list += war_deck1
                p2_list += war_deck2
                print("\t", "\t", result, "Player 2 now has ", len(p2_list), " cards")
            else:
                print("\t", "\t", result, "No one wins")
                p1_list += war_deck1
                p2_list += war_deck2
            
    print("Player 1 deck", "(",len(p1_list),")", "cards")
    pretty_print(p1_list)
    print("Player 2 deck", "(",len(p2_list),")", "cards")
    pretty_print(p2_list)    
    
main()
