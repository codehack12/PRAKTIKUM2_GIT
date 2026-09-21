# angka = [4, 3, 2]
# jumlah = sum(angka)

# print(jumlah) #function sum() digunakan untuk menjumlahkan semua elemen dalam list angka. Hasilnya adalah 9, karena 4 + 3 + 2 = 9.

# kelompok_2  = ["afdal", "muaz","julio", "salsa", "manda", "RIFKA", "dan yang lain"]
# if "RIFKA" in kelompok_2:
#     print("ADA VILLAIN DI KELOMPOK 2") 
#     #program ini akan memeriksa apakah "RIFKA" ada dalam list kelompok_2. Jika ada, maka akan mencetak "ADA VILLAIN DI KELOMPOK 2".
# if "RIFKA" not in kelompok_2:
#     print("TIDAK ADA VILLAIN DI KELOMPOK 2") 
#     #program ini akan memeriksa apakah "RIFKA" tidak ada dalam list kelompok_2. Jika tidak ada, maka akan mencetak "TIDAK ADA VILLAIN DI KELOMPOK 2".




#conditional statement

# angka = 10
# frekuensi = 5
# angkaTercapai = angka > 10 or frekuensi >= 5

# print(angkaTercapai)

# print("selamat angka tercapai")

#contoh lainnya 

# sudah_makan = False

# if not sudah_makan:
#     print("aayo makan")


#tugas gemini

#1
# kursiTersedia = int(input("masukkan nomor kursi anda:"))

# if kursiTersedia >= 3:
#     print("tersedia")
# elif kursiTersedia == 3:
#     print("tersedia")
# else:
#     print("mohon maaf, kursi tidak tersedia")

# print("kursiTersedia: ", kursiTersedia)

#2
# umur = int(input("berapa umur anda: ")) #boolean adaalah tipe data yang bernilai True/False di mana ketika si variabel bernilai benar maka hasilnya true. dan jika tidak maka outputnya False. 
# Ktp  = bool(input("apakah anda memiliki Ktp?: (true/false)"))

# dewasa = umur > 18 and Ktp == True
# print("anda sudah dewasa:", dewasa)

#3
# kursi_tersedia = True 

# if kursi_tersedia == True:
#     print("ada kursi yang tersedia")
# else:
#     print("mohon maaf, kursi sudah penuh🙏")


1
# angka = [14, 27, 33, 42, 50, 61]
# genap = [ x for x in angka if x % 2 == 0]
# ganjil = [ x for x in angka if x % 2 != 0]
# subTotalGanjil = len(ganjil)
# subTotalGenap = len(genap)
# print("jumlah angka Ganjil", subTotalGanjil)
# print("jumlah angka genap", subTotalGenap)
# print("list angka genap:", genap)
# print("list angka ganjil:", ganjil)

# test case 2
# angka = [2, 4, 6, 8]

# genap = [ x for x in angka if x % 2 == 0]
# print(genap)



#2
# nilai = [75, 80, -1, 95, -1, 60]

# nilaiValid = [ x for x in nilai if x != -1]

# if len(nilaiValid) > 0 :
#     nilaiTertinggi = max(nilaiValid)
#     nilaiTerendah = min(nilaiValid)

# print(nilaiValid)
# print(nilaiTertinggi)
# print(nilaiTerendah)

#test case 2
# nilai = [-1, -1, -1]

# nilaiValid = [ x for x in nilai if x > 0]
# nilai_tidak_valid = [x for x in nilai if x < 0]

# print(nilaiValid)
# print(nilai_tidak_valid)


# #3
# Barang = [25000, 15000, 40000]
# uang = 100000

# jumlah_barang = int(sum(Barang))

# belanja = jumlah_barang - uang

# print(belanja)

# for i in range (4):
#     print("sisfo")

# jumlah = 0
# for i in range(1,11,2):
#     jumlah = jumlah + i 
# print(jumlah)

# jumlah = 0 
# for i in range(1, 21, 1):
#     if i % 2 == 0 and i % 3 == 0:
#         jumlah = jumlah + i
# print(jumlah)


