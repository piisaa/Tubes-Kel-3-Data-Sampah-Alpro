MAKS_DATA = 100
data_sampah = [None] * MAKS_DATA

class Sampah:
    def __init__(self, jenis, kategori, jumlah, metode):
        self.jenis = jenis
        self.kategori = kategori
        self.jumlah = jumlah
        self.metode = metode


def menu_utama():
        print("\n===== MENU UTAMA =====")
        print("1. Tambah Data Sampah")
        print("2. Lihat Data Sampah")
        print("3. Data Daur Ulang")
        print("4. Sequential Search") #merubah data dan hapus data
        print("5. Binary Search") #mencari berdasarkan jenis dan jumlah
        print("6. Urutkan Data")
        print("7. Keluar")

        return input("Masukkan pilihan: ")


def tambah_data(data_sampah, n):

    print("\n===== TAMBAH DATA SAMPAH =====")

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

        if n < MAKS_DATA:

            print("\nData ke-", i + 1)
            jenis = input("Masukkan jenis sampah : ").lower()
            jumlah = int(input("Masukkan jumlah sampah (kg) : "))

        if jenis in ["sisa makanan", "sisa buah sayur", "sampah tumbuhan"]:
            kategori = "Organik"

        elif jenis in ["plastik", "logam", "kaca", "styrofoam"]:
            kategori = "Anorganik"

        elif jenis in ["obat", "barang elektronik", "residu kimia"]:
            kategori = "B3"

        else:
            kategori = ""

        if kategori != "":

            if jenis in ["sisa makanan", "sisa buah sayur", "sampah tumbuhan"]:
                metode = "Recycle"

            elif jenis in ["plastik", "kaca", "logam"]:
                metode = "Recycle"

            elif jenis == "styrofoam":
                metode = "Reduce"

            elif jenis == "barang elektronik":
                metode = "Reuse"

            elif jenis in ["obat", "residu kimia"]:
                metode = "Pengolahan limbah B3"

            else:
                metode = "Metode belum tersedia"

            data_sampah[n] = Sampah(jenis, kategori, jumlah, metode)
            n += 1

            print("\nData berhasil ditambahkan!")

        else:
            print("\nJenis sampah tidak valid!")

    return n


def lihat_data(data_sampah, n):

    if n == 0:
        print("Data kosong")

    else:

        for i in range(n):
          print('\n',
                i + 1,
                "| Jenis :", data_sampah[i].jenis,
                "| Kategori :", data_sampah[i].kategori,
                "| Jumlah :", data_sampah[i].jumlah, "kg",
                "| Metode :", data_sampah[i].metode
                )


def data_daur_ulang(data_sampah, n):

    target = input("Jenis sampah: ").lower()
    jumlah_daur = int(input("Jumlah didaur ulang: "))

    ditemukan = False
    i = 0

    while i < n and ditemukan == False:

        if data_sampah[i].jenis == target:

            ditemukan = True

            if data_sampah[i].jumlah >= jumlah_daur:

                data_sampah[i].jumlah -= jumlah_daur

                print("Berhasil didaur ulang")
                print("Sisa:", data_sampah[i].jumlah)

            else:
                print("Jumlah tidak mencukupi")

        i += 1

    if ditemukan == False:
        print("Data tidak ditemukan")


def sequential_search(data_sampah, n):

    print("\n===== SEQUENTIAL SEARCH ====")
    print("1. Ubah Data")
    print("2. Hapus Data")

    pilihan = input("Pilihan : ")

    target = input("Masukkan jenis sampah : ").lower()

    indeks = -1
    i = 0

    while i < n and indeks == -1:

        if data_sampah[i].jenis == target:
            indeks = i

        i += 1

    if indeks != -1:

        if pilihan == "1":

            jumlah_baru = int(input("Masukkan jumlah baru : "))

            data_sampah[indeks].jumlah = jumlah_baru

            print("Data berhasil diubah")

        elif pilihan == "2":

            for i in range(indeks, n - 1):
                data_sampah[i] = data_sampah[i + 1]

            data_sampah[n - 1] = None

            n -= 1

            print("Data berhasil dihapus")

        else:
            print("Pilihan tidak valid")

    else:
        print("\nData tidak ditemukan")

    return n


def selection_sort_jenis(data_sampah, n, mode):

  for i in range(n - 1):

      idx = i

      for j in range(i + 1, n):

          if mode == "asc":

              if data_sampah[j].jenis < data_sampah[idx].jenis:
                  idx = j

          else:

              if data_sampah[j].jenis > data_sampah[idx].jenis:
                  idx = j

      temp = data_sampah[i]
      data_sampah[i] = data_sampah[idx]
      data_sampah[idx] = temp


