# War-card-game
I created this Simpler version of the card game called war using Python as a final assignment with what I had learned from python.
## The rules are as follows:
1. Use a standard deck of 52 playing cards.

2. Shuffle the deck and deal five cards to each player. Each player receives their own deck of five cards, and the      remaining cards are not used.

3. In each of the 10 rounds, both players simultaneously reveal the top card of their own decks. The player with the higher-ranking card wins the round. In case of a tie, a war occurs.

4. Card Ranks:
    Cards are ranked from highest to lowest: Ace, King, Queen, Jack, 10, 9, 8, 7, 6, 5, 4, 3, 2.
    Suits do not matter in this game.

5. Winning a Round:
    The player with the higher-ranked card wins the round.
    The winner of the round collects both their card and their opponent's card and places them at the bottom of their deck.

6. Ties (War):
    If there is a tie (both players play cards of the same rank), a war occurs. When a war occurs, each player places three cards face down (as a prize) and then reveals a fourth card.
    The player whose fourth card has the higher rank wins all the cards in the middle, including the cards from the initial tie.
    If another tie occurs, the process is repeated until there is a clear winner.

7. Scoring:
    Keep track of how many rounds each player wins out of the 10 rounds.
    The player with the bigger deck wins the game (wins the most rounds).

8. Printing Decks:
    At the end of the 10 rounds, the program prints out both players' decks to show the cards they collected.