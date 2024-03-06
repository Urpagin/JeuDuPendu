import pygame

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((800, 600))


# Define a function to handle button clicks
def button_click():
    print("Button clicked!")


# Create a button
button_rect = pygame.Rect(300, 250, 200, 50)
button_color = RED
button_hover_color = WHITE

# Create the button surface
button_surface = pygame.Surface((button_rect.width, button_rect.height))
button_surface.fill(button_color)

# Draw text onto the button surface
font = pygame.font.SysFont("Arial", 24)
text = font.render("Click Me!", True, BLACK)
text_rect = text.get_rect(center=button_rect.center)
button_surface.blit(text, text_rect)


# Create a function to check for button clicks
def check_button_click(pos):
    if button_rect.collidepoint(pos):
        button_surface.fill(button_hover_color)
        if pygame.mouse.get_pressed()[0]:
            button_click()
            button_surface.fill(button_color)
    else:
        button_surface.fill(button_color)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_button_click(event.pos)

    screen.fill(WHITE)
    screen.blit(button_surface, button_rect)

    pygame.display.flip()

pygame.quit()
