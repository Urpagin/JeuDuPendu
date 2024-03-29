import pygame
from affichage import dessin, ecriture
import os
from menu_campagne import campagne
from pve import pve
from utils.button import Button
from qt_guis.new_game_settings import widget

pygame.init()

# ecriture:
pygame.font.init()
police_chr = pygame.font.Font('../resources/LilitaOne-Regular.ttf', 30)

# fenêtre:
largeur, hauteur = 1925, 1025
# convert() optimise les performances du programme
arriere_plan = pygame.transform.scale(pygame.image.load('../img/pendu_menu.png').convert(), (largeur, hauteur))
fenetre = pygame.display.set_mode((largeur, hauteur))

# Choix:w
choix_ecr = ['Joueur VS Ordinateur', 'Joueur VS Joueur', 'Campagne', 'Quitter']
ecart_bord_haut = hauteur - (hauteur * 7 / 41)
ecart_ecriture = hauteur * 8 / 41


def a():
    pass


def menu():
    clock = pygame.time.Clock()
    jeu = True
    coordonne_x_ecrtiture = []
    coordonne_y_ecrtiture = []

    # affichage:

    # 1: Arrière plan:
    dessin(fenetre, arriere_plan)

    # 2: Affichage + recupération des coordonnées des ecritures:
    for i in range(0, 4):
        choix = police_chr.render(choix_ecr[i], True, 'black')
        ecriture(fenetre, choix, (largeur / 2) - (choix.get_width() / 2), (hauteur - ecart_bord_haut) + (ecart_ecriture * i))

        coordonne_x_ecrtiture.append(largeur / 2 - choix.get_width() / 2 + choix.get_width())
        coordonne_x_ecrtiture.append(largeur / 2 - choix.get_width() / 2 - choix.get_width())

        coordonne_y_ecrtiture.append(hauteur - ecart_bord_haut + ecart_ecriture * i + choix.get_height())
        coordonne_y_ecrtiture.append(hauteur - ecart_bord_haut + ecart_ecriture * i - choix.get_height())

    pygame.display.update()  # rafraichi la fenêtre
    clock.tick(60)  # FPS max

    while jeu:
        pygame.display.update()  # rafraichi la fenêtre

        for evenement in pygame.event.get():

            if evenement.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if evenement.type == pygame.MOUSEBUTTONDOWN:
                # evenement.button est le tipe de clique. (1: clique gauche, 2: clique molette 3: clique droit, etc)
                if evenement.button == 1:

                    print(f'{evenement.pos=}')
                    #if sur_bouton()
                    if evenement.pos[0] <= coordonne_x_ecrtiture[0] and evenement.pos[0] >= coordonne_x_ecrtiture[1] and \
                            evenement.pos[1] <= coordonne_y_ecrtiture[0] and evenement.pos[1] >= coordonne_y_ecrtiture[
                        1]:
                        # Player vs Computer
                        # TODO: async or multithread
                        pve((largeur, hauteur), fenetre)


                    elif coordonne_x_ecrtiture[2] >= evenement.pos[0] >= coordonne_x_ecrtiture[
                        3] and evenement.pos[1] <= coordonne_y_ecrtiture[2] and evenement.pos[1] >= \
                            coordonne_y_ecrtiture[3]:
                        # Player vs Player
                        pass

                    elif evenement.pos[0] <= coordonne_x_ecrtiture[4] and evenement.pos[0] >= coordonne_x_ecrtiture[
                        5] and evenement.pos[1] <= coordonne_y_ecrtiture[4] and evenement.pos[1] >= \
                            coordonne_y_ecrtiture[5]:
                        campagne(clock)


                    elif evenement.pos[0] <= coordonne_x_ecrtiture[6] and evenement.pos[0] >= coordonne_x_ecrtiture[
                        7] and evenement.pos[1] <= coordonne_y_ecrtiture[6] and evenement.pos[1] >= \
                            coordonne_y_ecrtiture[7]:
                        jeu = False


menu()
