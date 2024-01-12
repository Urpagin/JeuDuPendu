import pygame


def dessin(fenetre, img, x=0, y=0):
    fenetre.blit(img, (x, y))


def ecriture(fenetre, txt, x=0, y=0):
    fenetre.blit(txt, (x, y))
