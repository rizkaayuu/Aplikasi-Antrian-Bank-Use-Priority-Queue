import heapq
import streamlit as st
from datetime import datetime
import base64

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
        if self.is_empty():
            print("Antrian kosong")
        else:
            sorted_items = sorted(self.items, key=lambda x: (x[0], x[1], x[2]))
            for i, (priority, timestamp, counter, (nama_nasabah, keperluan, time_of_enqueue)) in enumerate(sorted_items, start=1):
                st.write(f"{i}. {nama_nasabah} - {keperluan} (Priority: {priority}) at {time_of_enqueue}")

    def size(self):
        return len(self.items)
    
    def search_by_name(self, name):
        results = []
        for i, (priority, timestamp, counter, (nama_nasabah, keperluan, waktu)) in enumerate (self.items):
            if name.lower() in nama_nasabah.lower():
                results.append((i + 1, nama_nasabah, keperluan, waktu))
        return results

# Inisialisasi state untuk antrian
if 'queueAntrianCS' not in st.session_state:
    st.session_state.queueAntrianCS = PriorityQueue()

if 'queueAntrianTeller' not in st.session_state:
    st.session_state.queueAntrianTeller = PriorityQueue()

# Inisialisasi state untuk input nama
if 'namaNasabahCS' not in st.session_state:
    st.session_state.namaNasabahCS = ""

if 'namaNasabahTeller' not in st.session_state:
    st.session_state.namaNasabahTeller = ""

# Deklarasi pelayanan di Customer Service
keperluanCS_1 = "Pembukaan rekening bank"
keperluanCS_2 = "Pelayanan masalah pada rekening nasabah"
keperluanCS_3 = "Informasi saldo dan mutasi nasabah"
keperluanCS_4 = "Administrasi buku cek dan buku tabungan"

# Deklarasi pelayanan di Teller
keperluanTeller_1 = "Penyetoran tabungan dan deposito"
keperluanTeller_2 = "Pencatatan tabungan dan deposito"
keperluanTeller_3 = "Pencatatan transaksi buku tabungan"

# Constants
PRIORITY_HIGH = 0
PRIORITY_LOW = 1

KARTU_PRIORITAS_YES = 'ya'
KARTU_PRIORITAS_NO = 'tidak'


# Fungsi untuk memuat gambar dari file dan mengubahnya menjadi base64
def load_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Jalur relatif ke gambar latar belakang
background_image_path = "background.png"
background_image_base64 = load_image_as_base64(background_image_path)

