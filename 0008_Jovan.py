import re


gudang = {}


def tambahBarang():

    while True:
        menuTambahBarang()

        pilihan = inputAngka("Pilih sub menu (1-2): ")

        if pilihan == 1:
            tambahBarangProses()

        elif pilihan == 2:
            break

        else:
            print("Pilihan tidak valid!")


def tambahBarangProses():
    kode = input("Masukkan kode barang: ").upper()

    if not re.match(r'^[A-Z]-\d{3,}$', kode):
        print("Format kode tidak valid! Contoh: A-001 atau B-123")
        return

    if kode in gudang:
        print("Kode barang sudah ada!")
        return

    nama = input("Masukkan nama barang: ").strip()

    while True:
        if nama == "":
            print("Nama barang tidak boleh kosong!")
            nama = input("Masukkan nama barang: ").strip()
        else:
            break

    jumlah = inputAngka("Masukkan jumlah barang: ")

    while True:
        if jumlah < 0:
            print("Jumlah barang tidak boleh negatif!")
            jumlah = inputAngka("Masukkan jumlah barang: ")
        else:
            break

    while True:
        print("\nApakah Data Akan Disimpan?")
        print("1. Ya")
        print("2. Tidak")
        pilihan = inputAngka("Pilih (1-2): ")
        if pilihan == 1:
            break
        elif pilihan == 2:
            print("Penambahan barang dibatalkan.")
            return
        else:
            print("Pilihan tidak valid!")

    gudang[kode] = {"nama": nama, "jumlah": jumlah}
    print("Barang dengan kode", kode, "berhasil ditambahkan!")


def lihatBarang():

    while True:
        menuLihatBarang()

        pilihan = inputAngka("Pilih sub menu (1-3): ")

        if pilihan == 1:
            lihatSemuaBarang()

        elif pilihan == 2:
            lihatDetailBarang()

        elif pilihan == 3:
            break

        else:
            print("Pilihan tidak valid!")


def lihatSemuaBarang():
    if not gudang:
        print("Tidak ada barang di gudang!")
        return

    print("\nDaftar Barang di Gudang:")
    for kode, info in gudang.items():
        print("Kode:", kode, "| Nama:",
              info["nama"], "| Jumlah:", info["jumlah"])


def lihatDetailBarang():

    if not gudang:
        print("Tidak ada barang di gudang!")
        return

    print("\nDaftar Barang di Gudang:")
    for kode, info in gudang.items():
        print("Kode:", kode, "| Nama:",
              info["nama"], "| Jumlah:", info["jumlah"])

    kode = input("Masukkan kode barang yang ingin dilihat: ").upper()

    if kode not in gudang:
        print("Kode barang tidak ditemukan!")
        return

    info = gudang[kode]
    print("\nDetail Barang:")
    print("Kode:", kode)
    print("Nama:", info["nama"])
    print("Jumlah:", info["jumlah"])


def updateBarang():

    while True:
        menuUpdateBarang()

        pilihan = inputAngka("Pilih sub menu (1-2): ")

        if pilihan == 1:
            updateBarangProses()

        elif pilihan == 2:
            break

        else:
            print("Pilihan tidak valid!")


def updateBarangProses():
    lihatSemuaBarang()

    if not gudang:
        print("Tidak ada barang di gudang!")
        return
    
    kode = input("Masukkan kode barang yang ingin diupdate: ").upper()

    if kode not in gudang:
        print("Kode barang tidak ditemukan!")
        return

    namaBaru = input("Masukkan nama barang baru: ").strip()
    while True:
        if namaBaru == "":
            print("Nama barang tidak boleh kosong!")
            namaBaru = input("Masukkan nama barang baru: ").strip()
        else:
            break

    jumlahBaru = inputAngka("Masukkan jumlah barang baru: ")
    while True:
        if jumlahBaru < 0:
            print("Jumlah barang tidak boleh negatif!")
            jumlahBaru = inputAngka("Masukkan jumlah barang baru: ")
        else:
            break

    if (
        namaBaru == gudang[kode]["nama"]
        and jumlahBaru == gudang[kode]["jumlah"]
    ):
        print("Tidak ada perubahan data!")
        return

    gudang[kode] = {"nama": namaBaru, "jumlah": jumlahBaru}
    print("Barang dengan kode", kode, "berhasil diupdate!")


def hapusBarangProses():
    lihatSemuaBarang()
    kode = input("Masukkan kode barang yang ingin dihapus: ").upper()

    if kode not in gudang:
        print("Kode barang tidak ditemukan!")
        return

    while True:
        print("\nApakah Data Akan Dihapus?")
        print("1. Ya")
        print("2. Tidak")
        pilihan = inputAngka("Pilih (1-2): ")
        if pilihan == 1:
            break
        elif pilihan == 2:
            print("Penghapusan barang dibatalkan.")
            return
        else:
            print("Pilihan tidak valid!")

    del gudang[kode]
    print("Barang dengan kode", kode, "berhasil dihapus!")


def hapusBarang():
    menuHapusBarang()
    pilihan = inputAngka("Pilih sub menu (1-2): ")
    if pilihan == 1:
        hapusBarangProses()
    elif pilihan == 2:
        return
    else:
        print("Pilihan tidak valid!")


def menu():
    print("\n=== SISTEM GUDANG ===")
    print("1. Tambah Barang")
    print("2. Lihat Barang")
    print("3. Update Barang")
    print("4. Hapus Barang")
    print("5. Keluar")


def menuLihatBarang():
    print("\n=== Silahkan Pilih Sub Menu Lihat Barang ===")
    print("1. Lihat Barang")
    print("2. Lihat Barang Detail")
    print("3. Kembali ke Menu Utama")


def menuTambahBarang():
    print("\n=== Tambah Barang ===")
    print("Format kode: A-001, B-123, dst.")
    print("Kode harus diawali huruf kapital, diikuti tanda '-' dan angka minimal 3 digit.")
    print("1. Tambah Barang")
    print("2. Kembali ke Menu Utama")


def menuUpdateBarang():
    print("\n=== Update Barang ===")
    print("1. Update Barang")
    print("2. Kembali ke Menu Utama")


def menuHapusBarang():
    print("\n=== Hapus Barang ===")
    print("1. Hapus Barang")
    print("2. Kembali ke Menu Utama")


def inputAngka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input harus berupa angka!")


while True:
    menu()

    pilihan = inputAngka("Pilih menu (1-5): ")

    if pilihan == 1:
        tambahBarang()

    elif pilihan == 2:
        lihatBarang()

    elif pilihan == 3:
        updateBarang()

    elif pilihan == 4:
        hapusBarang()

    elif pilihan == 5:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
