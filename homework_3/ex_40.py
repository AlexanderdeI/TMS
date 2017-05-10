cards = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
cards_deck = []

for card in cards:
	for suit in "♥♦♣♠":
		cards_deck.append(str(card) + suit)
		
print(cards_deck)
