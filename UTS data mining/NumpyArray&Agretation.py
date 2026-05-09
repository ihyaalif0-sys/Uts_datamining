import numpy as np

scores = np.array([
    [80, 85, 90],
    [70, 60, 75],
    [95, 90, 100],
    [40, 50, 45]
])

# Rata-rata setiap mahasiswa
average_scores = np.mean(scores, axis=1)

# Nilai tertinggi
highest_score = np.max(scores)

# Status kelulusan
status = np.where(average_scores >= 70, "Lulus", "Gagal")

print("Rata-rata Mahasiswa:", average_scores)
print("Nilai Tertinggi:", highest_score)
print("Status Kelulusan:", status)