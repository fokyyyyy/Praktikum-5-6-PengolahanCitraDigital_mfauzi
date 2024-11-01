import numpy as np
import imageio as img  
import matplotlib.pyplot as plt

def zoomMinus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)
    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            # Mengambil piksel dari gambar asli yang sesuai dengan posisi (y, x) yang di-zoom out
            ori_y = int(y / factor)
            ori_x = int(x / factor)

            # Memastikan indeks berada dalam batas ukuran gambar asli
            ori_y = min(ori_y, height - 1)
            ori_x = min(ori_x, width - 1)

            imgZoom[y, x] = image[ori_y, ori_x]

    return imgZoom

# Membaca gambar
image = img.imread('c:\\Users\\Lenovo\\Downloads\\threesixty.jpeg')

# Faktor skala untuk mengecilkan gambar (contohnya 0.5 untuk setengah ukuran asli)
skala = 0.5
imgZoom = zoomMinus(image, skala)

# Menyimpan dan menampilkan hasil
img.imwrite("c:\\Users\\Lenovo\\Downloads\\threesixty_zoom_minus.jpeg", imgZoom)
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(imgZoom)
plt.title("Zoom Minus Image")

plt.show()