# CSS untuk menambahkan gambar latar belakang
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{background_image_base64});
            background-size: cover;
        }}
        .content {{
            padding: 20px;
            text-align: center;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='content'>", unsafe_allow_html=True)

# Buka User Interface Program
st.markdown("<h1 style='text-align: center;'>💸Aplikasi Antrian Bank💸</h1>", unsafe_allow_html=True)

user = st.selectbox("Pilih jenis user", ["Nasabah Bank", "Pegawai Bank", "Keluar"])

if user  == "Nasabah Bank":
    layanan = st.selectbox("Pilih layanan", ["Customer Service", "Teller", "Cek Antrian", "Cari Nama di Antrian", "Kembali ke Menu"])
    
    if layanan == "Customer Service":
        keperluan = st.selectbox("Pilih keperluan", [keperluanCS_1, keperluanCS_2, keperluanCS_3, keperluanCS_4])
    
        if keperluan:
            st.session_state.namaNasabahCS = st.text_input("Masukkan nama Anda :", st.session_state.namaNasabahCS)
            kartu_prioritas = st.radio("Apakah Anda memiliki kartu prioritas?", [KARTU_PRIORITAS_YES, KARTU_PRIORITAS_NO], key='kartu_prioritas')

            priority = PRIORITY_HIGH if kartu_prioritas == KARTU_PRIORITAS_YES else PRIORITY_LOW

            if st.button("Submit"):
                waktu = datetime.now().strftime("%Y-%m-%d")
                st.session_state.queueAntrianCS.enqueue((st.session_state.namaNasabahCS, keperluan, waktu), priority)
                st.write("== Customer Service ==")
                st.write("Nomor antrian anda : ", st.session_state.queueAntrianCS.size())
                st.write("Dengan keperluan : ", keperluan)
                st.write("Waktu : ", waktu)
                
                # Hapus input nama setelah submit
                st.session_state.namaNasabahCS = ""
                

    elif layanan == "Teller":
        keperluan = st.selectbox("Pilih keperluan", [keperluanTeller_1, keperluanTeller_2, keperluanTeller_3])
    
        if keperluan:
            st.session_state.namaNasabahTeller = st.text_input("Masukkan nama Anda :", st.session_state.namaNasabahTeller)
            kartu_prioritas = st.radio("Apakah Anda memiliki kartu prioritas?", [KARTU_PRIORITAS_YES, KARTU_PRIORITAS_NO], key='kartu_prioritas')

            priority = PRIORITY_HIGH if kartu_prioritas == KARTU_PRIORITAS_YES else PRIORITY_LOW

            if st.button("Submit"):
                waktu = datetime.now().strftime("%Y-%m-%d")
                st.session_state.queueAntrianTeller.enqueue((st.session_state.namaNasabahTeller, keperluan, waktu), priority)
                st.write("== Teller ==")
                st.write("Nomor antrian anda : ", st.session_state.queueAntrianTeller.size())
                st.write("Dengan keperluan : ", keperluan)
                st.write("Waktu : ", waktu)
                
                # Hapus input nama setelah submit
                st.session_state.namaNasabahTeller = ""



    elif layanan == "Cek Antrian":
        st.write("===== ANTRIAN CUSTOMER SERVICE =====")
        st.session_state.queueAntrianCS.queue_view()
        st.write("===== ANTRIAN TELLER =====")
        st.session_state.queueAntrianTeller.queue_view()

    elif layanan == "Cari Nama di Antrian":
        nama_cari = st.text_input("Masukkan nama nasabah yang ingin dicari:")
        
        if nama_cari :
            if st.button("Cari"):
                hasil_cari_cs = st.session_state.queueAntrianCS.search_by_name(nama_cari)
                hasil_cari_teller = st.session_state.queueAntrianTeller.search_by_name(nama_cari)

                st.write("===== ANTRIAN CUSTOMER SERVICE =====")
                if hasil_cari_cs:
                    for nama, keperluan, priority, waktu in hasil_cari_cs:
                        st.write(f"{nama} - {keperluan} (Waktu: {waktu})")
                else:
                    st.write("Nama tidak ditemukan di antrian Customer Service.")

                st.write("===== ANTRIAN TELLER =====")
                if hasil_cari_teller:
                    for nama, keperluan, priority, waktu in hasil_cari_teller:
                        st.write(f"{nama} - {keperluan} (Waktu: {waktu})")
                else:
                    st.write("Nama tidak ditemukan di antrian Teller.")
        else:
            st.write("Silakan masukkan nama nasabah terlebih dahulu.")
            
elif user == "Pegawai Bank":
    st.write("===== ANTRIAN CUSTOMER SERVICE =====")
    st.session_state.queueAntrianCS.queue_view()
    st.write("===== ANTRIAN TELLER =====")
    st.session_state.queueAntrianTeller.queue_view()

    jenisPegawai = st.selectbox("Pilih jenis pegawai", ["Customer Service", "Teller"])

    if jenisPegawai == "Customer Service":
        pengerjaan = st.selectbox("Pilih jenis pengerjaan", ["Layani", "Hapus"])

        if pengerjaan == "Layani" and not st.session_state.queueAntrianCS.is_empty():
            st.session_state.queueAntrianCS.dequeue()
            st.write("===== ANTRIAN CUSTOMER SERVICE =====")
            st.session_state.queueAntrianCS.queue_view()

        elif pengerjaan == "Hapus" and not st.session_state.queueAntrianCS.is_empty():
            st.session_state.queueAntrianCS.dequeue()
            st.write("===== ANTRIAN CUSTOMER SERVICE =====")
            st.session_state.queueAntrianCS.queue_view()

    elif jenisPegawai == "Teller":
        pengerjaan = st.selectbox("Pilih jenis pengerjaan", ["Layani", "Hapus"])

        if pengerjaan == "Layani" and not st.session_state.queueAntrianTeller.is_empty():
            st.session_state.queueAntrianTeller.dequeue()
            st.write("===== ANTRIAN TELLER =====")
            st.session_state.queueAntrianTeller.queue_view()

        elif pengerjaan == "Hapus" and not st.session_state.queueAntrianTeller.is_empty():
            st.session_state.queueAntrianTeller.dequeue()
            st.write("===== ANTRIAN TELLER =====")
            st.session_state.queueAntrianTeller.queue_view()

elif user == "Keluar":
    st.write("Terima kasih telah menggunakan aplikasi antrian bank!")
    
    
