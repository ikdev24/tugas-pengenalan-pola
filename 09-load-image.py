import matplotlib.pyplot as plt
import cv2
import numpy as np

print("read images using opencv")
five = cv2.imread("5.png")
print(five.shape)
print(five.size)

# Mengubah format warna dari BGR ke RGB
five_rgb = cv2.cvtColor(five, cv2.COLOR_BGR2RGB)

# Menampilkan gambar menggunakan Matplotlib
plt.imshow(five)
plt.axis('off')  # Menyembunyikan sumbu
plt.show()

# Membaca gambar menggunakan OpenCV
ipb = cv2.imread("ipb.png")

# Mengubah format warna dari BGR ke RGB
ipb_rgb = cv2.cvtColor(ipb, cv2.COLOR_BGR2RGB)

# Menampilkan gambar menggunakan Matplotlib
plt.imshow(ipb_rgb)
plt.axis('off')  # Menyembunyikan sumbu
plt.show()
