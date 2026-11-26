from rekening_tabungan import RekeningTabungan
from rekening_giro import RekeningGiro
from transaksi import Transaksi


class Bank:
    # constructor
    def __init__(self):
        self.__daftar_rekening = []
        self.__daftar_transaksi = []

    # Method untuk mendapatkan jumlah rekening 
    def get_jumlah_rekening(self):
        return len(self.__daftar_rekening)

    # Method untuk mendapatkan jumlah transaksi
    def get_jumlah_transaksi(self):
        return len(self.__daftar_transaksi)

    # Method untuk membuat rekening baru
    def buat_rekening(self, jenis, nama_pemilik, saldo_awal):
        if jenis == 1:
            rekening = RekeningTabungan(nama_pemilik, saldo_awal)
        elif jenis == 2:
            rekening = RekeningGiro(nama_pemilik, saldo_awal)
        else:
            raise ValueError("Jenis rekening tidak valid")
        self.__daftar_rekening.append(rekening)
        return rekening

    # Method untuk mencari rekening berdasarkan nomor rekening
    def cari_rekening(self, no_rekening):
        for rekening in self.__daftar_rekening:
            if rekening.get_no_rekening() == no_rekening:
                return rekening
        return None

    # Method untuk mencari rekening berdasarkan nomor rekening atau nama pemilik
    def cari(self, kata_kunci):
        hasil = []
        for rekening in self.__daftar_rekening:
            if kata_kunci == str(rekening.get_no_rekening()) or kata_kunci.lower() in rekening.get_nama_pemilik().lower():
                hasil.append(rekening)
        return hasil

    # Method untuk menghitung total dana di semua rekening
    def hitung_total_dana(self):
        total = 0
        for rekening in self.__daftar_rekening:
            total += rekening.get_saldo()
        return total

    # Method untuk menampilkan semua rekening
    def tampilkan_semua(self):
        if len(self.__daftar_rekening) == 0:
            print("Belum ada data rekening")
            return
        print()
        for rekening in self.__daftar_rekening:
            rekening.tampilkan()
            print()
        print(f"Jumlah rekening = {self.get_jumlah_rekening()}")
        print(f"Total dana = {self.hitung_total_dana()}")

    # Method untuk memproses transaksi
    def jalankan_transaksi(self, rekening, jenis, jumlah, tujuan=None):
        transaksi = Transaksi(rekening, jenis, jumlah, tujuan)
        self.__daftar_transaksi.append(transaksi)
        transaksi.proses_transaksi()
        return transaksi

    # Method untuk mencari transaksi berdasarkan ID transaksi
    def cari_transaksi(self, id_transaksi):
        for transaksi in self.__daftar_transaksi:
            if transaksi.get_id_transaksi() == id_transaksi:
                return transaksi
        return None

    # Method untuk menampilkan riwayat transaksi rekening
    def tampilkan_riwayat(self, rekening):
        ada = False
        for transaksi in self.__daftar_transaksi:
            if transaksi.get_rekening() is rekening:
                print(f"{transaksi.get_id_transaksi()}. {transaksi.get_jenis()} Rp {transaksi.get_jumlah()} - {transaksi.get_status()}")
                ada = True
        if not ada:
            print("Belum ada transaksi")
