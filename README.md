Sistem Manajemen Restoran dan Reservasi Meja

Konsep dari Sistem Manajemen Restoran dan Reservasi Meja dirancang untuk mensimulasikan operasional dasar dari sebuah Restoran berdasarkan program berbasis objek yang rapi dan terstruktur.

Penjelasan lebih lanjut terkait program ini adalah sebagai berikut :

1.Terdapat 3 utama :
 |_ a. Restoran : - Menyimpan informasi seperti, nama_restoran, nama cabang, alamat, jam operasional, dan kas internal.
                  - Class ini menjadi induk (parent) dari class-class lainnya. 
                  - Class ini memiliki atribut yang terdiri dari nama_cabang, alamat, kas_restoran.

 |_ b. Menu     : - Menyimpan informasi seperti, nama menu, kategori menu (makanan, minuman), dan harga.
                  - Class ini memiliki atribut yang terdiri dari total_menu nama_menu, kategori_menu, harga_menu.

 |_ c. Reservasi : - Menyimpan informasi terkait reservasi seperti, nama yang melakukan reservasi, nomor meja yang direservasi, serta jumlah orang agar dapat memenuhi kebutuhan pelanggan.
                   - Class ini memiliki atribut yang terdiri dari nama_reservasi, nomor_meja, jumlah_orang, status="Pending".
