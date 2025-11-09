import json
import os
from datetime import datetime

# Lokasi file JSON penyimpanan progres
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROGRESS_FILE = os.path.join(BASE_DIR, "sahabat_sehat/progress.json")

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
    """Menampilkan progres mingguan dengan grafik bar sederhana"""
    data = load_progress()
    if not data:
        print("\n⚠️ Belum ada data progres untuk ditampilkan.")
        return

    print("\n=== 📈 Grafik Progres Mingguan ===")
    for tanggal, nilai in data.items():
        langkah_bar = "█" * (nilai['langkah'] // 500)
        air_bar = "█" * int(nilai['air'] * 2)
        kalori_bar = "█" * (nilai['kalori'] // 100)

        print(f"\n📅 {tanggal}")
        print(f"🏃 Langkah: {langkah_bar}")
        print(f"💧 Air: {air_bar}")
        print(f"🔥 Kalori: {kalori_bar}")

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
