class Rekening:
    counter = 1000
    # Constructor
    def __init__(self, nama_pemilik, saldo_awal=0):
        if nama_pemilik.strip() == "" or saldo_awal < 0:
            raise ValueError("Nama/saldo awal tidak valid")
        Rekening.counter += 1
        self.__no_rekening = Rekening.counter
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo_awal
        self.__status = "Aktif"
    
    # method untuk mendapatkan nomor rekening
    def get_no_rekening(self):
        return self.__no_rekening

    # method untuk mendapatkan nama pemilik
    def get_nama_pemilik(self):
        return self.__nama_pemilik

    # method untuk mendapatkan saldo
    def get_saldo(self):
        return self.__saldo

    # method untuk mendapatkan status
    def get_status(self):
        return self.__status

    # method untuk mendapatkan jenis rekening
    def get_jenis(self):
        return "Rekening"

    # method untuk mendapatkan dana tersedia
    def get_dana_tersedia(self):
        return self.__saldo

    # method untuk menambah saldo
    def _tambah_saldo(self, jumlah):
        self.__saldo += jumlah

    # method untuk mengurangi saldo
    def _kurangi_saldo(self, jumlah):
        self.__saldo -= jumlah

    # Method untuk mengecek transaksi
    def _cek_transaksi(self, jumlah):
        if self.__status != "Aktif":
            print(f"Rekening {self.__no_rekening} sedang {self.__status}")
            return False
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0")
            return False
        return True

    # method untuk mengubah nama pemilik
    def ubah_nama_pemilik(self, nama_baru):
        if nama_baru.strip() == "":
            print("Gagal mengubah nama pemilik")
            return False
        self.__nama_pemilik = nama_baru
        print(f"Berhasil mengubah nama pemilik rekening {self.__no_rekening}")
        return True

    # Method untuk membekukan rekening
    def bekukan(self):
        if self.__status == "Dibekukan":
            print(f"Rekening {self.__no_rekening} sudah dibekukan")
            return False
        self.__status = "Dibekukan"
        print(f"Berhasil membekukan rekening {self.__no_rekening}")
        return True

    # Method untuk mengaktifkan rekening
    def aktifkan(self):
        if self.__status == "Aktif":
            print(f"Rekening {self.__no_rekening} sudah aktif")
            return False
        self.__status = "Aktif"
        print(f"Berhasil mengaktifkan rekening {self.__no_rekening}")
        return True

    # Method untuk menyetor ke rekening
    def setor(self, jumlah):
        if not self._cek_transaksi(jumlah):
            return False
        self._tambah_saldo(jumlah)
        print(f"Berhasil setor Rp {jumlah} ke rekening {self.__no_rekening}")
        return True

    # Method untuk menarik saldo rekening
    def tarik(self, jumlah):
        if not self._cek_transaksi(jumlah):
            return False
        if jumlah > self.get_dana_tersedia():
            print(f"Gagal tarik Rp {jumlah}, dana tersedia Rp {self.get_dana_tersedia()}")
            return False
        self._kurangi_saldo(jumlah)
        print(f"Berhasil tarik Rp {jumlah} dari rekening {self.__no_rekening}")
        return True

    # Method untuk mentransfer saldo ke rekening lain
    def transfer(self, tujuan, jumlah):
        if tujuan.get_no_rekening() == self.__no_rekening:
            print("Gagal transfer ke rekening sendiri")
            return False
        if tujuan.get_status() != "Aktif":
            print(f"Rekening tujuan {tujuan.get_no_rekening()} sedang {tujuan.get_status()}")
            return False
        if not self.tarik(jumlah):
            return False
        tujuan._tambah_saldo(jumlah)
        print(f"Berhasil transfer Rp {jumlah} ke rekening {tujuan.get_no_rekening()}")
        return True
    
    # Method untuk melakukan proses bulanan
    def proses_bulanan(self):
        print("Tidak ada proses bulanan untuk rekening ini")
        return False
    
    # Method untuk menampilkan data rekening
    def tampilkan(self):
        print(f"No rekening = {self.__no_rekening}")
        print(f"Jenis rekening = {self.get_jenis()}")
        print(f"Nama pemilik = {self.__nama_pemilik}")
        print(f"Saldo = {self.__saldo}")
        print(f"Status = {self.__status}")

    # Method untuk mengecek status rekening
    def cek_status(self):
        print(f"No rekening = {self.__no_rekening}")
        print(f"Status = {self.__status}")
        print(f"Saldo = {self.__saldo}")
        print(f"Dana tersedia = {self.get_dana_tersedia()}")
