import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

path = 'c:\\Users\\Lenovo\\Downloads\\threesixty.jpeg'
image = img.imread(path)

height, width = image.shape[:2]
both_mirrored = np.zeros_like(image)

# Melakukan mirroring vertikal dan horizontal secara bersamaan
for y in range(height):
    for x in range(width):
        both_mirrored[y, x] = image[height - 1 - y, width - 1 - x]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(both_mirrored)
plt.title("Both Mirrored Image")

plt.show()
