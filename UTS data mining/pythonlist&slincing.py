temperatures = [25, 28, 30, 22, 35, 40, 18, 24]

# Konversi Celsius ke Fahrenheit
temp_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures]

# Ambil 3 data terakhir
last_three = temp_fahrenheit[-3:]

print("Data Fahrenheit:", temp_fahrenheit)
print("3 Data Terakhir:", last_three)