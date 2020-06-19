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
def nucleotide_bg(base) :
    gd = 1
    bg.color(couleur_chaine)
    bg.pensize(largeur_chaine)
    bg.forward(longueur_nuc * 1.5)
    bg.right(90 * gd)
    bg.pensize(largeur_nuc)
    if base == "A":
        bg.pencolor("red")
        bg.forward(ecart_brin)
        bg.right(45 * gd)
        bg.forward(long_hyp2 / 2)
        bg.right(90 * gd)
        bg.forward(long_hyp2 / 2)
        bg.right(45 * gd)
        bg.forward(ecart_brin)
    if base == "T":
        bg.color("green")
        bg.forward(ecart_brin * 1.5)
        bg.right(135 * gd)
        bg.forward(long_hyp2 / 2)
        bg.right(-90 * gd)
        bg.forward(long_hyp2 / 2)
        bg.right(135 * gd)
        bg.forward(ecart_brin * 1.5)
    if base == "C":
        bg.color("blue")
        bg.forward(ecart_brin * 1.25)
        bg.right(180)
        bg.circle(gd * longueur_nuc / 2, 180)
        bg.right(180)
        bg.forward(ecart_brin * 1.25)
    if base == "G":
        bg.color("yellow")
        bg.forward(ecart_brin * 1.25)
        bg.right(180 * gd)
        bg.circle(gd * longueur_nuc / 2, -180)
        bg.right(180 * gd)
        bg.forward(ecart_brin * 1.25)
    bg.right(90 * gd)
    bg.color(couleur_chaine)
    bg.pensize(largeur_chaine)
    bg.forward(longueur_nuc * 1.5)

def nucleotide_bd(base) :
    gd = -1
    bd.color(couleur_chaine)
    bd.pensize(largeur_chaine)
    bd.forward(longueur_nuc * 1.5)
    bd.right(90 * gd)
    bd.pensize(largeur_nuc)
    if base == "A":
        bd.pencolor("red")
        bd.forward(ecart_brin)
        bd.right(45 * gd)
        bd.forward(long_hyp2 / 2)
        bd.right(90 * gd)
        bd.forward(long_hyp2 / 2)
        bd.right(45 * gd)
        bd.forward(ecart_brin)
    if base == "T":
        bd.color("green")
        bd.forward(ecart_brin * 1.5)
        bd.right(135 * gd)
        bd.forward(long_hyp2 / 2)
        bd.right(-90 * gd)
        bd.forward(long_hyp2 / 2)
        bd.right(135 * gd)
        bd.forward(ecart_brin * 1.5)
    if base == "C":
        bd.color("blue")
        bd.forward(ecart_brin * 1.25)
        bd.right(180)
        bd.circle(gd * longueur_nuc / 2, 180)
        bd.right(180)
        bd.forward(ecart_brin * 1.25)
    if base == "G":
        bd.color("yellow")
        bd.forward(ecart_brin * 1.25)
        bd.right(180 * gd)
        bd.circle(gd * longueur_nuc / 2, -180)
        bd.right(180 * gd)
        bd.forward(ecart_brin * 1.25)
    bd.right(90 * gd)
    bd.color(couleur_chaine)
    bd.pensize(largeur_chaine)
    bd.forward(longueur_nuc * 1.5)


#Ecriture de la séquence des deux brins à partir de la lecture de la sequence
for i in range(longueur_brin):
    nucleotide_bg(sequence[i])
    if sequence[i] == "A":
        complement = "T"
        nucleotide_bd(complement)
    if sequence[i] == "T":
        complement = "A"
        nucleotide_bd(complement)
    if sequence[i] == "C":
        complement = "G"
        nucleotide_bd(complement)
    if sequence[i] == "G":
        complement = "C"
        nucleotide_bd(complement)


#permet de ne pas faire l'application à la fin du programme
turtle.mainloop()