# angka = int(input("masukkan angka: "))

# if angka == 0:
#     print("ini nialinya nol")
# elif angka > 0:
#     print("ini nilainya positif")
#     if angka % 2 == 0:
#         print("ini nilainya genap")
#     elif angka % 2 != 0:
#         print("ini nilainya ganjil")





# hari = input("masukkan hari: ").lower()

# match hari: 
#     case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
#         print("Hari kerja")
#     case "sabtu" | "minggu":
#         print("Akhir pekan")
#     case _:
#         print("Hari tidak valid")


# nilai = int(input("masukkan nilai: "))
# tugasTambahan = int(input("masukkan nilai tugas: "))
# kehadiran = int(input("jumlah kehadiran: " ))

# if nilai >= 85 and kehadiran >= 75:
#     print("lulus dengan predikat A")
# elif nilai >= 75 and kehadiran >= 75:
#     print("lulus dengan predikat b")
# elif nilai >= 60 and kehadiran >= 75:
#     print("lulus dengan predikat c")
# else:
#     print("tidak lulus")
#     if tugasTambahan >= 70:
#         print("lulus dengan predikat c")  
#     elif kehadiran >= 75:
#             print("lulus dengan predikat c")

# lulus = nilai >= 60 and kehadiran >= 75

# print(lulus)


# def hitungHargaTiket(umur, hariLibur):

#     if umur < 12:
#         harga = 30000
#     elif umur >= 12:
#         harga = 50000


#     if hariLibur == True:
#         harga = harga + 10000
#     elif hariLibur == False:
#         harga = harga + 0

#     return harga 

# tiketAnak = hitungHargaTiket(10, True)
# print("harga tiket anak(hari libur): ", tiketAnak)

# tiketDewasa = hitungHargaTiket(15, False)
# print("harga tiket dewasa(hari biasa): ", tiketDewasa)

# def cekUjian(nilai):

#     if nilai >= 85 and nilai <= 100:
#         predikat = "A"
#     elif nilai >= 75 and nilai <= 84:
#         predikat = "B"
#     elif nilai >= 60 and nilai <= 74:
#         predikat = "C"
#     else:
#         predikat = "D"

#     lulus = "LULUS" if nilai >= 75 else "remedial"

#     return predikat, lulus

# predikat, lulus = cekUjian(75)
# print(lulus)

# def hitungParkir(kendaraan, durasi):

#     if kendaraan == "mobil":
#         if durasi <= 1:
#             totalBiaya = 7000
#         else:
#             totalBiaya = 7000 + ((durasi - 1) * 7000)

#     elif kendaraan == "motor":
#         if durasi <= 1:
#             totalBiaya = 3000
#         else:
#             totalBiaya = 3000 + ((durasi - 1) * 3000)

#     else:
#         totalBiaya = 0

#     return totalBiaya

# hasilMotor = hitungParkir("motor", 3)
# print("total biaya parkir: ", hasilMotor)

# def hitungTotalBelanja(belanja):
#     if belanja >= 500000:
#         diskon = 0.20
#     else:
#         diskon = 0
#     totalBelanja = belanja - (belanja * diskon)
#     return int(totalBelanja)

# print("total belanja anda: ", hitungTotalBelanja(500000))

# def hargaTiket(hariKunjungan):

#     if hariKunjungan == "sabtu":
#         hargaTiket = 50000
#     elif hariKunjungan == "minggu":
#         hargaTiket = 50000
#     else:
#         hargaTiket = 35000
        
#     return hargaTiket

# print(hargaTiket("kamis"))



# kehadiran = int(input('masukkan jumlah kehadiran anda: '))

# if kehadiran < 75:
#     print('anda tidak lulus')
# else :
#     nilai = int(input('masukkan nilai anda: '))
#     if nilai >= 75:
#         print('predikat memuaskan')
#     elif nilai >= 60 and nilai <= 74:
#         print('predikat cukup')
#         if nilai >=60 and nilai <= 65:
#             penerima_beasiswa = bool(input('apakah anda penerima beasisiwa (True/False)'))
#             if penerima_beasiswa == True:
#                 print('lulus dengan catatan')
#     elif nilai < 60:
#         print('tidak lulus')


