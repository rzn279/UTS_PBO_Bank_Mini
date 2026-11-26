from bank import Bank

bank = Bank()

# Fungsi untuk input angka dengan validasi
def input_angka(pesan):  
    try:
        return int(input(pesan))
    except ValueError:
        raise ValueError("Input harus berupa angka")

# Fungsi untuk mengambil rekening berdasarkan nomor rekening
def ambil_rekening(pesan="Input no rekening: "):
    rekening = bank.cari_rekening(input_angka(pesan))
    if rekening is None:
        print("Rekening tidak ditemukan")
    return rekening

# Fungsi untuk menambahkan rekening baru
def tambah_rekening():
    print("1. Rekening Tabungan\n2. Rekening Giro")
    jenis = input_angka("Pilih jenis rekening : ")
    if jenis not in (1, 2):
        print("invalid")
        return
    nama = input("Input nama pemilik: ")
    saldo = input_angka("Input saldo awal: ")
    rekening = bank.buat_rekening(jenis, nama, saldo)
    print("Rekening berhasil dibuat")
    rekening.tampilkan()

# Fungsi untuk mencari rekening berdasarkan nomor rekening atau nama pemilik
def cari_rekening():
    hasil = bank.cari(input("Input no rekening atau nama pemilik: "))
    if len(hasil) == 0:
        print("Data tidak ditemukan")
    for rekening in hasil:
        rekening.tampilkan()
        print()

# Fungsi untuk mengubah data/status rekening
def ubah_rekening():
    inp = 100
    while inp != 0:
        print("=" * 15)
        print("Ubah Data Rekening")
        print("1. Ubah nama pemilik\n2. Bekukan rekening\n3. Aktifkan rekening\n0. kembali")
        print("=" * 15)
        inp = input_angka("Pilih opsi : ")
        if inp == 1:
            rekening = ambil_rekening()
            if rekening is not None:
                rekening.ubah_nama_pemilik(input("Input nama pemilik baru: "))
        elif inp == 2:
            rekening = ambil_rekening()
            if rekening is not None:
                rekening.bekukan()
        elif inp == 3:
            rekening = ambil_rekening()
            if rekening is not None:
                rekening.aktifkan()
        elif inp == 0:
            print("Kembali.....")
        else:
            print("invalid")

# Fungsi untuk mengecek status rekening
def cek_status_rekening():
    rekening = ambil_rekening()
    if rekening is not None:
        rekening.cek_status()

# Fungsi untuk melakukan transaksi (setor, tarik, transfer)
def lakukan_transaksi(jenis):
    rekening = ambil_rekening()
    if rekening is None:
        return
    tujuan = None
    if jenis == "transfer":
        tujuan = ambil_rekening("Input no rekening tujuan: ")
        if tujuan is None:
            return
    jumlah = input_angka("Input jumlah: ")
    transaksi = bank.jalankan_transaksi(rekening, jenis, jumlah, tujuan)
    print("\nResi Transaksi")
    transaksi.cetak_resi()

# Fungsi untuk menampilkan riwayat transaksi rekening
def riwayat_transaksi():
    rekening = ambil_rekening()
    if rekening is not None:
        bank.tampilkan_riwayat(rekening)

# Fungsi untuk mengecek status transaksi berdasarkan ID transaksi
def cek_status_transaksi():
    transaksi = bank.cari_transaksi(input_angka("Input ID transaksi: "))
    if transaksi is None:
        print("Transaksi tidak ditemukan")
    else:
        transaksi.cek_status()

# Fungsi untuk memproses biaya admin bulanan pada rekening giro
def proses_bulanan():
    rekening = ambil_rekening()
    if rekening is not None:
        rekening.proses_bulanan()

# Fungsi utama untuk mengatur alur program
def main():
    
    # Data dummy
    bank.buat_rekening( 1, "Rifki", 1000000)
    bank.buat_rekening( 1, "Rizal", 150000)
    bank.buat_rekening( 2, "PT. Indonesia Emas", 100000000)
    bank.buat_rekening( 2, "CV. Indonesia Perak", 50000000)
    
    inp = 100
    while inp != 0:
        print("=" * 28)
        print(f"Sistem Rekening Bank Mini")
        print("=" * 28)
        print("1. Tambah rekening\n2. Tampilkan data rekening\n3. Cari rekening\n4. Ubah data rekening\n5. Cek status rekening")
        print("6. Setor tunai\n7. Tarik tunai\n8. Transfer\n9. Riwayat transaksi\n10. Cek status transaksi\n11. Proses bulanan\n0. exit")
        print("=" * 28)
        try:
            inp = input_angka("Pilih opsi : ")
            if inp == 1:
                tambah_rekening()
            elif inp == 2:
                bank.tampilkan_semua()
            elif inp == 3:
                cari_rekening()
            elif inp == 4:
                ubah_rekening()
            elif inp == 5:
                cek_status_rekening()
            elif inp == 6:
                lakukan_transaksi("setor")
            elif inp == 7:
                lakukan_transaksi("tarik")
            elif inp == 8:
                lakukan_transaksi("transfer")
            elif inp == 9:
                riwayat_transaksi()
            elif inp == 10:
                cek_status_transaksi()
            elif inp == 11:
                proses_bulanan()
            elif inp == 0:
                print("Exit.....")
            else:
                print("invalid")
        except ValueError as e:
            print(f"Gagal: {e}")


if __name__ == "__main__": # memanggil fungsi main()
    main()
