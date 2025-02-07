# vektor python numpy with range value
import numpy as np

# Membuat vektor dengan np.arange()
a = np.arange(1, 20, 1)  # Vektor dari 1 hingga 19
b = np.arange(1, 20, 2)  # Vektor dari 1 hingga 19 dengan langkah 2

# Membuat vektor dengan np.array()
c = np.array([1, 2, 3, 4, 5])        # Vektor integer
d = np.array([1.5, 2.5, 5, 6, 7])    # Vektor float

# Menampilkan vektor
print("Vektor a:", a)
print("Vektor b:", b)

# Menampilkan dimensi dan bentuk
print("Dimensi a:", a.ndim)
print("Bentuk a:", a.shape)

print("Dimensi b:", b.ndim)
print("Bentuk b:", b.shape)