from rekening import Rekening


class RekeningTabungan(Rekening):
    # Constructor
    def __init__(self, nama_pemilik, saldo_awal=0, suku_bunga=3, saldo_minimum=50000, batas_tarik=5000000):
        if suku_bunga < 0 or saldo_minimum < 0 or batas_tarik <= 0:
            raise ValueError("Data rekening tabungan tidak valid")
        if saldo_awal < saldo_minimum:
            raise ValueError(f"Saldo awal minimal Rp {saldo_minimum}")
        super().__init__(nama_pemilik, saldo_awal) # atribut inherit dari kelas Rekening
        self.__suku_bunga = suku_bunga
        self.__saldo_minimum = saldo_minimum
        self.__batas_tarik = batas_tarik

    # method untuk mendapatkan suku bunga
    def get_suku_bunga(self):
        return self.__suku_bunga

    # method untuk mendapatkan saldo minimum,
    def get_saldo_minimum(self):
        return self.__saldo_minimum

    # method untuk mendapatkan batas 
    def get_batas_tarik(self):
        return self.__batas_tarik

    # method untuk mendapatkan jenis rekening
    def get_jenis(self):
        return "Tabungan"
    
    # method untuk mendapatkan dana tersedia
    def get_dana_tersedia(self):
        return self.get_saldo() - self.__saldo_minimum

    # method untuk menghitung bunga
    def hitung_bunga(self):
        return int(self.get_saldo() * self.__suku_bunga / 100 / 12)

    # method untuk melakukan tarik
    def tarik(self, jumlah):
        if jumlah > self.__batas_tarik:
            print(f"Gagal tarik Rp {jumlah}, batas tarik Rp {self.__batas_tarik}")
            return False
        return super().tarik(jumlah)

    # method untuk melakukan proses bulanan
    def proses_bulanan(self):
        if self.get_status() != "Aktif":
            print(f"Rekening {self.get_no_rekening()} sedang {self.get_status()}")
            return False
        bunga = self.hitung_bunga()
        if bunga <= 0:
            print("Bunga bulan ini belum tersedia")
            return False
        self._tambah_saldo(bunga)
        print(f"Berhasil menambahkan bunga Rp {bunga} ke rekening {self.get_no_rekening()}")
        return True

    # method untuk menampilkan data rekening
    def tampilkan(self):
        super().tampilkan()
        print(f"Suku bunga = {self.__suku_bunga}% per tahun")
        print(f"Saldo minimum = {self.__saldo_minimum}")
        print(f"Batas tarik = {self.__batas_tarik}")
