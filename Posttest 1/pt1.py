class Restoran:
    nama_restoran = "Vintage Restaurant"

    def __init__(self, nama_cabang, alamat, kas_restoran ):
        self.nama_cabang = nama_cabang
        self.alamat = alamat
        self.__kas_restoran = kas_restoran

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

class Menu:
    total_menu = 0

    def __init__(self, nama_menu, kategori_menu, harga_menu):
        self.nama_menu = nama_menu
        self.kategori_menu = kategori_menu
        self.__harga_menu = harga_menu
        Menu.total_menu += 1

    def tampilkan_menu(self):
        print(f"Menu : {self.nama_menu} | Kategori : {self.kategori_menu} | Harga : {self.__harga_menu}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama_menu"], data["kategori_menu"], data["harga_menu"])

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

class Reservasi:
    total_reservasi = 0

    def __init__(self, nama_reservasi, nomor_meja, jumlah_orang, status="Pending"):
        self.nama_reservasi = nama_reservasi
        self.nomor_meja = nomor_meja
        self.jumlah_orang = jumlah_orang
        self.__status = status
        Reservasi.total_reservasi += 1

    def tampilkan_reservasi(self):
        print(f"Nama reservasi : {self.nama_reservasi} | Meja : {self.nomor_meja} | Jumlah orang : {self.jumlah_orang} | status : {self.__status}")

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


# Uji coba tampilkan_restoran (Instance Method)
cabang1 = Restoran("Vintage Suryanata", "Jl.P Suryanta", 20000000)
cabang1.tampilkan_restoran() # output : Restoran : Vintage Suryanata | Alamat : Jl.P Suryanta) | Kas : 20000000

# Uji coba ganti_nama_restoran (Class Method)
Restoran.ganti_nama_restoran("Vintage Fine Dining Restaurant")
print(Restoran.nama_restoran)  # output : Vintage Fine Dining Restaurant

# Uji coba getter dan setter
print(f"Kas : Rp.{cabang1.kas}") # output : Kas : Rp.20000000
cabang1.kas = 25000000 # valid

try :
    cabang1.kas = -25000000 # invalid
except ValueError as e:
    print(f"Error : {e}") # output : Error : Kas harus bernilai positf !

# Uji coba validasi_jam_operasional (Static Method)
print(f"Status Restoran jam 11.00 : {Restoran.validasi_jam_operasional(11)}") # output : Status Restoran jam 11.00 : Restoran sedang buka !

# ----------------
# Uji coba tampilkan_menu (Instance Method)
menu1 = Menu("Nasi Goreng", "Makanan", 15000)
menu1.tampilkan_menu() # output : Menu : Nasi Goreng | Kategori : Makanan | Harga : 15000

# Uji coba Class Method 
menu2 = Menu.dari_dict({"nama_menu" : "Es Teh", "kategori_menu" : "Minuman", "harga_menu" : 7000})
menu2.tampilkan_menu() # output : Menu : Es Teh | Kategori : Minuman | Harga : 7000

# Uji coba getter, setter, Static Method
print(f"Harga Nasi goreng : Rp.{menu1.harga}")  # output : Harga Nasi goreng : Rp.15000
print(f"Harga Rp.1.200.000 setelah diskon : {Menu.diskon(1200000)}")  # valid. Output : Harga Rp.1.200.000 setelah diskon : 900000.0

try :
    menu1.harga = -15000 # invalid
except ValueError as e:
    print(f"Error : {e}")  # output : Error : Harga harus bernilai positf !

# -------------
# Uji coba tampilkan_reservasi (Instance Method)
reservasi1 = Reservasi("Rafli", 13, 2, "Booked")
reservasi1.tampilkan_reservasi()  # output : Nama reservasi : Rafli | Meja : 13 | Jumlah orang : 2 | status : Booked

# Uji coba tampilkan_reservasi (Class Method)
reservasi2 = Reservasi.dari_dict({"nama_reservasi" : "Putra", "nomor_meja" : 10, "jumlah_orang" : 3, "status" : "Pending"})
reservasi2.tampilkan_reservasi()  # output : Nama reservasi : Putra | Meja : 10 | Jumlah orang : 3 | status : Pending

# Uji coba getter, setter dan validasi_nomor_meja (Static Method)
print(Reservasi.validasi_nomor_meja(5)) # output : Meja 5 tersedia !
reservasi1.status_reservasi = "Canceled" # valid

print(f"Status reservasi1 baru : {reservasi1.status_reservasi}")  # output : Status reservasi1 baru : Canceled

try :
    reservasi1.status_reservasi = "Batal" # invalid
except ValueError as e:
    print(f"Error : {e}")  # output : Error : Status tidak valid ! Pilihan status : Pending, Booked, Canceled 