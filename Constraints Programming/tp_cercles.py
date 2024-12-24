# Bibliothèques
import numpy as np
import matplotlib.pyplot as plt

# Variables du problème
x_min, x_max = 1, 3.5
y_min, y_max = 1, 2
resolution = 1000
tolerance = 1e-3  # Tolérance pour considérer qu'un point est "sur" le cercle

# Création du maillage
x = np.linspace(x_min, x_max, resolution)
y = np.linspace(y_min, y_max, resolution)
X, Y = np.meshgrid(x, y)

# Fonctions
def get_circle_perimeter_points(a, b, r, X, Y, tol):
    """Retourne les points (x, y) situés sur le périmètre du cercle de centre (a, b) et rayon r."""
    distance = np.sqrt((X - a)**2 + (Y - b)**2)
    return np.abs(distance - r) <= tol

# Cercle 1
mask_cercle_1 = get_circle_perimeter_points(2, 2, 1.5, X, Y, tolerance)
x_cercle_1, y_cercle_1 = X[mask_cercle_1], Y[mask_cercle_1]

# Cercle 2
mask_cercle_2 = get_circle_perimeter_points(3, 3, 2, X, Y, tolerance)
x_cercle_2, y_cercle_2 = X[mask_cercle_2], Y[mask_cercle_2]

# Cercle 3
mask_cercle_3 = get_circle_perimeter_points(3.5, 0.8, 1, X, Y, tolerance)
x_cercle_3, y_cercle_3 = X[mask_cercle_3], Y[mask_cercle_3]

# Tracé des cercles
plt.figure(figsize=(8, 6))
plt.plot(x_cercle_1, y_cercle_1, '.', label="Cercle 1")
plt.plot(x_cercle_2, y_cercle_2, '.', label="Cercle 2")
plt.plot(x_cercle_3, y_cercle_3, '.', label="Cercle 3")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis("equal")
plt.show()
