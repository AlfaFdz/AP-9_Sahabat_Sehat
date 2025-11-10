FILE_NAME = 'riwayat.txt'

def show_history():
    print("\n=== Daftar History BMI ===")
    try:
        f = open(FILE_NAME)
        lines = f.readlines()
        f.close()
    except:
        print("Belum ada data.")
        return

    if not lines:
        print("File kosong.")
        return

    print("-" * 40)
    print("{:<10} {:<10} {:<10}".format("ID", "BMI", "Kategori"))
    print("-" * 40)
    for l in lines:
        data = l.strip().split('|')
        if len(data) == 3:
            print("{:<10} {:<10} {:<10}".format(data[0], data[1], data[2]))
    print("-" * 40)

def delete_history():
    print("\n=== Hapus Data History ===")
    try:
        f = open(FILE_NAME)
        lines = f.readlines()
        f.close()
    except:
        print("Belum ada data.")
        return

    if not lines:
        print("File kosong.")
        return

    show_history()
    target_id = input("Masukkan ID yang ingin dihapus: ").strip()
    if not target_id:
        print("ID tidak boleh kosong.")
        return

    baru = []
    ditemukan = False
    for l in lines:
        if not l.startswith(target_id + "|"):
            baru.append(l)
        else:
            ditemukan = True

    if not ditemukan:
        print("ID tidak ditemukan.")
        return

    try:
        f = open(FILE_NAME, 'w')
        f.writelines(baru)
        f.close()
        print("Data berhasil dihapus.")
    except:
        print("Gagal menghapus data.")