def insertion_sort_jumlah(data_sampah, n, mode):

  for i in range(1, n):

      key = data_sampah[i]

      j = i - 1

      if mode == "asc":

          while j >= 0 and data_sampah[j].jumlah > key.jumlah:

              data_sampah[j + 1] = data_sampah[j]
              j -= 1

      else:

          while j >= 0 and data_sampah[j].jumlah < key.jumlah:

              data_sampah[j + 1] = data_sampah[j]
              j -= 1

      data_sampah[j + 1] = key


def binary_search(data_sampah, n):

    if n == 0:
        print("Data kosong")

    else:

        print("\n===== BINARY SEARCH =====")
        print("1. Cari berdasarkan jenis")
        print("2. Cari berdasarkan jumlah")

        pilihan = input("Pilihan : ")

        indeks = -1

        # Cari berdasarkan jenis
        if pilihan == "1":

            target = input("Masukkan jenis sampah : ").lower()

            # urutkan berdasarkan jenis
            selection_sort_jenis(data_sampah, n, "asc")

            kiri = 0
            kanan = n - 1

            while kiri <= kanan and indeks == -1:

                tengah = (kiri + kanan) // 2

                if data_sampah[tengah].jenis == target:

                    indeks = tengah

                elif target < data_sampah[tengah].jenis:

                    kanan = tengah - 1

                else:

                    kiri = tengah + 1


        # Cari berdasarkan jumlah
        elif pilihan == "2":

            target = int(input("Masukkan jumlah sampah : "))

            # urutkan berdasarkan jumlah
            insertion_sort_jumlah(data_sampah, n, "asc")

            kiri = 0
            kanan = n - 1

            while kiri <= kanan and indeks == -1:

                tengah = (kiri + kanan) // 2

                if data_sampah[tengah].jumlah == target:

                    indeks = tengah

                elif target < data_sampah[tengah].jumlah:

                    kanan = tengah - 1

                else:

                    kiri = tengah + 1

        else:
            print("Pilihan tidak valid")


        if indeks != -1:

            print("\nData ditemukan")
            print("Jenis     :", data_sampah[indeks].jenis)
            print("Kategori  :", data_sampah[indeks].kategori)
            print("Jumlah    :", data_sampah[indeks].jumlah, "kg")
            print("Metode    :", data_sampah[indeks].metode)

        elif pilihan == "1" or pilihan == "2":

            print("\nData tidak ditemukan")


def menu_sort(data_sampah, n):

    if n == 0:
        print("Data kosong")

    else:

        print("\n===== URUTKAN DATA =====")
        print("1. Jenis (Selection Sort)")
        print("2. Jumlah (Insertion Sort)")

        pilih = input("Pilihan : ")

        if pilih == "1":

            print("\n1. Ascending")
            print("2. Descending")

            urutan = input("Pilihan : ")

            if urutan == "1":
                selection_sort_jenis(data_sampah, n, "asc")

            elif urutan == "2":
                selection_sort_jenis(data_sampah, n, "desc")

            else:
                print("Pilihan tidak valid")


        elif pilih == "2":

            print("\n1. Ascending")
            print("2. Descending")

            urutan = input("Pilihan : ")

            if urutan == "1":
                insertion_sort_jumlah(data_sampah, n, "asc")

            elif urutan == "2":
                insertion_sort_jumlah(data_sampah, n, "desc")

            else:
                print("Pilihan tidak valid")

        else:
            print("Pilihan tidak valid")


        # tampilkan hasil pengurutan
        if pilih == "1" or pilih == "2":

            print("\n===== DATA SETELAH DIURUTKAN =====")

            for i in range(n):

                print('\n',
                    i + 1,
                    "| Jenis :", data_sampah[i].jenis,
                    "| Kategori :", data_sampah[i].kategori,
                    "| Jumlah :", data_sampah[i].jumlah, "kg",
                    "| Metode :", data_sampah[i].metode
                )

n = 0
selesai = False

while selesai == False:
    pilihan = menu_utama()

    if pilihan == "1":
        n = tambah_data(data_sampah, n)

    elif pilihan == "2":
        lihat_data(data_sampah, n)

    elif pilihan == "3":
        data_daur_ulang(data_sampah, n)

    elif pilihan == "4":
        n = sequential_search(data_sampah, n)

    elif pilihan == "5":
        binary_search(data_sampah, n)

    elif pilihan == "6":
        menu_sort(data_sampah, n)

    elif pilihan == "7":
        selesai = True
        print("Program selesai")

    else:
        print("Pilihan tidak valid")