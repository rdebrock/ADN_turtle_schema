import turtle
import math

#déclaration des variables pour les deux brins d'ADN.
bg = turtle.Turtle()
bd = turtle.Turtle()

#Options
     #position de la molécule(brin gauche)
pos_x = -100
pos_y = -350
    #ecart entre les deux brins
ecart_brin = 40
    #apparence chaîne
couleur_chaine = "black"
largeur_chaine = 4
    #apparence_nucleotide
longueur_nuc = 40
largeur_nuc = 4;
long_hyp2 = 0
    #longueur_brin et sequence
longueur_brin = 0
sequence = 0
    #vitesse
vitesse_bg = 0
vitesse_bd = 0
    #taille
multi = 0


#Ouverture et lecture du fichier sequence.txt
with open("sequence.txt", "r+") as file:
    sequence = file.read()
    file.close()
longueur_brin = len(sequence)

#taille de la molécule en fonction de la longueur de la sequence
multi = 2 * (4/longueur_brin)
largeur_chaine = 4 * multi
largeur = 4 * multi
ecart_brin = ecart_brin * multi
longueur_nuc = longueur_nuc * multi
long_hyp2 = round(ecart_brin / math.sin(45))

#position et orientation de départ des deux brins
bg.penup()
bg.speed(vitesse_bg)
bg.setposition(pos_x, pos_y)
bg.left(90)
bg.pendown()
bd.speed(vitesse_bd)
bd.penup()
bd.setposition(pos_x + ecart_brin * 3, pos_y)
bd.pendown()
bd.left(90)

#fonction pour tracer les différents nucléotides
def nucleotide(base, orientation) :
    if orientation == bd:
        gd = -1
    else:
        gd = 1
    orientation.color(couleur_chaine)
    orientation.pensize(largeur_chaine)
    orientation.forward(longueur_nuc * 1.5)
    orientation.right(90 * gd)
    orientation.pensize(largeur_nuc)
    if base == "A":
        orientation.pencolor("red")
        orientation.forward(ecart_brin)
        orientation.right(45 * gd)
        orientation.forward(long_hyp2 / 2)
        orientation.right(90 * gd)
        orientation.forward(long_hyp2 / 2)
        orientation.right(45 * gd)
        orientation.forward(ecart_brin)
    if base == "T":
        orientation.color("green")
        orientation.forward(ecart_brin * 1.5)
        orientation.right(135 * gd)
        orientation.forward(long_hyp2 / 2)
        orientation.right(-90 * gd)
        orientation.forward(long_hyp2 / 2)
        orientation.right(135 * gd)
        orientation.forward(ecart_brin * 1.5)
    if base == "C":
        orientation.color("blue")
        orientation.forward(ecart_brin * 1.25)
        orientation.right(180)
        orientation.circle(gd * longueur_nuc / 2, 180)
        orientation.right(180)
        orientation.forward(ecart_brin * 1.25)
    if base == "G":
        orientation.color("yellow")
        orientation.forward(ecart_brin * 1.25)
        orientation.right(180 * gd)
        orientation.circle(gd * longueur_nuc / 2, -180)
        orientation.right(180 * gd)
        orientation.forward(ecart_brin * 1.25)
    orientation.right(90 * gd)
    orientation.color(couleur_chaine)
    orientation.pensize(largeur_chaine)
    orientation.forward(longueur_nuc * 1.5)

#Ecriture de la séquence des deux brins à partir de la lecture de la sequence
for i in range(longueur_brin):
    nucleotide(sequence[i], bg)
    if sequence[i] == "A":
        complement = "T"
        nucleotide(complement, bd)
    if sequence[i] == "T":
        complement = "A"
        nucleotide(complement, bd)
    if sequence[i] == "C":
        complement = "G"
        nucleotide(complement, bd)
    if sequence[i] == "G":
        complement = "C"
        nucleotide(complement, bd)




#permet de ne pas faire l'application à la fin du programme
turtle.mainloop()