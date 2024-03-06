import pygame
from affichage import (dessin)

# fenêtre:
largeur, hauteur = 1925, 1025
# arriere_plan = pygame.transform.scale(pygame.image.load(os.path.join("jeu_du_pendu", "img", "no_image.png")), (largeur, hauteur))
arriere_plan = pygame.transform.scale(pygame.image.load('../img/pendu_menu.png'), (largeur, hauteur))
fenetre = pygame.display.set_mode((largeur, hauteur))
print(type(fenetre))


def campagne(clock: pygame.time.Clock):
    # affichage:
    dessin(fenetre, arriere_plan)

    while True:

        pygame.display.update()  # rafraichi la fenêtre

        for evenement in pygame.event.get():

            if evenement.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        clock.tick(60)  # FPS max
