import heapq
import datetime

class PriorityQueue:
    def __init__(self):
        self.counter = 0  # Counter to keep track of insertion order
        self.items = []

    def enqueue(self, item, priority):
        timestamp = self.counter  # Use counter as the secondary key for maintaining order
        heapq.heappush(self.items, (priority, timestamp, self.counter, item))
        self.counter += 1

    def dequeue(self):
        return heapq.heappop(self.items)[3]

    def is_empty(self):
        return len(self.items) == 0
    
    def queue_view(self):
        sorted_items = sorted(self.items, key=lambda x: (x[0], x[1], x[2]))
        for i, (priority, timestamp, counter, (nama_nasabah, keperluan, time_of_enqueue)) in enumerate(sorted_items, start=1):
            print(f"{i}. {nama_nasabah} - {keperluan} (Priority: {priority}) at {time_of_enqueue}")
    
    def size(self):
        return len(self.items)
    
    def search_by_name(self, name):
        results = []
        for i, (priority, timestamp, counter, (nama_nasabah, keperluan, time_of_enqueue)) in enumerate(self.items):
            if name.lower() in nama_nasabah.lower():
                results.append((i + 1, nama_nasabah, keperluan, priority, time_of_enqueue))
        return results

# Deklarasi Variabel
layanan = 0
keperluan = 0
user = 0
pengerjaan = 0
jenisPegawai = 0
namaNasabah = ""

# Deklarasi pelayanan di Customer Service
keperluanCS_1 = "Pembukaan rekening bank"
keperluanCS_2 = "Pelayanan masalah pada rekening nasabah"
keperluanCS_3 = "Informasi saldo dan mutasi nasabah"
keperluanCS_4 = "Administrasi buku cek dan buku tabungan"

# Deklarasi pelayanan di Teller
keperluanTeller_1 = "Penyetoran tabungan dan deposito"
keperluanTeller_2 = "Pencatatan tabungan dan deposito"
keperluanTeller_3 = "Pencatatan transaksi buku tabungan"

# Initialize priorities
PRIORITY_HIGH = 0
PRIORITY_LOW = 1

# Initialize priority card
KARTU_PRIORITAS_YES = 'ya'
KARTU_PRIORITAS_NO = 'tidak'


queueAntrianCS = PriorityQueue()  # Menggunakan Priority Queue
queueAntrianTeller = PriorityQueue()  # Menggunakan Priority Queue

# Buka User Interface Program
print("===== Aplikasi Antrian Bank =====")

