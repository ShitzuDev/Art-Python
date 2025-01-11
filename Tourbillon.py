import turtle

# Initialisation de la fenêtre Turtle
screen = turtle.Screen()
screen.bgcolor("black")

# Création de la tortue (le "pinceau" pour dessiner)
spiral = turtle.Turtle()
spiral.speed(0)  # Vitesse la plus rapide

# Liste des couleurs à utiliser pour la spirale
colors = ["red", "yellow", "green", "blue", "purple", "orange"]

# Fonction pour dessiner une spirale colorée
for i in range(360):
    spiral.pencolor(colors[i % 6])  # Change la couleur de la ligne à chaque itération
    spiral.width(i / 100 + 1)  # Augmente la taille du trait au fur et à mesure
    spiral.forward(i * 3 / 2 + i)  # Déplace la tortue en avant
    spiral.left(59)  # Fait tourner la tortue pour créer la spirale

# Terminer l'exécution
turtle.done()
