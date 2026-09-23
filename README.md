Sistem Manajemen Restoran dan Reservasi Meja

Konsep dari Sistem Manajemen Restoran dan Reservasi Meja dirancang untuk mensimulasikan operasional dasar dari sebuah Restoran berdasarkan program berbasis objek yang rapi dan terstruktur.

Penjelasan lebih lanjut terkait program ini adalah sebagai berikut :

1.Terdapat 3 utama :
a. Restoran :
- Menyimpan informasi seperti, nama_restoran, nama cabang, alamat, jam operasional, dan kas internal.
- Class ini menjadi induk (parent) dari class-class lainnya.
- Class ini memiliki atribut yang terdiri dari nama_cabang (publik), alamat(publik), kas_restoran (private).
- Instance Method dari class ini adalah tampilkan_restoran. Dengan parameter self agar bisa membaca dan mengubah instance milik 
objek dan juga tetap bisa membaca atribut kelas. Dengan output menampilkan informasi restoran seperti nama cabang, alamat dan kas.
- Class Method dari class ini adalah ganti_nama_restoran. Dengan parameter self dan nama_baru. Dengan output mengubah nama dari restoran yang diinginkan.
- Static Method dari class ini adalah validasi_jam_operasional. Dengan parameter jam, yang akan memvalidasi jam buka dan jam tutup restoran. Dengan output "Restoran sedang buka !" jika jam >= 9 dan "Restoran sedang tutup !" jika jam >= 22.
- Getter di class ini akan mengambil nilai dari kas_restoran yang bersifat private. Sehingga bisa mengambil atau menampilkan nilai dari kas_restoran.
- Setter di class ini akan memvalidasi inputan dari kas_baru agar bernilai positif, lalu mengubah nilai kas_restoran dengan kas_baru.

b. Menu     : 
- Menyimpan informasi seperti, nama menu, kategori menu (makanan, minuman), dan harga.
- Class ini memiliki atribut yang terdiri dari total_menu nama_menu, kategori_menu, harga_menu.
- Instance Method dari class ini adalah tampilkan_Menu. Dengan parameter self agar bisa membaca dan mengubah instance milik 
objek dan juga tetap bisa membaca atribut kelas. Dengan output menampilkan informasi menu seperti nama menu, kategori menu dan harga.
- Class Method dari class ini adalah ganti_nama_restoran. Dengan parameter self dan nama_baru. Dengan output mengubah nama dari restoran yang diinginkan.

c. Reservasi : 
- Menyimpan informasi terkait reservasi seperti, nama yang melakukan reservasi, nomor meja yang direservasi, serta jumlah orang agar dapat memenuhi kebutuhan pelanggan.
- Class ini memiliki atribut yang terdiri dari nama_reservasi, nomor_meja, jumlah_orang, status="Pending".
- Instance Method dari class ini adalah tampilkan_reservasi. Dengan parameter self agar bisa membaca dan mengubah instance milik 
objek dan juga tetap bisa membaca atribut kelas. Dengan output menampilkan informasi reservasi seperti nama yang melakukan reservasi, nomor meja, jumlah orang dan status.
- 
