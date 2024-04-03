perangkat = {'lampu': 20, 'kulkas': 250, 'kipas': 120, 'televisi': 150, 'komputer': 300, 'dispenser': 200} # Daftar perangkat elektronik dan konsumsi listriknya (dalam watt)
jumlah_perangkat = int(input("Masukkan jumlah perangkat elektronik yang digunakan: "))
total_konsumsi = 0
for i in range(jumlah_perangkat):
    perangkat_input = input("Masukkan nama perangkat elektronik ke-" + str(i+1) + ": ")
    if perangkat_input in perangkat:
        total_konsumsi += perangkat[perangkat_input]
    else:
        print("Perangkat", perangkat_input, "tidak terdaftar.")
konsumsi_bulanan = total_konsumsi * 30 / 1000  # Mengonversi dari watt menjadi kWh
harga_per_kwh = 1.500
total_biaya = konsumsi_bulanan * harga_per_kwh
print("========TOTAL KONSUMSI LISTRIK DAN BIAYA PERBULAN========")
print("Estimasi konsumsi listrik bulanan:", konsumsi_bulanan, "kWh")
print("Total biaya bulanan:", "Rp.", total_biaya,)

