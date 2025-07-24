import numpy as np
n = 7
n_col = int(1.5 * (n-1) + 1)

range_x = np.linspace(-2, 1, n)
range_y = np.linspace(-1, 1, n_col)

def mandelbrot(c, iterations=10):
    z = 0 + 0j  # Initialisation de z_0 à 0
    for _ in range(iterations):
        z = z**2 + c
        if abs(z) > 1:
            return False
    return True


tab = np.zeros((len(range_x), len(range_y)), dtype=object)
for i in range(len(range_x)):
    for k in range(len(range_y)):
        if mandelbrot(range_x[i] + range_y[k]*1j):
            tab[i][k] = "*"
        else:
            tab[i][k] = " "
     
print(tab)
for i in range(n):
    print(''.join(tab[i]))
    