# kehadiran = int(input('masukkan jumlah kehadiran anda: '))

# if kehadiran < 75:
#     print('Status: Tidak Lulus (Kehadiran kurang dari 75%)')
# else:
#     nilai = int(input('masukkan nilai anda: '))
    
#     # Tentukan status dasar berdasarkan nilai
#     if nilai >= 75:
#         status = 'Lulus Memuaskan'
#     elif nilai >= 60 and nilai <= 74:
#         status = 'Lulus Cukup'
#     else:
#         status = 'Tidak Lulus'
    
#     # Cek aturan khusus beasiswa untuk nilai 60-65
#     if 60 <= nilai <= 65:
#         # Perhatikan cara memperbaiki input boolean di sini
#         penerima_beasiswa = input('apakah anda penerima beasiswa (True/False): ') == 'True'
        
#         if penerima_beasiswa:
#             status = 'Lulus dengan Catatan' # Di-override di sini!

#     print(f'Hasil Akhir: {status}')


# pacar = ['siapa', 'aku', 'anak']
# for i in pacar:
#     print(f'dia adalah pacar saya {i}')


# for huruf in 'buah':
#     print(f"ini adalah salah satu huruf : {huruf}")

# jam_antri = 1

# while jam_antri <= 5:
#     print(f'jam {jam_antri}: silahkan maju lagi')

# jam_antri += 1
# print("besnsin habis")


# angka = [14, 27, 33, 42, 50, 61]
# ganjil = 0
# genap = 0

# for i in angka:
#     if i % 2 !=0:
#         ganjil += 1
#     else:
#         genap += 1

# print(f"ganjil: {ganjil},  genap: {genap}")

#for dengan string

# for i in "python":
#     print(i)

#for dengan range

# for i in range(5):
#     print(i)

#while

# jam_antri = 1
# while jam_antri <= 5:
#     print(f"{jam_antri} jam : Antrean maju setengah meter... 🛵 ")
#     jam_antri += 1
# print("BENSIN HABIS!. Silakan putar balik!")

#while loop

# while True:
#     angka = input("masukkan angka: ")
#     if angka == "0":
#         break
#     print(f'kamu memasukkan angka {angka}')

# print("apakah dulee")


# sisa_tugas = 5
# while sisa_tugas > 0:
#     print(f"memproses tugas.... sisa antrian {sisa_tugas} ")
#     sisa_tugas -= 1
# print('seluruh tugas sudah selesai')


# angka = 0

# while angka < 10:
#     angka += 1
#     if (angka % 2 == 0):
#         continue#skip yang memenuhi if di atas
#     print(angka)


#while else:

# angka = [2, 4,6, 8]

# for i in angka:
#     if i == 7:
#         print(f'angka ditemukan {i}')
#         break
# else:
#     print('angka tidak ditemukan')

# sisa_tugas = 5
# while sisa_tugas > 0:
#     print(f"memproses tugas.... sisa antrian {sisa_tugas} ")
#     sisa_tugas -= 1
#     if (sisa_tugas == 2):
#         break
# print('server overload, proses dihentikan paksa')

# adj = ['buah', 'enak']
# fruits = ['apel', 'pisang']

# for x in adj:
#     for i in fruits:
#         print(x,i)

# x = 5
# y ='lima' 

# try :
#     z = x+y
# except :
#     z = str(x) + y
# finally :
#     print('lakukan konversi tipe data')
# print(z)

# minuman = ['kopi', 'es teh']
# makanan= ['indomie', 'roti bakar']

# for x in minuman:
#     for i in makanan:
#         print(f'paket: {x,i}')


# buah = ["apel", 'mangga']

# for i in buah:
#     print('ini adalah nama2 buah: ', i)

# for i in range(1,5):
#     print(i)

makanan = ['indomie', 'roti bakar']
minuman = ['air putih']

for i in makanan:
    for x in minuman:
        print('paket: ', i ,'+', x)