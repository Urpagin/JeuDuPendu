import pygame
import pygame.freetype
from affichage import dessin
import tkinter

def pve(dimensions: tuple[int, int], fenetre: pygame.surface.Surface):
    """
    fonction qui ....
    :param fenetre: fenetre afin d'afficher
    :param dimensions: (largeur, hauteur) de la fenètre
    :return: ?
    """
    arriere_plan = pygame.transform.scale(pygame.image.load('../img/pendu_menu.png'), dimensions)
    dessin(fenetre, arriere_plan)
    pygame.display.update()  # rafraichi la fenêtre
    clock = pygame.time.Clock()

    settings_rect_dims: tuple[int, int] = int(dimensions[0] * 0.6), int(dimensions[1] * 0.6)
    # Calculer les dimensions du coin supérieur gauche
    settings_rect_xy: tuple[int, int] = (dimensions[0] - settings_rect_dims[0]) // 2, (dimensions[1] - settings_rect_dims[1]) // 2

    dessin(fenetre, arriere_plan)

    # Font setup
    pygame.freetype.init()
    font_size = 24
    font = pygame.freetype.SysFont('../resources/LilitaOne-Regular.ttf', font_size)

    # Colors
    white = (255, 255, 255)
    grey = (200, 200, 200)
    darker_grey = (150, 150, 150)
    black = (0, 0, 0)

    # Settings placeholder
    player_name = 'Joueur'
    difficulty_levels = ['Facile', 'Normal', 'Difficile']
    selected_difficulty = difficulty_levels[1]
    languages = ['Français', 'English']
    selected_language = languages[0]

    # Start game button
    button_color = grey
    button_hover_color = darker_grey
    button_rect = pygame.Rect(dimensions[0] / 2 - 100, dimensions[1] - 100, 200, 50)
    button_text = "Lancer"

    # Input field for player name
    input_active = False  # Initially, the input field is not active
    input_rect = pygame.Rect(100, 100, 140, 30)  # Position and size of the input field

    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(mouse_pos):
                    print('button clicked!')
                # Activate the input field when clicked
                if input_rect.collidepoint(mouse_pos):
                    input_active = True
                else:
                    input_active = False
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        fenetre.fill((0, 0,
                      0))  # Clear the entire screen (use the appropriate background color or draw the background image again)
        dessin(fenetre, arriere_plan)  # Redraw the background if necessary

        # Clear the input field area by filling it with the background color before drawing the text
        pygame.draw.rect(fenetre, white, input_rect)  # Fill the input field with a solid color
        pygame.draw.rect(fenetre, black, input_rect, 2)  # Draw the border of the input field

        input_text_surface = font.render(f'Pseudonyme: {player_name}', fgcolor=black, size=font_size)[0]
        fenetre.blit(input_text_surface, (input_rect.x + 5, input_rect.y + 5))

        # Draw the settings rectangle
        pygame.draw.rect(fenetre, white, (settings_rect_xy + settings_rect_dims))

        # Draw the start game button
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(fenetre, button_hover_color, button_rect)  # Button hover effect
        else:
            pygame.draw.rect(fenetre, button_color, button_rect)
        button_text_surface = font.render(button_text, fgcolor=black, size=font_size)[0]
        fenetre.blit(button_text_surface, (button_rect.x + (button_rect.width - button_text_surface.get_width()) / 2,
                                           button_rect.y + (button_rect.height - button_text_surface.get_height()) / 2))

        pygame.display.flip()
        clock.tick(60)

