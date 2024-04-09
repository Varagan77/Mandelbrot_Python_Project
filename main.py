import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(width, height, xmin, xmax, ymin, ymax, max_iter):
    mandelbrot_image = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            real = xmin + (xmax - xmin) * x / (width - 1)
            imaginary = ymin + (ymax - ymin) * y / (height - 1)
            c = complex(real, imaginary)
            mandelbrot_image[y, x] = mandelbrot(c, max_iter)
    return mandelbrot_image

def plot_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    mandelbrot_image = mandelbrot_set(width, height, xmin, xmax, ymin, ymax, max_iter)
    plt.imshow(mandelbrot_image, cmap='hot', extent=(xmin, xmax, ymin, ymax))
    plt.title('Mandelbrot Set')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()

# Define parameters here
width = 1000
height = 1000
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
max_iter = 500 

plot_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter)
