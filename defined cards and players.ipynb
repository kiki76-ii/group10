#Reahs code - made a window, defined cards and players in a class and shuffled the cards to deal the players starting hands

import pygame
import random

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jubilee")

# Define the card colours using RGB values
CARD_COLOURS = {
    "red": (255, 0, 0),
    "green": (0, 150, 0),
    "yellow": (220, 180, 0),
    "black": (0, 0, 0),
    "blue": (0, 0, 255)
}

# Define the Card class
class Card:
    def __init__(self, colour, number):
        self.colour = colour
        self.number = number

    # Draw a card on the Pygame window
    def draw(self, screen, x, y):
        card_width = 60
        card_height = 90

        # Create the card rectangle
        card_rect = pygame.Rect(x, y, card_width, card_height)

        # Draw the coloured card
        pygame.draw.rect(screen, CARD_COLOURS[self.colour], card_rect)

        # Draw a white outline around the card
        pygame.draw.rect(screen, (255, 255, 255), card_rect, 3)

        # Display the card number in white
        font = pygame.font.SysFont("Arial", 36, bold=True)
        text = font.render(str(self.number), True, (255, 255, 255))

        # Centre the number on the card
        text_rect = text.get_rect(center=card_rect.center)
        screen.blit(text, text_rect)

    # Draw the back of a card
    def draw_back(self, screen, x, y):
        card_width = 60
        card_height = 90
        card_rect = pygame.Rect(x, y, card_width, card_height)
    
        # Draw a blue card back
        pygame.draw.rect(screen, (30, 60, 150), card_rect)
    
        # Draw a white outline
        pygame.draw.rect(screen, (255, 255, 255), card_rect, 3)

# Create the deck of 90 cards
colours = ["red", "green", "yellow", "black", "blue"]
numbers = range(1, 10)
cards = []
for colour in colours:
    for number in numbers:
        for copy in range(2):
            card = Card(colour, number)
            cards.append(card)

# Shuffle the deck
random.shuffle(cards)

# Define the Players class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    # Draw a card from the deck
    def draw_card(self, deck):
        if len(self.hand) < 20 and len(deck) > 0:
            card = deck.pop()
            self.hand.append(card)

# Create three players
player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")

players = [player1, player2, player3]

# Deal seven cards to each player
for player in players:
    for i in range(7):
        player.draw_card(cards)

# Check how many cards each player has
for player in players:
    print(player.name, "has", len(player.hand), "cards")



# Main game loop
running = True

while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Fill the window with a green background
    screen.fill((30, 120, 70))

    # Create font for player names
    font = pygame.font.SysFont("Arial", 25, bold=True)

    # Display Player 1's hand at the top
    text = font.render(player1.name, True, (255, 255, 255))
    screen.blit(text, (50, 30))

    for i, card in enumerate(player1.hand):
        card.draw(screen, 50 + i * 75, 70)

    # Display Player 2's hand on the left
    text = font.render(player2.name, True, (255, 255, 255))
    screen.blit(text, (50, 250))

    for i, card in enumerate(player2.hand):
        card.draw(screen, 50 + i * 75, 290)

    # Display Player 3's hand at the bottom
    text = font.render(player3.name, True, (255, 255, 255))
    screen.blit(text, (50, 470))

    for i, card in enumerate(player3.hand):
        card.draw(screen, 50 + i * 75, 510)

    # Display the deck in the middle-right area
    deck_x = 800
    deck_y = 290

    if len(cards) > 0:
        cards[-1].draw_back(screen, deck_x, deck_y)

    # Display the number of cards remaining in the deck
    deck_text = font.render(
        "Deck: " + str(len(cards)),
        True,
        (255, 255, 255)
    )

    screen.blit(deck_text, (deck_x - 10, deck_y + 110))

    # Update the display
    pygame.display.flip()



pygame.quit()
