def Menu_utama ():
  print ("===== MENU UTAMA =====")
  print ("1. Tambah Data Sampah")
  print ("2. Lihat Data Sampah")
  print ("3. Ubah Data Sampah")
  print ("4. Hapus Data Sampah")
  print ("5. Tambah Data Daur Ulang")
  print ("6. Cari Data Sampah")
  print ("7. Urutkan Data")
  print ("8. Statistik Sampah & Daur Ulang")
  print ("9. Keluar")

  pilihan = int(input("Masukkan pilihan menu : "))
  return pilihan
  print ()

jenis_sampah= []
jumlah_sampah = []
def Tambah_data_sampah ():
  print ()
  print ("===== TAMBAH DATA SAMPAH =====")
  print ("input jenis sampah seusai klasifikasi berikut:")
  print ("sisa makanan, sisa buah sayur, sampah tumbuhan ")
  print ("plastik, logam, kaca, styrofoam")
  print ("obat, barang elektronik, residu kimia")

  jenis = input("Masukkan jenis sampah : ")
  jumlah = int(input("Masukkan jumlah sampah (kg): "))

  if jenis in ["sisa makanan", "sisa buah sayur", "sampah tumbuhan"]:
    jenis = "organik"
  elif jenis in ["plastik", "logam", "kaca", "styrofoam"]:
    jenis = "anorganik"
  elif jenis in ["obat", "barang ekeltronik", "residu kimia"]:
    jenis = "B3"
  else:
    print ("Jenis sampah tidak valid!")

  jenis_sampah.append(jenis)
  jumlah_sampah.append(jumlah)

  print ("jenis: ", jenis_sampah)
  print ("jumlah:", jumlah_sampah)
  print ("Data berhasil ditambahkan!")
  print ()

jum_organik = 0
jum_anorganik = 0
jum_B3 = 0
def Lihat_data_sampah ():
  print ()
  print ("===== LIHAT DATA SAMPAH =====")
  if len(jenis_sampah) == 0:
    print ("Data Sampah Kosong!")
  else:
    for i in range (len(jenis_sampah)):
      if jenis_sampah[i] == "organik":
        jum_organik += jumlah_sampah[i]
      elif jenis_sampah[i] == "anorganik":
        jum_anorganik += jumlah_sampah[i]
      elif jenis_sampah[i] == "B3":
        jum_B3 += jumlah_sampah[i]
      else:
        print ("Jenis sampah tidak valid!")
      jumlah_sampah.append(jum_organik, jum_anorganik, jum_B3)
    print ("Jenis Sampah:", jenis_sampah)
    print ("Jumlah Sampah:", jumlah_sampah)
  print ()

def Data_daur_ulang ():
  print ()
  print ("===== DATA DAU RULANG =====")
  print ("jenis")
  kategori = input ("Masukan kategori sampah yang ingin didaur ulang: ")
  jumlah2 = int(input("Masukan jumlah sampah yang ingin didaur ulang: "))
  metode = input("Masukan metode daur ulang sampah: ")
  for i in range (len(jenis_sampah)):
    if jenis_sampah[i] == kategori:
      jumlah_sampah[i] = jumlah_sampah[i] - jumlah2
      print ("Jenis sampah:", jenis_sampah[i])
      print ("Jumlah sampah:", jumlah_sampah[i])
      print ("Metode daur ulang sampah:", metode)
  else:
    print ("Jenis sampah tidak ditemukan!")



while True:
  pilihan = Menu_utama()

  if pilihan == 1:
    Tambah_data_sampah()

  elif pilihan == 2:
    Lihat_data_sampah()

  elif pilihan == 5:
    Data_daur_ulang()

  elif pilihan == 9:
    print ("Program selesai!")
    break

  else:
    print ("Pilihan salah!")
    print ()