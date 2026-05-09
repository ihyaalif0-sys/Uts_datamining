import pandas as pd
import numpy as np

# 1. Membuat DataFrame dengan data yang lebih kompleks (ada nilai NaN/Kosong)
data = {
    'Student': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'Age': [21, 19, 22, 20, np.nan], # Ada data hilang
    'Mark': [85, 90, 78, 92, 88],
    
    'Class': ['A', 'B', 'A', 'B', 'A']
}
df = pd.DataFrame(data)

# 2. Data Cleaning: Mengisi nilai Age yang kosong dengan rata-rata
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 3. Feature Engineering: Menambah kolom status berdasarkan nilai
df['Status'] = np.where(df['Mark'] >= 80, 'High', 'Standard')

# 4. Aggregation: Menghitung rata-rata nilai per kelas (Penting untuk pola data)
class_summary = df.groupby('Class')['Mark'].mean()

print("--- DataFrame Setelah Cleaning ---")
print(df)
print("\n--- Rata-rata Nilai per Kelas ---")
print(class_summary)

# 5. Statistik Deskriptif: Ringkasan cepat seluruh data numerik
print("\n--- Ringkasan Statistik ---")
print(df.describe())