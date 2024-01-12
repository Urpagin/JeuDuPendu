import pygame
import pygame.font

# Initialize pygame
pygame.init()

# Create a font object
font = pygame.font.Font("../resources/LilitaOne-Regular.ttf", 16)

# Render some text
text = font.render("Hello, world!", True, (0, 0, 0))

# Display the text on the screen
screen = pygame.display.set_mode((640, 480))
screen.blit(text, (20, 20))
pygame.display.flip()
