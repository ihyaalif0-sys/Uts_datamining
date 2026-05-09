inventory = {
    "laptop": {"stok": 10, "harga": 15000000},
    "mouse": {"stok": 50, "harga": 250000},
    "monitor": {"stok": 20, "harga": 3000000}
}

# Tambah produk baru
inventory["keyboard"] = {"stok": 30, "harga": 500000}

# Update harga laptop
inventory["laptop"].update({"harga": 14500000})

# Hitung total nilai aset
total_aset = sum(item["stok"] * item["harga"] for item in inventory.values())

print("Inventory Baru:")
print(inventory)

print("\nTotal Nilai Aset:", total_aset)