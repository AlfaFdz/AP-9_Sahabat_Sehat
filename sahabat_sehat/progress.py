import json
import os
from datetime import datetime

# Lokasi file JSON penyimpanan progres
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)
PROGRESS_FILE = os.path.join(DATA_DIR, "progress.json")

# ====== UTILITAS DASAR ======
def load_progress():
    """Memuat data progres dari file JSON"""
    if not os.path.exists(PROGRESS_FILE):
        return {}
    try:
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Peringatan: File progress.json rusak. Membuat file baru.")
        return {}

def save_progress(data):
    """Menyimpan data progres ke file JSON"""
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- FUNGSI INPUT BANTU ---
def get_validated_input(prompt, target_type, default_value):
    """Fungsi helper untuk validasi input saat update/edit."""
    while True:
        user_input = input(prompt)
        if not user_input:
            # Pengguna menekan Enter (melewatkan)
            return default_value
        try:
            # Mencoba konversi ke tipe yang diinginkan (int atau float)
            return target_type(user_input)
        except ValueError:
            print(f"Input tidak valid. Harap masukkan angka {target_type.__name__}.")

# ====== FITUR UTAMA (IDE 1, 2, 3) ======

# --- (IDE 1: Tambah / Update) ---
def tambah_atau_update_progres():
    """Menambahkan atau memperbarui progres harian pengguna"""
    data = load_progress()
    tanggal = datetime.now().strftime("%Y-%m-%d")

    # Ambil data hari ini jika ada, atau buat data baru
    progress_hari_ini = data.get(tanggal, {
        "langkah": 0, "air": 0.0, "kalori": 0, "berat": 0.0
    })

    print(f"\n=== ✏️ Tambah/Update Progres Harian ({tanggal}) ===")
    print("Tekan Enter untuk melewati jika tidak ada perubahan.")

    try:
        # Gunakan fungsi helper untuk input yang lebih bersih
        langkah_baru = get_validated_input(
            f"Masukkan jumlah langkah (sebelumnya: {progress_hari_ini['langkah']}): ",
            int, progress_hari_ini['langkah']
        )
        air_baru = get_validated_input(
            f"Masukkan jumlah air (L) (sebelumnya: {progress_hari_ini['air']}): ",
            float, progress_hari_ini['air']
        )
        kalori_baru = get_validated_input(
            f"Masukkan total kalori hari ini (sebelumnya: {progress_hari_ini['kalori']}): ",
            int, progress_hari_ini['kalori']
        )
        berat_baru = get_validated_input(
            f"Masukkan berat badan (kg) (sebelumnya: {progress_hari_ini['berat']}): ",
            float, progress_hari_ini['berat']
        )
        
        # Update dictionary
        progress_hari_ini = {
            "langkah": langkah_baru,
            "air": air_baru,
            "kalori": kalori_baru,
            "berat": berat_baru
        }

        data[tanggal] = progress_hari_ini
        save_progress(data)
        print(f"\n✅ Progres untuk {tanggal} berhasil di-update!")

    except ValueError:
        print("⚠️ Input tidak valid. Progres tidak disimpan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# --- (FITUR ASLI: Lihat Progres) ---
# --- (FITUR ASLI: Lihat Progres) ---
def lihat_progres():
    """Menampilkan seluruh data progres DENGAN PAGINATION"""
    data = load_progress()
    if not data:
        print("\n⚠️ Belum ada data progres tersimpan.")
        return

    print("\n=== 📊 Progres Harian (Per Halaman) ===")
    
    sorted_keys = sorted(data.keys())
    
    # Tentukan berapa banyak data yang ingin ditampilkan per "halaman"
    PAGE_SIZE = 5 
    
    if not sorted_keys:
        print("Data kosong.")
        return

    for i, tanggal in enumerate(sorted_keys):
        nilai = data[tanggal]
        print(f"\n📅 {tanggal}")
        print(f"  🏃 Langkah: {nilai.get('langkah', 0)}")
        print(f"  💧 Air: {nilai.get('air', 0)} L")
        print(f"  🔥 Kalori: {nilai.get('kalori', 0)}")
        print(f"  ⚖️ Berat: {nilai.get('berat', 0)} kg")

        # Cek apakah kita berada di akhir halaman
        # (i + 1) adalah jumlah item yang sudah ditampilkan (misal: 1, 2, 3, 4, 5)
        is_page_end = (i + 1) % PAGE_SIZE == 0
        
        # Cek apakah ini BUKAN item terakhir di seluruh daftar
        is_not_last_item = (i + 1) < len(sorted_keys)

        # Jika ini adalah akhir halaman DAN bukan item terakhir, jeda program
        if is_page_end and is_not_last_item:
            try:
                # Menunggu input pengguna
                ans = input(f"\n--- Menampilkan {i + 1} dari {len(sorted_keys)} data. Tekan Enter untuk lanjut, atau 'q' untuk berhenti: --- ")
                if ans.lower().strip() == 'q':
                    print("Menghentikan tampilan progres.")
                    break # Keluar dari loop for
            except EOFError:
                break # Keluar jika pengguna menekan Ctrl+D
    
    print("\n--- Akhir dari data progres ---")

    print("\n=== 📊 Progres Harian ===")
    # Mengurutkan berdasarkan tanggal
    for tanggal in sorted(data.keys()):
        nilai = data[tanggal]
        print(f"\n📅 {tanggal}")
        print(f"  🏃 Langkah: {nilai.get('langkah', 0)}")
        print(f"  💧 Air: {nilai.get('air', 0)} L")
        print(f"  🔥 Kalori: {nilai.get('kalori', 0)}")
        print(f"  ⚖️ Berat: {nilai.get('berat', 0)} kg")

# --- (FITUR ASLI: Grafik Mingguan) ---
# --- (FITUR ASLI: Grafik Mingguan) ---
def grafik_mingguan():
    print("\n" + "="*60)
    print("📊  GRAFIK PROGRES MINGGUAN (vs. Target)".center(60))
    print("="*60)

    data = load_progress()
    if not data:
        print("❌ Belum ada data progres yang bisa ditampilkan.")
        return

    # --- (PERUBAHAN UTAMA DIMULAI DI SINI) ---
    print("Silakan masukkan target harian Anda untuk skala grafik.")
    print("Tekan Enter untuk menggunakan nilai default.")
    
    try:
        target_langkah_str = input(f"Target Langkah (default: 10000): ")
        target_langkah = int(target_langkah_str) if target_langkah_str else 10000
        
        target_air_str = input(f"Target Air (L) (default: 2.5): ")
        target_air = float(target_air_str) if target_air_str else 2.5
        
        target_kalori_str = input(f"Target Kalori (Kkal) (default: 2000): ")
        target_kalori = int(target_kalori_str) if target_kalori_str else 2000
        
        if target_langkah <= 0 or target_air <= 0 or target_kalori <= 0:
            print("Target harus bernilai positif.")
            return

    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return
    # --- (PERUBAHAN UTAMA SELESAI) ---


    # Mengurutkan data berdasarkan tanggal
    sorted_items = sorted(data.items())
    
    # Ambil maksimal 7 hari terakhir
    last_week_items = sorted_items[-7:]

    if len(last_week_items) < 7:
        print(f"\n🌱 Data kamu baru {len(last_week_items)} hari, grafik ditampilkan berdasarkan data yang ada.\n")
    else:
        print(f"\nMenampilkan {len(last_week_items)} hari terakhir:\n")

    # Header tabel
    print(f"{'📅 Tanggal':<12} | {'Langkah (bar)':<25} | {'Air (bar)':<15} | {'Kalori (bar)':<20}")
    print("-"*80)

    for tgl, d in last_week_items:
        langkah_hari_ini = d.get('langkah', 0)
        air_hari_ini = d.get('air', 0)
        kalori_hari_ini = d.get('kalori', 0)

        # Hitung persentase progres berdasarkan TARGET
        # (jika progres melebihi target, batasi di 100% (skala 20) agar rapi)
        skala_langkah = min(int((langkah_hari_ini / target_langkah) * 20), 20)
        skala_air = min(int((air_hari_ini / target_air) * 10), 10)
        skala_kalori = min(int((kalori_hari_ini / target_kalori) * 15), 15)

        langkah_bar = "█" * skala_langkah
        air_bar = "▒" * skala_air
        kalori_bar = "▓" * skala_kalori
        
        # Tambahan: Tampilkan nilai aktual di sebelah bar
        print(f"{tgl:<12} | {langkah_bar:<25} ({langkah_hari_ini})")
        print(f"{'':<12} | {'':<25} | {air_bar:<15} ({air_hari_ini} L)")
        print(f"{'':<12} | {'':<25} | {'':<15} | {kalori_bar:<20} ({kalori_hari_ini} Kkal)")
        print("-" * 80)


    print("Legenda:")
    print(f"█ = Langkah (Target: {target_langkah})  ▒ = Air (Target: {target_air} L)  ▓ = Kalori (Target: {target_kalori} Kkal)")
    print("="*60 + "\n")

# --- (IDE 2: Fitur Edit) ---
def edit_progres():
    """Mengedit progres untuk tanggal tertentu."""
    data = load_progress()
    tanggal_edit = input("Masukkan tanggal yang ingin di-edit (YYYY-MM-DD): ").strip()

    if tanggal_edit not in data:
        print(f"⚠️ Data untuk tanggal {tanggal_edit} tidak ditemukan.")
        return

    progress_edit = data[tanggal_edit]
    
    print(f"\n=== ✏️ Mengedit Progres ({tanggal_edit}) ===")
    print("Tekan Enter untuk melewati jika tidak ada perubahan.")

    try:
        langkah_baru = get_validated_input(
            f"Masukkan jumlah langkah (sebelumnya: {progress_edit['langkah']}): ",
            int, progress_edit['langkah']
        )
        air_baru = get_validated_input(
            f"Masukkan jumlah air (L) (sebelumnya: {progress_edit['air']}): ",
            float, progress_edit['air']
        )
        kalori_baru = get_validated_input(
            f"Masukkan total kalori (sebelumnya: {progress_edit['kalori']}): ",
            int, progress_edit['kalori']
        )
        berat_baru = get_validated_input(
            f"Masukkan berat badan (kg) (sebelumnya: {progress_edit['berat']}): ",
            float, progress_edit['berat']
        )
        
        # Update dictionary
        data[tanggal_edit] = {
            "langkah": langkah_baru,
            "air": air_baru,
            "kalori": kalori_baru,
            "berat": berat_baru
        }

        save_progress(data)
        print(f"\n✅ Progres untuk {tanggal_edit} berhasil di-edit!")

    except ValueError:
        print("⚠️ Input tidak valid. Perubahan dibatalkan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# --- (IDE 2: Fitur Hapus per Tanggal) ---
def hapus_progres_tanggal():
    """Menghapus data progres untuk tanggal tertentu."""
    data = load_progress()
    tanggal_hapus = input("Masukkan tanggal yang ingin dihapus (YYYY-MM-DD): ").strip()

    if tanggal_hapus not in data:
        print(f"⚠️ Data untuk tanggal {tanggal_hapus} tidak ditemukan.")
        return

    # Tampilkan data yang akan dihapus untuk konfirmasi
    print("\nData yang akan dihapus:")
    nilai = data[tanggal_hapus]
    print(f"  🏃 Langkah: {nilai.get('langkah', 0)}")
    print(f"  💧 Air: {nilai.get('air', 0)} L")
    print(f"  🔥 Kalori: {nilai.get('kalori', 0)}")
    print(f"  ⚖️ Berat: {nilai.get('berat', 0)} kg")
    
    konfirmasi = input(f"Apakah kamu yakin ingin menghapus data untuk {tanggal_hapus}? (y/n): ")
    if konfirmasi.lower() == "y":
        del data[tanggal_hapus]
        save_progress(data)
        print(f"✅ Data untuk {tanggal_hapus} berhasil dihapus!\n")
    else:
        print("❎ Aksi dibatalkan.\n")

# --- (IDE 3: Fitur Statistik) ---
def lihat_statistik():
    """Menampilkan ringkasan statistik dari data progres."""
    data = load_progress()
    if not data:
        print("\n⚠️ Belum ada data progres untuk dianalisis.")
        return

    print("\n" + "="*60)
    print("📈  RINGKASAN STATISTIK".center(60))
    print("="*60)

    # Mengurutkan data berdasarkan tanggal
    sorted_data = dict(sorted(data.items()))
    sorted_keys = list(sorted_data.keys())

    # --- 1. Analisis Berat Badan ---
    print("\n⚖️ Analisis Berat Badan:")
    # Ambil semua data berat yang valid (bukan 0)
    berat_entries = [(t, d['berat']) for t, d in sorted_data.items() if d.get('berat', 0) > 0]
    
    if len(berat_entries) >= 2:
        tanggal_awal, berat_awal = berat_entries[0]
        tanggal_akhir, berat_akhir = berat_entries[-1]
        perubahan = berat_akhir - berat_awal
        
        print(f"  ⚖️ Berat Awal: {berat_awal} kg (pada {tanggal_awal})")
        print(f"  ⚖️ Berat Akhir: {berat_akhir} kg (pada {tanggal_akhir})")
        print(f"  📈 Total Perubahan: {perubahan:+.2f} kg")
    elif len(berat_entries) == 1:
        print(f"  ⚖️ Berat Terakhir: {berat_entries[0][1]} kg (pada {berat_entries[0][0]})")
        print("  (Data belum cukup untuk melihat perubahan berat badan)")
    else:
        print("  (Tidak ada data berat badan yang tercatat)")

    # --- 2. Rata-rata 7 Hari Terakhir ---
    print("\n📊 Rata-rata 7 Hari Terakhir:")
    last_7_keys = sorted_keys[-7:]
    n = len(last_7_keys)
    
    if n > 0:
        total_langkah = sum(sorted_data[k].get('langkah', 0) for k in last_7_keys)
        total_air = sum(sorted_data[k].get('air', 0) for k in last_7_keys)
        total_kalori = sum(sorted_data[k].get('kalori', 0) for k in last_7_keys)

        print(f"  🏃 Rata-rata Langkah: {total_langkah / n:.0f} / hari")
        print(f"  💧 Rata-rata Air: {total_air / n:.2f} L / hari")
        print(f"  🔥 Rata-rata Kalori: {total_kalori / n:.0f} Kkal / hari")
    else:
        print("  (Tidak ada data)")

    # --- 3. Rekor Tertinggi ---
    print("\n🏆 Rekor Tertinggi (Keseluruhan):")
    try:
        max_langkah_day = max(sorted_data, key=lambda k: sorted_data[k].get('langkah', 0))
        max_langkah = sorted_data[max_langkah_day].get('langkah', 0)
        if max_langkah > 0:
            print(f"  🏃 Langkah Terbanyak: {max_langkah} (pada {max_langkah_day})")
        else:
            print("  🏃 (Belum ada data langkah)")
            
        max_kalori_day = max(sorted_data, key=lambda k: sorted_data[k].get('kalori', 0))
        max_kalori = sorted_data[max_kalori_day].get('kalori', 0)
        if max_kalori > 0:
             print(f"  🔥 Kalori Terbanyak: {max_kalori} Kkal (pada {max_kalori_day})")
        else:
            print("  🔥 (Belum ada data kalori)")

    except Exception as e:
        print(f"  (Gagal menghitung rekor: {e})")
        
    print("="*60 + "\n")


# --- (FITUR ASLI: Reset) ---
def reset_progres():
    """Menghapus seluruh data progres"""
    konfirmasi = input("\n‼️ PERINGATAN: Aksi ini akan menghapus SEMUA data progres.\n"
                       "Apakah kamu yakin ingin melanjutkan? (y/n): ")
    if konfirmasi.lower() == "y":
        if os.path.exists(PROGRESS_FILE):
            os.remove(PROGRESS_FILE)
        print("✅ Semua data progres berhasil dihapus!\n")
    else:
        print("❎ Aksi dibatalkan.\n")

# ====== MENU UTAMA PROGRES (Diperbarui) ======
def menu_progres():
    """Menu utama fitur Progres Harian"""
    while True:
        print("\n=== 📅 Menu Progres Harian ===")
        print("1. Tambah/Update progres hari ini")
        print("2. Edit progres tanggal lain")
        print("3. Hapus progres per tanggal")
        print("4. Lihat progres lengkap")
        print("5. Lihat grafik mingguan")
        print("6. Lihat ringkasan statistik")
        print("7. Reset semua progres")
        print("8. Kembali")

        pilihan = input("Pilih menu (1-8): ")

        if pilihan == "1":
            tambah_atau_update_progres()
        elif pilihan == "2":
            edit_progres()
        elif pilihan == "3":
            hapus_progres_tanggal()
        elif pilihan == "4":
            lihat_progres()
        elif pilihan == "5":
            grafik_mingguan()
        elif pilihan == "6":
            lihat_statistik()
        elif pilihan == "7":
            reset_progres()
        elif pilihan == "8":
            break
        else:
            print("⚠️ Pilihan tidak valid.")