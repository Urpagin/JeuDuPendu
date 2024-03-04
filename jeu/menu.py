import pygame

import player_vs_computer
from affichage import dessin, ecriture
from menu_campagne import campagne

pygame.init()

# Set up font and window
pygame.font.init()
police_chr = pygame.font.Font('../resources/LilitaOne-Regular.ttf', 30)
largeur, hauteur = 1925, 1025
arriere_plan = pygame.transform.scale(pygame.image.load('../img/pendu_menu.png').convert(), (largeur, hauteur))
fenetre = pygame.display.set_mode((largeur, hauteur))

# Menu options
choix_ecr = ['Joueur VS Ordinateur', 'Joueur VS Joueur', 'Campagne', 'Quitter']
ecart_bord_haut = hauteur - (hauteur * 7 / 41)
ecart_ecriture = hauteur * 8 / 41

print("VEUILLEZ CACHER LA CONSOLE, LE MOT VA Y ÊTRE AFFICHER.")


def menu():
    clock = pygame.time.Clock()
    jeu = True

    # Create Rects for each menu item
    menu_rects = []
    for i, choix in enumerate(choix_ecr):
        text_surface = police_chr.render(choix, True, 'black')
        text_rect = text_surface.get_rect(center=(largeur / 2, (hauteur - ecart_bord_haut) + (ecart_ecriture * i)))
        menu_rects.append(text_rect)

    while jeu:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:  # Left click
                for i, rect in enumerate(menu_rects):
                    if rect.collidepoint(evenement.pos):
                        if i == 0:
                            # Player vs Computer
                            player_vs_computer.main((largeur, hauteur))
                        elif i == 1:
                            # Player vs Player
                            pass
                        elif i == 2:
                            # Campagne
                            campagne(clock)
                        elif i == 3:
                            # Quitter
                            jeu = False

        # Draw background and menu options
        dessin(fenetre, arriere_plan)
        for i, choix in enumerate(choix_ecr):
            ecriture(fenetre, police_chr.render(choix, True, 'black'), menu_rects[i].x, menu_rects[i].y)

        pygame.display.update()
        clock.tick(60)  # FPS max


menu()
