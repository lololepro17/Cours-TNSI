from turtle import *


pi = 3.14159


def disque(rayon: float) -> float:
    """Calcul de l'aire d'un disque en fonction de son rayon."""
    return pi * rayon * rayon


def rectangle(largeur: float, longueur: float) -> float:
    """Calcul de l'aire d'un rectangle en fonction de sa largeur et longueur."""
    return largeur * longueur


def triangle(base: float, hauteur: float) -> float:
    """Calcul de l'aire d'un triangle en fonction de sa base et hauteur."""
    return base * hauteur / 2


couleurs = ["blue", "green", "yellow", "orange", "red", "purple"]
bgcolor("black")


def dessin():
    for i in range(180):
        color(couleurs[i % 6])
        forward(i)
        right(59)


listen()
onkey(dessin, "a")
mainloop()
