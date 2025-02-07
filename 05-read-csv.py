import pandas as pd

# Membaca data dari file CSV
data = pd.read_csv("Data.csv", sep=";")

# Menampilkan data
print(data)

# Menampilkan 5 baris pertama
print(data.head())

# Menampilkan informasi tentang DataFrame
print(data.info())

# Menampilkan statistik deskriptif
print(data.describe())

