import pygame 
from affichage import (dessin, ecriture)
import os
from menu_campagne import campagne

#ecriture:
pygame.font.init()
police_chr = pygame.font.SysFont("comicsans", 30)

#fenêtre:
largeur, hauteur = 1925, 1025
arriere_plan = pygame.transform.scale(pygame.image.load('../img/pendu_menu.png'), (largeur, hauteur))
fenetre = pygame.display.set_mode((largeur, hauteur))

#Choix:
choix_ecr = ['joueur VS ordinateur', 'joueur VS joueur', 'campagne', 'quiter']
ecart_bord_haut= hauteur - (hauteur * 7/41)
ecart_ecriture = hauteur * 8/41

def menu():

    clock = pygame.time.Clock()
    jeu = True
    coordonne_x_ecrtiture = []
    coordonne_y_ecrtiture = []

    #affichage:

    #1: Arrière plan:
    dessin(fenetre, arriere_plan)

    #2: Affichage + recupération des coordonnées des ecritures:
    for i in range(0, 4):
        
        choix = police_chr.render(choix_ecr[i], 10, 'black')
        ecriture(fenetre, choix, largeur/2 - choix.get_width() / 2, hauteur - ecart_bord_haut + ecart_ecriture*i)

        coordonne_x_ecrtiture.append(largeur/2 - choix.get_width() / 2 + choix.get_width())
        coordonne_x_ecrtiture.append(largeur/2 - choix.get_width() / 2 - choix.get_width())

        coordonne_y_ecrtiture.append(hauteur - ecart_bord_haut + ecart_ecriture*(i) + choix.get_height())
        coordonne_y_ecrtiture.append(hauteur - ecart_bord_haut + ecart_ecriture*(i) - choix.get_height())

    pygame.display.update()#rafraichi la fenêtre
        


    while jeu:

        clock.tick(60) #FPS max
        pygame.display.update()#rafraichi la fenêtre

        for evenement in pygame.event.get():

            if evenement.type == pygame.QUIT:
                jeu = False

            elif evenement.type == pygame.MOUSEBUTTONDOWN:

                if evenement.button == 1:
                    
                    if evenement.pos[0] <= coordonne_x_ecrtiture[0] and evenement.pos[0] >= coordonne_x_ecrtiture[1] and evenement.pos[1] <= coordonne_y_ecrtiture[0] and evenement.pos[1] >= coordonne_y_ecrtiture[1]:
                        #votre fonction J vs J
                        pass


                    elif evenement.pos[0] <= coordonne_x_ecrtiture[2] and evenement.pos[0] >= coordonne_x_ecrtiture[3] and evenement.pos[1] <= coordonne_y_ecrtiture[2] and evenement.pos[1] >= coordonne_y_ecrtiture[3]:
                        #votre fonction J vs O
                        pass


                    elif evenement.pos[0] <= coordonne_x_ecrtiture[4] and evenement.pos[0] >= coordonne_x_ecrtiture[5] and evenement.pos[1] <= coordonne_y_ecrtiture[4] and evenement.pos[1] >= coordonne_y_ecrtiture[5]:
                        jeu = campagne()


                    elif evenement.pos[0] <= coordonne_x_ecrtiture[6] and evenement.pos[0] >= coordonne_x_ecrtiture[7] and evenement.pos[1] <= coordonne_y_ecrtiture[6] and evenement.pos[1] >= coordonne_y_ecrtiture[7]:
                        jeu = False

menu()