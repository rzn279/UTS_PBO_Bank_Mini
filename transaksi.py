from rekening import Rekening


class Transaksi:
    counter = 0
    # Constructor
    def __init__(self, rekening, jenis, jumlah, tujuan=None):
        if not isinstance(rekening, Rekening):
            raise ValueError("Rekening tidak valid")
        if jenis not in ("setor", "tarik", "transfer"):
            raise ValueError("Jenis transaksi tidak valid")
        if jumlah <= 0:
            raise ValueError("Jumlah transaksi harus lebih dari 0")
        if jenis == "transfer" and not isinstance(tujuan, Rekening):
            raise ValueError("Rekening tujuan tidak valid")
        Transaksi.counter += 1
        self.__id_transaksi = Transaksi.counter
        self.__rekening = rekening
        self.__jenis = jenis
        self.__jumlah = jumlah
        self.__tujuan = tujuan
        self.__status = "Pending"

    # Method untuk mendapatkan ID transaksi
    def get_id_transaksi(self):
        return self.__id_transaksi

    # Method untuk mendapatkan rekening
    def get_rekening(self):
        return self.__rekening

    # Method untuk mendapatkan jenis
    def get_jenis(self):
        return self.__jenis

    # Method untuk mendapatkan jumlah
    def get_jumlah(self):
        return self.__jumlah

    # Method untuk mendapatkan tujuan transaksi
    def get_tujuan(self):
        return self.__tujuan

    # Method untuk mendapatkan status transaksi
    def get_status(self):
        return self.__status

    # Method untuk memproses transaksi
    def proses_transaksi(self):
        if self.__status != "Pending":
            print("Transaksi sudah pernah diproses")
            return False
        if self.__jenis == "setor":
            berhasil = self.__rekening.setor(self.__jumlah)
        elif self.__jenis == "tarik":
            berhasil = self.__rekening.tarik(self.__jumlah)
        else:
            berhasil = self.__rekening.transfer(self.__tujuan, self.__jumlah)
        if berhasil:
            self.__status = "Berhasil"
            print("Transaksi berhasil!")
        else:
            self.__status = "Gagal"
            print("Transaksi gagal!")
        return berhasil

    # Method untuk mengecek status transaksi
    def cek_status(self):
        print(f"ID Transaksi = {self.__id_transaksi}")
        print(f"Jenis = {self.__jenis}")
        print(f"Status = {self.__status}")

    # Method untuk mencetak resi transaksi
    def cetak_resi(self):
        print(f"ID Transaksi: {self.__id_transaksi}")
        print(f"No Rekening: {self.__rekening.get_no_rekening()}")
        print(f"Pemilik: {self.__rekening.get_nama_pemilik()}")
        print(f"Jenis: {self.__jenis}")
        if self.__tujuan is not None:
            print(f"Rekening Tujuan: {self.__tujuan.get_no_rekening()}")
        print(f"Jumlah: {self.__jumlah}")
        print(f"Status: {self.__status}")
        print(f"Saldo Akhir: {self.__rekening.get_saldo()}")
