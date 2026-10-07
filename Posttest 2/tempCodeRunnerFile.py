class Pelanggan:
    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp

    def buat_reservasi(self, reservasi):
        print("======= DETAIL RESERVASI ========")
        print(f"Nama       : {self.nama}")
        print(f"No.Hp      : {self.no_hp}")
        print(f"Nomor Meja : {reservasi.detail_meja.nomor_meja}")
        print(f"Kapasitas : {reservasi.detail_meja.kapasitas} orang")