# mengubah dari 1D menjadi matrik 2D
import numpy as np

a = np.arange(1,21,1)
print(a)

c = a.reshape((4,5))
print(c)

# Membuat array 1D
b = np.arange(1, 13)  # 1D array dengan 12 elemen
print("Array 1D:")
print(b)

# Mengubah menjadi matriks 2D (3 baris, 4 kolom)
d = b.reshape((3, 4))
print("\nMatriks 2D:")
print(d)