while True:
    # Masukkan user
    print("Pilih jenis user : ")
    print("1. Nasabah Bank")
    print("2. Pegawai Bank")
    print("3. Keluar")
    user = int(input())

    if user == 1:
        while True:
            print()
            print("Pilih layanan : ")
            print("1. Customer Service")
            print("2. Teller")
            print("3. Cek Antrian")
            print("4. Cari Nama di Antrian")
            print("5. Kembali ke Menu")
            layanan = int(input())

            if layanan == 1:
                while True:
                    print()
                    print("Pilih keperluan : ")
                    print("1. " + keperluanCS_1)
                    print("2. " + keperluanCS_2)
                    print("3. " + keperluanCS_3)
                    print("4. " + keperluanCS_4)
                    print("5. Kembali")
                    keperluan = int(input())

                    if keperluan >= 1 and keperluan <= 4:
                        print()
                        namaNasabah = input("Masukkan nama Anda : ")
                        print("Apakah Anda memiliki kartu prioritas? (ya/tidak): ")
                        kartu_prioritas = input().strip().lower()

                        priority = PRIORITY_HIGH if kartu_prioritas == KARTU_PRIORITAS_YES else PRIORITY_LOW
                        
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d , %H:%M:%S")

                        if keperluan == 1:
                            queueAntrianCS.enqueue((namaNasabah, keperluanCS_1, timestamp), priority)
                        elif keperluan == 2:
                            queueAntrianCS.enqueue((namaNasabah, keperluanCS_2, timestamp), priority)
                        elif keperluan == 3:
                            queueAntrianCS.enqueue((namaNasabah, keperluanCS_3, timestamp), priority)
                        elif keperluan == 4:
                            queueAntrianCS.enqueue((namaNasabah, keperluanCS_4, timestamp), priority)

                        print()
                        print("== Customer Service ==")
                        print("Nomor antrian anda : ", queueAntrianCS.size())
                        print("Dengan keperluan : ", end="")
                        if keperluan == 1:
                            print(keperluanCS_1)
                        elif keperluan == 2:
                            print(keperluanCS_2)
                        elif keperluan == 3:
                            print(keperluanCS_3)
                        elif keperluan == 4:
                            print(keperluanCS_4)
                        break
                    elif keperluan == 5:
                        break
                    else:
                        print("Nomor tidak valid!")

            elif layanan == 2:
                while True:
                    print()
                    print("Pilih keperluan : ")
                    print("1. " + keperluanTeller_1)
                    print("2. " + keperluanTeller_2)
                    print("3. " + keperluanTeller_3)
                    print("4. Kembali")

                    keperluan = int(input())

                    if keperluan >= 1 and keperluan <= 3:
                        print()
                        namaNasabah = input("Masukkan nama Anda : ")
                        print("Apakah Anda memiliki kartu prioritas? (ya/tidak): ")
                        kartu_prioritas = input().strip().lower()

                        priority = PRIORITY_HIGH if kartu_prioritas == KARTU_PRIORITAS_YES else PRIORITY_LOW
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d , %H:%M:%S")

                        if keperluan == 1:
                            queueAntrianTeller.enqueue((namaNasabah, keperluanTeller_1, timestamp), priority)
                        elif keperluan == 2:
                            queueAntrianTeller.enqueue((namaNasabah, keperluanTeller_2, timestamp), priority)
                        elif keperluan == 3:
                            queueAntrianTeller.enqueue((namaNasabah, keperluanTeller_3, timestamp), priority)

                        print("== Teller ==")
                        print("Nomor antrian anda : ", queueAntrianTeller.size())
                        print("Dengan keperluan : ", end="")
                        if keperluan == 1:
                            print(keperluanTeller_1)
                        elif keperluan == 2:
                            print(keperluanTeller_2)
                        elif keperluan == 3:
                            print(keperluanTeller_3)
                        break
                    elif keperluan == 4:
                        break
                    else:
                        print("Nomor tidak valid!")
        
            elif layanan == 3:
                print()
                print("===== ANTRIAN CUSTOMER SERVICE =====")
                queueAntrianCS.queue_view()
                print("=====      ANTRIAN TELLER      =====")
                queueAntrianTeller.queue_view()
            
            elif layanan == 4:
                print()
                print("Masukkan nama nasabah yang ingin dicari: ")
                nama_cari = input().strip()
                
                print("===== HASIL PENCARIAN CUSTOMER SERVICE =====")
                hasil_cs = queueAntrianCS.search_by_name(nama_cari)
                if hasil_cs:
                    for result in hasil_cs:
                        print(f"{result[0]}. {result[1]} - {result[2]} (Priority: {result[3]}) at {result[4]}")
                else:
                    print("Nama tidak ditemukan di antrian Customer Service.")

                print("===== HASIL PENCARIAN TELLER =====")
                hasil_teller = queueAntrianTeller.search_by_name(nama_cari)
                if hasil_teller:
                    for result in hasil_teller:
                        print(f"{result[0]}. {result[1]} - {result[2]} (Priority: {result[3]}) at {result[4]}")
                else:
                    print("Nama tidak ditemukan di antrian Teller.")
                    
            elif layanan == 5:
                break
            else:
                print("Nomor tidak valid!")
                
    elif user == 2:
        while True:
            print()
            print("===== ANTRIAN CUSTOMER SERVICE =====")
            queueAntrianCS.queue_view()
            print("=====      ANTRIAN TELLER      =====")
            queueAntrianTeller.queue_view()

            print()
            print("Pilh jenis pegawai : ")
            print("1. Customer Service")
            print("2. Teller")
            print("3. Kembali ke Menu Utama")

            jenisPegawai = int(input())

            if jenisPegawai == 1:
                while True:
                    print()
                    print("Pilih jenis pengerjaan : ")
                    print("1. Layani")
                    print("2. Hapus")
                    print("3. Kembali ke menu pegawai")

                    pengerjaan = int(input())

                    if pengerjaan == 1:
                        if queueAntrianCS.is_empty():
                            print("Antrian Customer Service kosong.")
                        else:
                            dilayani = queueAntrianCS.dequeue()
                            print(f"Nasabah {dilayani[0]} dengan keperluan {dilayani[1]} telah dilayani.")
                            print("===== ANTRIAN CUSTOMER SERVICE =====")
                            queueAntrianCS.queue_view()
                        
                    elif pengerjaan == 2:
                        if queueAntrianCS.is_empty():
                            print("Antrian Customer Service kosong.")
                        else:
                            dihapus = queueAntrianCS.dequeue()
                            print(f"Nasabah {dihapus[0]} dengan keperluan {dihapus[1]} telah dihapus dari antrian.")
                            print("===== ANTRIAN CUSTOMER SERVICE =====")
                            queueAntrianCS.queue_view()
                    
            elif jenisPegawai == 2:
                while True:
                    print()
                    print("Pilih jenis pengerjaan : ")
                    print("1. Layani")
                    print("2. Hapus")
                    print("3. Kembali ke menu pegawai")

                    pengerjaan = int(input())

                    if pengerjaan == 1:
                        if queueAntrianTeller.is_empty():
                            print("Antrian Teller kosong.")
                        else:
                            dilayani = queueAntrianTeller.dequeue()
                            print(f"Nasabah {dilayani[0]} dengan keperluan {dilayani[1]} telah dilayani.")
                            print("=====      ANTRIAN TELLER      =====")
                            queueAntrianTeller.queue_view()
                    elif pengerjaan == 2:
                        if queueAntrianTeller.is_empty():
                            print("Antrian Teller kosong.")
                        else:
                            dihapus = queueAntrianTeller.dequeue()
                            print(f"Nasabah {dihapus[0]} dengan keperluan {dihapus[1]} telah dihapus dari antrian.")
                            print("=====      ANTRIAN TELLER      =====")
                            queueAntrianTeller.queue_view()
            
            elif jenisPegawai == 3:
                break
            else:
                print("Nomor tidak valid!")
                
    if user == 3:
        break
    else:
        print("Nomor tidak valid!")
