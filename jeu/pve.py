import pygame
from affichage import dessin


def pve(dimensions: tuple[int, int], fenetre: pygame.surface.Surface):
    """
    fonction qui ....
    :param fenetre: fenetre afin d'afficher
    :param dimensions: (largeur, hauteur) de la fenètre
    :return: ?
    """
    jeu = True
    arriere_plan = pygame.transform.scale(pygame.image.load('../img/no_image.png'), dimensions)
    dessin(fenetre, arriere_plan)
    pygame.display.update()  # rafraichi la fenêtre

    while jeu:
        for evenement in pygame.event.get():
            pass
