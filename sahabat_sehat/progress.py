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
    with open(PROGRESS_FILE, "r") as f:
        return json.load(f)

def save_progress(data):
    """Menyimpan data progres ke file JSON"""
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ====== FITUR UTAMA ======
def tambah_progres():
    """Menambahkan progres harian pengguna"""
    data = load_progress()
    tanggal = datetime.now().strftime("%Y-%m-%d")

    print("\n=== ✏️ Tambah Progres Harian ===")
    langkah = input("Masukkan jumlah langkah: ")
    air = input("Masukkan jumlah air (liter): ")
    kalori = input("Masukkan total kalori hari ini: ")
    berat = input("Masukkan berat badan (kg): ")

    try:
        data[tanggal] = {
            "langkah": int(langkah),
            "air": float(air),
            "kalori": int(kalori),
            "berat": float(berat)
        }
    except ValueError:
        print("⚠️ Input tidak valid. Progres tidak disimpan.")
        return

    save_progress(data)
    print(f"✅ Progres untuk {tanggal} berhasil disimpan!\n")

def lihat_progres():
    """Menampilkan seluruh data progres"""
    data = load_progress()
    if not data:
        print("\n⚠️ Belum ada data progres tersimpan.")
        return

    print("\n=== 📊 Progres Harian ===")
    for tanggal, nilai in data.items():
        print(f"\n📅 {tanggal}")
        print(f"🏃 Langkah: {nilai['langkah']}")
        print(f"💧 Air: {nilai['air']} L")
        print(f"🔥 Kalori: {nilai['kalori']}")
        print(f"⚖️ Berat: {nilai['berat']} kg")

def grafik_mingguan():
    print("\n" + "="*60)
    print("📊  GRAFIK PROGRES MINGGUAN".center(60))
    print("="*60)

    data = load_progress()

    if not data:
        print("❌ Belum ada data progres yang bisa ditampilkan.")
        return
    
    if isinstance(data, dict):
        data = [{"tanggal": k, **v} for k, v in data.items()]

    # Ambil maksimal 7 hari terakhir
    last_week = data[-7:]

    if len(last_week) < 7:
        print(f"🌱 Data kamu baru {len(last_week)} hari, grafik ditampilkan berdasarkan data yang ada.\n")

    # Hitung nilai maksimum untuk skala grafik
    max_langkah = max([d.get("langkah", 0) for d in last_week]) or 1
    max_air = max([d.get("air", 0) for d in last_week]) or 1
    max_kalori = max([d.get("kalori", 0) for d in last_week]) or 1

    # Header tabel
    print(f"{'📅 Tanggal':<12} | {'Langkah (bar)':<25} | {'Air (bar)':<15} | {'Kalori (bar)':<20}")
    print("-"*80)

    # Isi tabel
    for d in last_week:
        tgl = d.get("tanggal", "????-??-??")
        langkah_bar = "█" * int((d["langkah"] / max_langkah) * 20)
        air_bar = "▒" * int((d["air"] / max_air) * 10)
        kalori_bar = "▓" * int((d["kalori"] / max_kalori) * 15)

        print(f"{tgl:<12} | {langkah_bar:<25} | {air_bar:<15} | {kalori_bar:<20}")

    print("-"*80)
    print("Legenda:")
    print("█ = Langkah  ▒ = Air (L)  ▓ = Kalori (Kcal)")
    print("="*60 + "\n")



def reset_progres():
    """Menghapus seluruh data progres"""
    konfirmasi = input("Apakah kamu yakin ingin menghapus semua data progres? (y/n): ")
    if konfirmasi.lower() == "y":
        if os.path.exists(PROGRESS_FILE):
            os.remove(PROGRESS_FILE)
        print("✅ Semua data progres berhasil dihapus!\n")
    else:
        print("❎ Aksi dibatalkan.\n")

# ====== MENU UTAMA PROGRES ======
def menu_progres():
    """Menu utama fitur Progres Harian"""
    while True:
        print("\n=== 📅 Menu Progres Harian ===")
        print("1. Tambah progres hari ini")
        print("2. Lihat progres lengkap")
        print("3. Lihat grafik mingguan")
        print("4. Reset progres")
        print("5. Kembali")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_progres()
        elif pilihan == "2":
            lihat_progres()
        elif pilihan == "3":
            grafik_mingguan()
        elif pilihan == "4":
            reset_progres()
        elif pilihan == "5":
            break
        else:
            print("⚠️ Pilihan tidak valid.")
