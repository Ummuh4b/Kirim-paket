# Inisialisasi variabel
nama_pengirim = "Melati"
nama_penerima = "Mawar"
alamat_pengirim = "Jl. Siliwangi No. 30"
alamat_penerima = "Jl. Diponegoro No. 06"
berat_barang = 2.5  # dalam kilogram
ongkos_kirim = 10000  # per kilogram

# Hitung total ongkos kirim
total_ongkos_kirim = ongkos_kirim * berat_barang

# Cetak detail pengiriman
print("===============================")
print("Detail Pengiriman Barang")
print("===============================")
print("Nama Pengirim: " + nama_pengirim)
print("Nama Penerima: " + nama_penerima)
print("Alamat Pengirim: " + alamat_pengirim)
print("Alamat Penerima: " + alamat_penerima)
print("Berat Barang: " + str(berat_barang) + " kg")
print("Ongkos Kirim: Rp. " + str(ongkos_kirim) + " per kg")
print("Total Ongkos Kirim: Rp. " + str(total_ongkos_kirim))
print("===============================")