# tahap 1
#=====================================================================================
# inisialisasi & konfigurasi jendela utama (gui)
#=========== 1.MEMANGGIL PUSTAKA TKINTER
import tkinter as tk

#====== 2.MEMBUAT CUSTOM VARIABEL JENDELA UTAMA APLIKASI
layar_utama = tk.Tk()

#====== 3.MENGATUR ATRIBUT JENDELA UTAMA APLIKASI (judul,ukuran,dan warna background)
layar_utama.title("Calculator")
layar_utama.geometry("350x500")
layar_utama.configure(bg="#171717")
#=====================================================================================

# tahap 2
#=====================================================================================
# deklarasi variabel pemproses data
# membuat variabel data hitung sebagai memori penyimpan input string angka/operator
papan_hitung = ""
#=====================================================================================

# tahap 3
#=====================================================================================
# pembuatan fungsi logika (dummy/sementara)
# fungsi dikosongkan dengan 'pass' agar tombol yang akan dibuat bisa merujuk ke fungsi ini
#========= 1.fungsi dummy untuk tombol angka & operator
def tekan_tombol(num):
    global papan_hitung
    papan_hitung = papan_hitung + str(num)
    string_tampilan.set(papan_hitung)

#========= 2.fungsi dummy untuk tombol (=)
def hitung():
    global papan_hitung
    try:
        # mengganti karakter visual menjadi operator python sebelum dihitung
        total = str(eval(papan_hitung.replace('x', '*').replace('÷', '/').replace(',', '.')))
        string_tampilan.set(total)
        papan_hitung = total
    except: 
        string_tampilan.set("error")
        papan_hitung = ""

#========== 3.fungsi dummy untuk tombol reset (c)
def hapus_semua():
    global papan_hitung
    papan_hitung = ""
    string_tampilan.set("")
#===========================================================================================

# tahap 4
# ==========================================================================================
# PEMBUATAN LAYAR TAMPILAN ANGKA DAN OPERATOR
# ========= 1. membuat variabel Tkinter untuk sinkronisasi teks pada komponen Entry
string_tampilan = tk.StringVar()

# ========= 2. membuat komponen widget Entry untuk layar kalkulator 
layar = tk.Entry(
    layar_utama,
    textvariable=string_tampilan,
    font=("Helvetica", 36),
    bd=0,
    bg="#fafefa",
    fg="black",
    justify="right"
)
layar.pack(fill="both", ipadx=10, ipady=30, padx=10, pady=10)
#===========================================================================================

# tahap 5
#===========================================================================================
# PEMBUATAN DAN KONFIGURASI WIDGET FRAME TOMBOL
# ========= 1. membuat frame khusus sebagai tempat meletakan susunan tombol
frame_tombol = tk.Frame(layar_utama, bg="#f32434")
frame_tombol.pack(fill="both", expand=True, padx=10, pady=10)

# ========= 2. konfigursai grid layout agar ukuran tombol bisa membesar/mengecil secara proporsional
for i in range(5):
    frame_tombol.rowconfigure(i, weight=1)
for i in range(4):
    frame_tombol.columnconfigure(i, weight=1)
#==========================================================================================

# tahap 6
# ===============================================================================================
# DESAIN DATA & RENDERING TOMBOL (GRID SYSTEM)
# ========= 1.pemetaaan data konfigurasi tombol
# susunan data (teks, baris(row), warna bg, warna fg, fungsi/aksi)
tombol_config = [
('C', 0, 0, '#a5a5a5', 'black', hapus_semua),
('+/-', 0, 1, '#a5a5a5', 'black', lambda: tekan_tombol('-')),
('%', 0, 2, '#a5a5a5', 'black', lambda: tekan_tombol('/100')),
('÷', 0, 3, '#a5a5a5', 'black', lambda: tekan_tombol('÷')),

('1', 1, 0, '#333333', 'white', lambda: tekan_tombol('1')),
('2', 1, 1, '#333333', 'white', lambda: tekan_tombol('2')),
('3', 1, 2, '#333333', 'white', lambda: tekan_tombol('3')),
('x', 1, 3, '#333333', 'white', lambda: tekan_tombol('x')),

('4', 2, 0, '#333333', 'white', lambda: tekan_tombol('4')),
('5', 2, 1, '#333333', 'white', lambda: tekan_tombol('5')),
('6', 2, 2, '#333333', 'white', lambda: tekan_tombol('6')),
('-', 2, 3, '#333333', 'white', lambda: tekan_tombol('-')),

('7', 3, 0, '#333333', 'white', lambda: tekan_tombol('7')),
('8', 3, 1, '#333333', 'white', lambda: tekan_tombol('8')),
('9', 3, 2, '#333333', 'white', lambda: tekan_tombol('9')),
('+', 3, 3, '#333333', 'white', lambda: tekan_tombol('+')),

(',', 4, 2, '#333333', 'white', lambda: tekan_tombol(',')),
('=', 4, 3, '#ff9f0a', 'white', hitung)
]

#======= 2. membuat dan menampilkan tombol berdasarkan data di atas
for teks, r, c, bg_color, fg_color, aksi in tombol_config:
    btn = tk.Button(
      frame_tombol, text=teks, font=("Helvetica", 18, "bold"),
      bg=bg_color, fg=fg_color, bd=0, relief="flat", command=aksi
    )
    btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

    # penanganan khusus untuk tombol '0' agar berukuran lebih lebar (memaka 2 kolom grid)
    btn_nol = tk.Button(
    frame_tombol, text="0", font=("Helvetica", 18, "bold"),
    bg="#333333", fg="white", bd=0, relief="flat", command=aksi    
)
btn_nol.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
#==============================================================================================

# LOOPING
# didahulukan setelah 
    
    


layar_utama.mainloop()