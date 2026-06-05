#hana
# ===== PROGRAM PENGELOLAAN SAMPAH =====

data_sampah = []

# ===== MENU UTAMA =====
def Menu_utama():

    print("\n===== MENU UTAMA =====")
    print("1. Tambah Data Sampah")
    print("2. Lihat Data Sampah")
    print("3. Tambah Data Daur Ulang")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan menu : ")
    return pilihan


# ===== TAMBAH DATA SAMPAH =====
def Tambah_data_sampah():

    print("\n===== TAMBAH DATA SAMPAH =====")

    # ===== LIST JENIS SAMPAH =====
    print("Jenis sampah yang tersedia:")
    print("- sisa makanan")
    print("- sisa buah sayur")
    print("- sampah tumbuhan")
    print("- plastik")
    print("- logam")
    print("- kaca")
    print("- styrofoam")
    print("- obat")
    print("- barang elektronik")
    print("- residu kimia")

    banyak = int(input("\nBerapa data yang ingin ditambahkan : "))

    for i in range(banyak):

        print("\nData ke-", i + 1)

        jenis = input("Masukkan jenis sampah : ").lower()
        jumlah = int(input("Masukkan jumlah sampah (kg) : "))

        # ===== KATEGORI SAMPAH =====
        if jenis in ["sisa makanan", "sisa buah sayur", "sampah tumbuhan"]:
            kategori = "organik"

        elif jenis in ["plastik", "logam", "kaca", "styrofoam"]:
            kategori = "anorganik"

        elif jenis in ["obat", "barang elektronik", "residu kimia"]:
            kategori = "B3"

        else:
            print("Jenis sampah tidak valid!")
            continue


        # ===== METODE DAUR ULANG =====
        # UBAH BAGIAN INI SESUAI KEBUTUHAN

        if jenis in ["sisa makanan", "sisa buah sayur", "sampah tumbuhan"]:
            metode = "Recycle"

        elif jenis in ["plastik", "kaca", "logam"]:
            metode = "Recycle"

        elif jenis in ["styrofoam"]:
            metode = "Reduce"

        elif jenis in ["barang elektronik"]:
            metode = "Reuse"

        elif jenis in ["obat", "residu kimia"]:
            metode = "Pengolahan limbah B3"

        else:
            metode = "Metode belum tersedia"

        # =================================


        # ===== SIMPAN DATA =====
        data = {
            "jenis": jenis,
            "kategori": kategori,
            "jumlah": jumlah,
            "metode": metode
        }

        data_sampah.append(data)

        print("Data berhasil ditambahkan!")

    print()


# ===== LIHAT DATA SAMPAH =====
def Lihat_data_sampah():

    print("\n===== LIHAT DATA SAMPAH =====")

    if len(data_sampah) == 0:
        print("Data sampah kosong!")
        return

    total_organik = 0
    total_anorganik = 0
    total_B3 = 0

    for i in range(len(data_sampah)):

        print(
            i + 1,
            "| Jenis :", data_sampah[i]["jenis"],
            "| Kategori :", data_sampah[i]["kategori"],
            "| Jumlah :", data_sampah[i]["jumlah"], "kg",
            "| Metode :", data_sampah[i]["metode"]
        )

        # ===== HITUNG TOTAL =====
        if data_sampah[i]["kategori"] == "organik":
            total_organik += data_sampah[i]["jumlah"]

        elif data_sampah[i]["kategori"] == "anorganik":
            total_anorganik += data_sampah[i]["jumlah"]

        elif data_sampah[i]["kategori"] == "B3":
            total_B3 += data_sampah[i]["jumlah"]

    print("\n===== TOTAL SAMPAH =====")
    print("Total Organik :", total_organik, "kg")
    print("Total Anorganik :", total_anorganik, "kg")
    print("Total B3 :", total_B3, "kg")


# ===== DATA DAUR ULANG =====
def Data_daur_ulang():

    print("\n===== DATA DAUR ULANG =====")

    if len(data_sampah) == 0:
        print("Data sampah kosong!")
        return

    cari = input("Masukkan jenis sampah yang ingin didaur ulang : ").lower()
    jumlah_daur = int(input("Masukkan jumlah yang ingin didaur ulang : "))

    ditemukan = False

    for i in range(len(data_sampah)):

        if data_sampah[i]["jenis"] == cari:

            ditemukan = True

            if data_sampah[i]["jumlah"] >= jumlah_daur:

                data_sampah[i]["jumlah"] -= jumlah_daur

                print("\nData berhasil didaur ulang!")
                print("Jenis :", data_sampah[i]["jenis"])
                print("Metode :", data_sampah[i]["metode"])
                print("Sisa jumlah :", data_sampah[i]["jumlah"], "kg")

            else:
                print("Jumlah sampah tidak mencukupi!")

            break

    if ditemukan == False:
        print("Jenis sampah tidak ditemukan!")


# ===== MAIN PROGRAM =====
while True:

    pilihan = Menu_utama()

    if pilihan == "1":
        Tambah_data_sampah()

    elif pilihan == "2":
        Lihat_data_sampah()

    elif pilihan == "3":
        Data_daur_ulang()

    elif pilihan == "4":
        print("Program selesai!")
        break

    else:
        print("Pilihan salah!\n")