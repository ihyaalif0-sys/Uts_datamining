import pandas as pd
import numpy as np

df_data = {
    'Nama': ['Andi', 'Budi', 'Caca', 'Dedi', 'Euis'],
    'Departemen': ['IT', 'HR', 'IT', 'Sales', 'Sales'],
    'Gaji': [8000000, 7000000, 8500000, np.nan, 6000000],
    'Pengalaman_Tahun': [5, 3, 6, 2, 1]
}

df = pd.DataFrame(df_data)

# Isi NaN dengan median gaji
median_gaji = df['Gaji'].median()
df['Gaji'] = df['Gaji'].fillna(median_gaji)

# Tambah kolom kategori senioritas
df['Kategori_Senioritas'] = np.where(
    df['Pengalaman_Tahun'] > 4,
    'Senior',
    'Junior'
)

# Rata-rata gaji per departemen
rata_gaji_departemen = df.groupby('Departemen')['Gaji'].mean()

print("DataFrame Setelah Manipulasi:")
print(df)

print("\nRata-rata Gaji per Departemen:")
print(rata_gaji_departemen)