import pandas as pd
f = pd.read_csv('http://www.exploredata.net/ftp/Spellman.csv')
print(f)

print(f.head())  # Menampilkan 5 baris pertama

print(f.info())

print(f.describe())

