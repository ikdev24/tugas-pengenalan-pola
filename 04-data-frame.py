import pandas as pd
import numpy as np

# Membuat DataFrame dari array NumPy
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  columns=['a', 'b', 'c'])

# Mencetak DataFrame
print(df)

print(df['a'])  # Mengakses kolom 'a'

print(df.iloc[0])  # Mengakses baris pertama

df['d'] = [10, 11, 12]  # Menambahkan kolom baru 'd'
print(df)

print(df.mean())  # Menghitung rata-rata setiap kolom
