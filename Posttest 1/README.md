Untuk penjelasan terkait perubahan kode program sebagai berikut : 
1. Agregasi (Restoran -> Menu) : 
- Yang dimana memiliki hubungan "memiliki" yang bersifat lemah. 
- Objek Restoran menampung daftar objek  Menu (yaitu  Makanan dan Minuman) di dalam list "self.daftar_menu" melalui method "tambahkan_menu()".
- Jika objek Restoran dihapus, maka objek Menu masih tetap berdiri sendiri dan tidak terhapus.
- Kode yang ditambahkan : 

class Makanan(Menu):
    def __init__(self, nama_menu, kategori_menu, harga_menu, tingkat_pedas):
        super().__init__(nama_menu, kategori_menu, harga_menu)
        self.tingkat_pedas = tingkat_pedas 

    def tampilkan_info(self):
        print(f"Menu : {self.nama_menu} | Kategori : {self.kategori_menu} | Harga : {self._harga_menu} | Tingkat Kepedasan : {self.tingkat_pedas}")

class Minuman(Menu):
    def __init__(self, nama_menu, kategori_menu, harga_menu, ukuran_gelas):
        super().__init__(nama_menu, kategori_menu, harga_menu)
        self.ukuran_gelas = ukuran_gelas

    def tampilkan_info(self):
        print(f"Menu : {self.nama_menu} | Kategori : {self.kategori_menu} | Harga : {self._harga_menu} | Ukuran : {self.ukuran_gelas}")

- Untuk tes kodenya : 
cabang1.tambahkan_menu(seblak)
cabang1.tampilkan_semua_menu()

- Outputnya :
Menu Seblak berhasil ditambahkan!
Menu : Seblak | Kategori : Makanan | Harga : 150000 | Tingkat Kepedasan : 5


2. Komposisi (Reservasi -> Meja) :
- Yang dimana memiliki hubungan "memiliki" yang bersifat sangat kuat.
- Objek Meja yang dibuat secara langsung didalam konstruktut "__init__" dari Reservasi (self.detail_meja = Meja()).
- Meja tidak dapat berdiri secara independen tanpa Reservasi.
- Untuk Kodenya : 

class Meja:
    def __init__(self, nomor_meja, kapasitas):
        self.nomor_meja = nomor_meja
        self.kapasitas = kapasitas

- Untuk tes kodenya : 
res1 = Reservasi("Rafli", 13, 2, 2)
print(f"Nama : {res1.nama_reservasi} | Nomor Meja : {res1.detail_meja.nomor_meja} | Kapasitas : {res1.detail_meja.kapasitas} | Total Reservasi : {Reservasi.total_reservasi}")

- Untuk outputnya :
Nama : Rafli | Nomor Meja : 13 | Kapasitas : 2 | Total Reservasi : 1

3. Asosiasi (Pelanggan -> Reservasi) : 
- Yang dimana memiliki hubungan interaksi biasa antar objek.
- Class Pelanggan berinteraksi dengan Reservasi melalui method. "buat_reservasi(reservasi)" dengan menerima objek Reservasi sebagai parameternya untuk mencetak detail pemesanan.
- Untuk Kodenya : 

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

- Untuk tes kodenya : 
p1 = Pelanggan("Rafli", 000)
p1.buat_reservasi(res1)

- Untuk outputnya :
======= DETAIL RESERVASI ========
Nama       : Rafli
No.Hp      : 0
Nomor Meja : 13
Kapasitas : 2 orang

4. Overriding Method : 
- Mengambil method pada superclass Menu yaitu method tampilkan_info(), lalu mengubah isinya pada class Makanan dan class Minuman