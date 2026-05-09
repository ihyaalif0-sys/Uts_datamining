# 1. Array 1D & Filtering (Boolean Indexing)
# Mencari data tertentu tanpa menggunakan 'for loop'
marks = np.array([80, 90, 70, 60, 95])
top_marks = marks[marks >= 85]  # Filter instan: ambil yang >= 85
print(f"Nilai di atas 85: {top_marks}")

# 2. Agregasi Berdasarkan Axis (Penting untuk Data Tabular)
# Baris: Mahasiswa, Kolom: Nilai Ujian 1 & Ujian 2
data_ujian = np.array([
    [80, 85], 
    [90, 88], 
    [70, 75]
])

# axis=0 adalah kolom (rata-rata per mata kuliah)
# axis=1 adalah baris (rata-rata per mahasiswa)
mean_per_student = np.mean(data_ujian, axis=1)
print(f"Rata-rata per mahasiswa: {mean_per_student}")

# 3. Reshaping (Menyiapkan data untuk Machine Learning)
# Mengubah array 1D menjadi matriks kolom (sering diminta oleh Scikit-Learn)
reshaped_data = marks.reshape(-1, 1)
print(f"Bentuk data setelah reshape:\n{reshaped_data.shape}")