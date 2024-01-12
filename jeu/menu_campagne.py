import pygame
from affichage import (dessin)

# fenêtre:
largeur, hauteur = 1925, 1025
# arriere_plan = pygame.transform.scale(pygame.image.load(os.path.join("jeu_du_pendu", "img", "Erreur 405, image notfound.png")), (largeur, hauteur))
arriere_plan = pygame.transform.scale(pygame.image.load('../img/pendu_menu.png'), (largeur, hauteur))
fenetre = pygame.display.set_mode((largeur, hauteur))


def campagne(clock: pygame.time.Clock):
    jeu = True
    # affichage:
    dessin(fenetre, arriere_plan)

    pygame.display.update()  # rafraichi la fenêtre

    while jeu:

        clock.tick(60)  # FPS max

        for evenement in pygame.event.get():

            if evenement.type == pygame.QUIT:
                pygame.quit()
