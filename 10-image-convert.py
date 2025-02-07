import cv2
import matplotlib.pyplot as plt

# Membaca gambar menggunakan OpenCV
babon = cv2.imread("baboon.jpg")

# Mengonversi gambar ke grayscale
babon_gray = cv2.cvtColor(babon, cv2.COLOR_BGR2GRAY)

# Membuat subplot untuk menampilkan kedua gambar
plt.figure(figsize=(10, 5))

# Menampilkan gambar berwarna
plt.subplot(1, 2, 1)  # 1 baris, 2 kolom, gambar pertama
plt.imshow(cv2.cvtColor(babon, cv2.COLOR_BGR2RGB))  # Mengonversi BGR ke RGB
plt.axis('off')  # Menyembunyikan sumbu
plt.title('Gambar Berwarna')

# Menampilkan gambar grayscale
plt.subplot(1, 2, 2)  # 1 baris, 2 kolom, gambar kedua
plt.imshow(babon_gray, cmap='gray')  # Menampilkan gambar grayscale
plt.axis('off')  # Menyembunyikan sumbu
plt.title('Gambar Grayscale')

# Menampilkan semua subplot
plt.tight_layout()
plt.show()
