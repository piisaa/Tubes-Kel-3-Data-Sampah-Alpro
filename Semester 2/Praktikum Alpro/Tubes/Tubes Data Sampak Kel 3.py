# ===== PROGRAM PENGELOLAAN SAMPAH =====

jenis_sampah = []
jumlah_sampah = []

def Menu_utama():
    print("===== MENU UTAMA =====")
    print("1. Tambah Data Sampah")
    print("2. Lihat Data Sampah")
    print("3. Ubah Data Sampah")
    print("4. Hapus Data Sampah")
    print("5. Tambah Data Daur Ulang")
    print("6. Cari Data Sampah")
    print("7. Urutkan Data")
    print("8. Statistik Sampah & Daur Ulang")
    print("9. Keluar")

    pilihan = int(input("Masukkan pilihan menu : "))
    return pilihan


def Tambah_data_sampah():
    print("\n===== TAMBAH DATA SAMPAH =====")
    print("Input jenis sampah sesuai klasifikasi berikut:")
    print("sisa makanan, sisa buah sayur, sampah tumbuhan")
    print("plastik, logam, kaca, styrofoam")
    print("obat, barang elektronik, residu kimia")

    jenis = input("Masukkan jenis sampah : ").lower()
    jumlah = int(input("Masukkan jumlah sampah (kg): "))

    if jenis in ["sisa makanan", "sisa buah sayur", "sampah tumbuhan"]:
        kategori = "organik"
    elif jenis in ["plastik", "logam", "kaca", "styrofoam"]:
        kategori = "anorganik"
    elif jenis in ["obat", "barang elektronik", "residu kimia"]:
        kategori = "B3"
    else:
        print("Jenis sampah tidak valid!")
        return

    jenis_sampah.append(kategori)
    jumlah_sampah.append(jumlah)

    print("Data berhasil ditambahkan!")
    print("Jenis:", jenis_sampah)
    print("Jumlah:", jumlah_sampah)


def Lihat_data_sampah():
    print("\n===== LIHAT DATA SAMPAH =====")
    if len(jenis_sampah) == 0:
        print("Data Sampah Kosong!")
    else:
        jum_organik = 0
        jum_anorganik = 0
        jum_B3 = 0

        for i in range(len(jenis_sampah)):
            if jenis_sampah[i] == "organik":
                jum_organik += jumlah_sampah[i]
            elif jenis_sampah[i] == "anorganik":
                jum_anorganik += jumlah_sampah[i]
            elif jenis_sampah[i] == "B3":
                jum_B3 += jumlah_sampah[i]

        print("Jenis Sampah:", jenis_sampah)
        print("Jumlah Sampah:", jumlah_sampah)
        print("Total Organik:", jum_organik, "kg")
        print("Total Anorganik:", jum_anorganik, "kg")
        print("Total B3:", jum_B3, "kg")


def Data_daur_ulang():
    print("\n===== DATA DAUR ULANG =====")
    kategori = input("Masukkan kategori sampah yang ingin didaur ulang (organik/anorganik/B3): ")
    jumlah2 = int(input("Masukkan jumlah sampah yang ingin didaur ulang: "))
    metode = input("Masukkan metode daur ulang sampah: ")

    ditemukan = False
    for i in range(len(jenis_sampah)):
        if jenis_sampah[i] == kategori:
            if jumlah_sampah[i] >= jumlah2:
                jumlah_sampah[i] -= jumlah2
                print("Jenis sampah:", jenis_sampah[i])
                print("Jumlah sampah setelah daur ulang:", jumlah_sampah[i])
                print("Metode daur ulang:", metode)
            else:
                print("Jumlah sampah tidak mencukupi!")
            ditemukan = True
            break

    if not ditemukan:
        print("Jenis sampah tidak ditemukan!")


# ===== MAIN PROGRAM =====
while True:
    pilihan = Menu_utama()

    if pilihan == 1:
        Tambah_data_sampah()
    elif pilihan == 2:
        Lihat_data_sampah()
    elif pilihan == 5:
        Data_daur_ulang()
    elif pilihan == 9:
        print("Program selesai!")
        break
    else:
        print("Pilihan salah!\n")
