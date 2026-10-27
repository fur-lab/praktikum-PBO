from abc import ABC, abstractmethod

class Restoran:
    nama_restoran = "Vintage Restaurant"

    def __init__(self, nama_cabang, alamat, kas_restoran):
        self.nama_cabang = nama_cabang
        self.alamat = alamat
        self.__kas_restoran = kas_restoran
        self.daftar_menu = [] # Agregasi

    def tampilkan_restoran(self):
        print(f"Restoran : {self.nama_cabang} | Alamat : {self.alamat}) | Kas : {self.kas}")

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

    
    def tambahkan_menu(self, menu):
        self.daftar_menu.append(menu)
        print(f"Menu {menu.nama_menu} berhasil ditambahkan!")

    def tampilkan_semua_menu(self):
        for i in self.daftar_menu:
            i.tampilkan_info()

class Menu(ABC):
    total_menu = 0

    def __init__(self, nama_menu, kategori_menu, harga_menu):
        self.nama_menu = nama_menu
        self.kategori_menu = kategori_menu
        self._harga_menu = harga_menu
        Menu.total_menu += 1

    def __str__(self):
        return f"{self.nama_menu} ({self.kategori_menu} - Rp.{self._harga_menu})"

    def __add__(self, other):
        if isinstance(other, Menu):
            return self._harga_menu + other._harga_menu
        return NotImplemented

    @abstractmethod
    def tampilkan_info(self):
        pass

    @abstractmethod
    def hitung_total(self, jumlah):
        pass

    def deskripsi_singkat(self):
        print(f"{{self.kategori_menu}}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama_menu"], data["kategori_menu"], data["harga_menu"])

    @property
    def harga(self):
        return self._harga_menu

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru < 0:
            raise ValueError("Harga harus bernilai positf !")

        self._harga_menu = harga_baru

    @staticmethod   
    def diskon(total_pembelian):
        if total_pembelian >= 1000000:
            potongan = total_pembelian * 0.25
            return total_pembelian - potongan

        return total_pembelian

class Makanan(Menu):
    def __init__(self, nama_menu, kategori_menu, harga_menu, tingkat_pedas):
        super().__init__(nama_menu, kategori_menu, harga_menu)
        self.tingkat_pedas = tingkat_pedas 

    def tampilkan_info(self):
        print(f"Menu : {self.nama_menu} | Kategori : {self.kategori_menu} | Harga : {self._harga_menu} | Tingkat Kepedasan : {self.tingkat_pedas}")

    def hitung_total(self, jumlah):
        return self._harga_menu * jumlah

class Minuman(Menu):
    def __init__(self, nama_menu, kategori_menu, harga_menu, ukuran_gelas):
        super().__init__(nama_menu, kategori_menu, harga_menu)
        self.ukuran_gelas = ukuran_gelas

    def tampilkan_info(self):
        print(f"Menu : {self.nama_menu} | Kategori : {self.kategori_menu} | Harga : {self._harga_menu} | Ukuran : {self.ukuran_gelas}")

    def hitung_total(self, jumlah):
        return self._harga_menu * jumlah

class Meja:
    def __init__(self, nomor_meja, kapasitas):
        self.nomor_meja = nomor_meja
        self.kapasitas = kapasitas

class Reservasi:
    total_reservasi = 0

    def __init__(self, nama_reservasi, nomor_meja, jumlah_orang, kapasitas_meja = 4, status="Pending"):
        self.nama_reservasi = nama_reservasi
        self.jumlah_orang = jumlah_orang
        self.__status = status
        self.detail_meja = Meja(nomor_meja, kapasitas_meja)
        Reservasi.total_reservasi += 1

    def tampilkan_reservasi(self):
        print(f"Nama reservasi : {self.nama_reservasi} | Meja : {self.detail_meja.nomor_meja} | Jumlah orang : {self.jumlah_orang} | status : {self.__status}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama_reservasi"], data["nomor_meja"], data["jumlah_orang"], data["status"])

    @property
    def status_reservasi(self):
        return self.__status

    @status_reservasi.setter
    def status_reservasi(self, status_baru="Booked"):
        jenis_status = ["Pending", "Booked", "Canceled"]

        if status_baru not in jenis_status:
            raise ValueError("Status tidak valid ! Pilihan status : Pending, Booked, Canceled ")
        self.__status =status_baru

    @staticmethod
    def validasi_nomor_meja(nomor_meja):
        if 1 <= nomor_meja <= 50 :
            return f"Meja {nomor_meja} tersedia !"

        return f"Meja {nomor_meja} tidak ada ! (Nomor Meja hanya tersedia 1-50)"

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

class NotifikasiWhatsapp:
    def kirim(self, pesan):
        print(f"Notifikasi WA : {pesan}")

class NotifikasiEmail:
    def kirim(self, pesan):
        print(f"Notifikasi Email : {pesan}")

def kirim_notifikasi(layanan, pesan):
    layanan.kirim(pesan)

# ================== UJI COBA ================================  
# ABSTRAKSI
try : 
    tes_menu = Menu("Bakso", "Makanan", 15000 )

except TypeError as err :
    print("Class Menu tidak bisa diinstansiasi langsung !")
    print(f"Pesan Error : {err}\n")

# OVERLOADING
es_teh = Minuman("Es Teh", "Minuman", 5000, "Large")
seblak = Makanan("Seblak", "Makanan", 15000, 5)

print(seblak) # __str__
total = seblak + es_teh # __add__
print(f"Total Pesanan = Rp.{total}")

# DUCK TYPING
wa = NotifikasiWhatsapp()
email = NotifikasiEmail()

kirim_notifikasi(wa, "Reservasi Meja 15 Telah Berhasil !")
kirim_notifikasi(email, "Struk Pembayaran Telah Terkirim.")
