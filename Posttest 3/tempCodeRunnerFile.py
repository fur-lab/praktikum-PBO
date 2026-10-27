class NotifikasiWhatsapp:
    def kirim(self, pesan):
        print(f"Notifikasi WA : {pesan}")

class NotifikasiEmail:
    def kirim(self, pesan):
        print(f"Notifikasi Email : {pesan}")

def kirim_notifikasi(layanan, pesan):
    layanan.kirim(pesan)