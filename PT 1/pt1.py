class Restoran:
    nama_restoran = "Vintage Restaurant"

    def __init__(self, nama_cabang, alamat, kas_restoran ):
        self.nama_cabang = nama_cabang
        self.alamat = alamat
        self.__kas_restoran = kas_restoran

    def tampilkan_restoran(self):
        print(f"(Restoran : {self.nama_cabang} | Alamat : {self.alamat}) | Kas : {self.kas}")

    @classmethod
    def ganti_nama_restoran(cls, nama_baru):
        cls.nama_restoran = nama_baru

        return nama_baru

    @property
    def kas(self):
        return self.__kas_restoran

    @kas.setter
    def kas(self, kas_baru):
        if kas_baru < 0:
            raise ValueError("Kas harus bernilai positf !")
        
        self.__kas_restoran = kas_baru

    @staticmethod
    def validasi_jam_operasional(jam):
        if 9 <= jam <= 22:
            return "Restoran sedang buka !"
        else:
            return "Restoran sedang tutup !"

class Menu:
    total_menu = 0

    def __init__(self, nama_menu, kategori_menu, harga_menu):
        self.nama_menu = nama_menu
        self.kategori_menu = kategori_menu
        self.__harga_menu = harga_menu
        Menu.total_menu += 1

    def tampilkan_menu(self):
        print(f"(Menu : {self.nama_menu} | Kategori : {self.kategori_menu} | Harga : {self.__harga_menu})")

    @property
    def harga(self):
        return self.__harga_menu

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru < 0:
            raise ValueError("Harga harus bernilai positf !")

        self.__harga_menu = harga_baru

    @staticmethod
    def diskon(total_pembelian):
        if total_pembelian >= 1000000:
            potongan = total_pembelian * 0.25
            return total_pembelian - potongan

        return total_pembelian

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama_menu"], data["kategori_menu"], data["harga_menu"])


class Reservasi:
    total_reservasi = 0

    def __init__(self, nama_reservasi, nomor_meja, jumlah_orang, status="Pending"):
        self.nama_reservasi = nama_reservasi
        self.nomor_meja = nomor_meja
        self.jumlah_orang = jumlah_orang
        self.__status = status
        Reservasi.total_reservasi += 1

    def tampilkan_reservasi(self):
        print(f"(Nama reservasi : {self.nama_reservasi} | Meja : {self.nomor_meja} | Jumlah orang : {self.jumlah_orang} | status : {self.__status})")

    @property
    def status_reservasi(self):
        return self.__status

    @status_reservasi.setter
    def status_reservasi(self, status_baru="Booked"):
        jenis_status = ["Pending", "Booked", "Canceled"]

        if status_baru not in jenis_status:
            raise ValueError("Status tidak valid ! Pilihan status : Pending, Booked, Canceled ")
        self.__status =status_baru

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama_reservasi"], data["nomor_meja"], data["jumlah_orang"], data["status"])

    @staticmethod
    def validasi_nomor_meja(nomor_meja):
        if 1 <= nomor_meja <= 50 :
            return f"Meja {nomor_meja} tersedia !"

        return f"Meja {nomor_meja} tidak ada ! (Nomor Meja hanya tersedia 1-50)"