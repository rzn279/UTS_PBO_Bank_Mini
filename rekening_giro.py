from rekening import Rekening

class RekeningGiro(Rekening):
    # Constructor
    def __init__(self, nama_pemilik, saldo_awal=0, limit_cerukan=5000000, biaya_admin=25000, setoran_minimum=100000):
        if limit_cerukan < 0 or biaya_admin < 0 or setoran_minimum < 0:
            raise ValueError("Data rekening giro tidak valid")
        if saldo_awal < setoran_minimum:
            raise ValueError(f"Saldo awal minimal Rp {setoran_minimum}")
        super().__init__(nama_pemilik, saldo_awal) # atribut inherit dari kelas Rekening
        self.__limit_cerukan = limit_cerukan
        self.__biaya_admin = biaya_admin
        self.__setoran_minimum = setoran_minimum

    # Method untuk mendapatkan limit cerukan
    def get_limit_cerukan(self):
        return self.__limit_cerukan

    # Method untuk mendapatkan biaya admin
    def get_biaya_admin(self):
        return self.__biaya_admin

    # Method untuk mendapatkan setoran minimum
    def get_setoran_minimum(self):
        return self.__setoran_minimum

    # Method untuk mendapatkan jenis rekening
    def get_jenis(self):
        return "Giro"

    # Method untuk mendapatkan dana tersedia
    def get_dana_tersedia(self):
        return self.get_saldo() + self.__limit_cerukan

    # Method untuk melakukan setor
    def setor(self, jumlah):
        if jumlah < self.__setoran_minimum:
            print(f"Gagal setor Rp {jumlah}, setoran minimum Rp {self.__setoran_minimum}")
            return False
        return super().setor(jumlah)

    # Method untuk melakukan  proses bulanan
    def proses_bulanan(self):
        if self.get_status() != "Aktif":
            print(f"Rekening {self.get_no_rekening()} sedang {self.get_status()}")
            return False
        if self.get_dana_tersedia() < self.__biaya_admin:
            print("Gagal memotong biaya admin, dana tersedia tidak mencukupi")
            return False
        self._kurangi_saldo(self.__biaya_admin)
        print(f"Berhasil memotong biaya admin Rp {self.__biaya_admin} dari rekening {self.get_no_rekening()}")
        return True

    # Method untuk melakukan menampilkan data rekening
    def tampilkan(self):
        super().tampilkan()
        print(f"Limit cerukan = {self.__limit_cerukan}")
        print(f"Biaya admin = {self.__biaya_admin}")
        print(f"Setoran minimum = {self.__setoran_minimum}")
