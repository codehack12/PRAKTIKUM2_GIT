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

# makanan = ['indomie', 'roti bakar']
# minuman = ['air putih']

# for i in makanan:
#     for x in minuman:
#         print('paket: ', i ,'+', x)




# while True:
#     try:
#         item = int(input('masukkan jumlah item: '))
#         if item == 0:
#             print('toko ditutup')
#             break
#         elif item < 0:
#             print('jumlah tidak butuh negatif')
#         elif item > 100:
#             print('maksimal 100 item')
#         else:
#             print(f'transaksi {item} berhasil')
#     except ValueError:
#         print('input harus berupa angka')

# total_pendapatan = 0
# jumlah_pengunjung = 0

# print("=== SISTEM KASIR FUNLAND ===")

# while True:
#     input_user = input("\nMasukkan umur pengunjung (atau 'selesai'): ")
    
#     # Cek kondisi berhenti
#     if input_user.lower() == 'selesai':
#         break
        
#     try:
#         umur = int(input_user)
#     except ValueError:
#         print("Input tidak valid! Masukkan angka atau 'selesai'.")
#         continue
        
#     if umur < 0:
#         print("Umur tidak valid!")
#         continue
        
#     # Penentuan harga
#     if umur <= 3:
#         harga = 0
#         kategori = "Balita (Gratis)"
#     elif umur <= 10:
#         harga = 35000
#         kategori = "Anak-anak"
#     else:
#         harga = 70000
#         kategori = "Dewasa"
        
#     total_pendapatan += harga
#     jumlah_pengunjung += 1
#     print(f"Kategori: {kategori} | Harga: Rp {harga:,}")

# print("\n===============================")
# print(f"Total Pengunjung : {jumlah_pengunjung} orang")
# print(f"Total Pendapatan : Rp {total_pendapatan:,}")
# print("===============================")
            


# while True:
#     try:
#         jumlah = int(input('masukkan jumlah item: '))
#     except ValueError:
#         print('input hatus berupa angka')

#     if jumlah < 0:
#         print('input tidak boleh negatif!')
#         continue
#     if jumlah > 100:
#         print('maksimal 100 item per transaksi!')
#         continue
#     if jumlah == 0:
#         print('toko ditutup, transaksi selesai!')
#         break

#     print(f'transaksi {jumlah} item berhasil!!')
    
# while True:
#     try:
#         angka = int(input('masukkan angka: '))
#     except ValueError:
#         print('input harus angka')
    


# print('\n---setup denah bioskop---\n')


# while True:
#     try:
#         jumlah_baris = int(input('masukkan jumlah baris: '))
#         if jumlah_baris <= 0:
#             print('jumlah baris harus lebih dari 0!')
#             continue
#         jumlah_kursi = int(input('masukkan jumlah kursi per baris: '))
#         if jumlah_kursi <= 0:
#             print('jumlah kursi harus lebih dari 0!')
#             continue
#         break
#     except ValueError:
#             print('input harus berupa angka')

# print('\n=== Daftar kursi tersedia ===\n')             
# for baris in range(1, jumlah_baris + 1):
#     for kursi in range(1, jumlah_kursi + 1):
#         if kursi == 13:
#             continue
#         if baris == 1 and kursi % 2 == 0:
#             continue

#         print(f'baris {baris} - kursi {kursi}')



# print('\n---SETUP DENAH BIOSKOP NONTON YUK---\n')
# while True:
#     try:
#         jumlah_baris = int(input('masukkan jumlah baris: '))
#         if jumlah_baris < 0:
#             print('jumlah baris harus lebih dari 0')
#             continue
#         jumlah_kursi = int(input('masukkan jumlah kursi: '))
#         if jumlah_kursi < 0:
#             print('jumlah kursi harus lebih dari 0')
#             continue
#         break
#     except ValueError:
#         print('input harus berupa angka')

# print('\n===DAFTAR KURSI TERSEDIA===\n')
# for baris in range(1, jumlah_baris + 1):
#     for kursi in range(1, jumlah_kursi + 1):

#         if kursi == 13:
#             continue
#         if baris == 1 and kursi % 2 == 0:
#             continue

#         print(f'baris {baris} - kursi {kursi}')


# while True:
#     try:
#         kursi = int(input('masukkan jumlah maksimal kursi: '))
#         if kursi < 0:
#             print('jumlah harus lebih dari 0 ')
#             continue
#         break
#     except ValueError:
#         print('input harus berupa angka')

# sisa_kursi = kursi 
# pendapatan_total = 0

# print('\n===SISTEM RESERVASI PO BUS DIMULAI===\n')

# while sisa_kursi > 0:
#     print(f'sisa kursi {sisa_kursi}')

#     try:
#         umur = int(input('masukkan umur penumpang: '))
#     except ValueError:
#         print('input harus berupa angka')
#         continue

#     if umur < 0:
#         print('umur tidak valid')
#         continue

#     if umur <= 5:
#         kategori = 'Balita - Tiket Gratis (Rp 0)'
#         harga = 0
    
#     elif umur <= 12:
#         kategori = "Anak - Harga: Rp 50.000"
#         harga = 50000
    
#     else:
#         kategori = "Dewasa - Harga: Rp 100.000"
#         harga = 100000
    
        
#     print(f'kategori: {kategori}')

#     sisa_kursi -= 1
#     pendapatan_total += harga

# print('\n===SEMUA KURSI TERISI===\n')
# print(f'total pendapatan perjalanan ini = {pendapatan_total}')

# total = 0

# while True:
#     harga = int(input("Masukkan harga barang (ketik 0 untuk selesai): "))

#     # 1. Kondisi untuk menghentikan loop
#     if harga == 0:
#         break

#     # 2. Filter barang dengan harga kurang dari 100.000 (diabaikan)
#     if harga < 100000:
#         print("Barang di bawah Rp100.000 diabaikan.\n")
#         continue

#     # 3. Akumulasi total belanjaan
#     total += harga
#     print(f"Subtotal saat ini: Rp{total:,}\n")

# # 4. Pengecekan diskon setelah semua barang selesai diinput
# if total >= 100000:
#     diskon = total * 0.10
#     total_akhir = total - diskon
#     print(f"Selamat! Anda mendapatkan diskon 10% (Rp{diskon:,.0f}).")
#     print(f"Total yang harus dibayar: Rp{total_akhir:,.0f}")
# else:
#     print(f"Total yang harus dibayar: Rp{total:,}")


# for i in range(1,31):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'angka [{i}]: kelipatan angka 3 dan kelipatan angka 5')
#     elif i % 2 == 0:
#         print(f'angka [{i}]: genap')
#     else:
#         print(f'angka [{i}]: ganjil')


# kode = 123456
# percobaan = 3

# print('\n===== SELAMAT DATANG ======\n')
# while True:
#     try:
#         pin = int(input('masukkan pin anda: '))

#         if pin == kode:
#             print('Selamat datang, akses anda diterima')
#             break

#         else:
#             percobaan -= 1
#             if percobaan > 0:
#                 print(f'kode salah, sisa percobaan [{percobaan}]')
#                 continue
#             elif percobaan == 0:
#                 print('KARTU ATM ANDA TERBLOKIR')
#                 break

#     except ValueError:
#         print('\npin harus berupa angka\n')


# nilai_siswa = [45, 78, 60, 88, 30, 95, 52, 70]
# kkm = 60

# siswa_lulus = 0
# siswa_tidak_lulus = 0
# nilai_lulus = 0

# for angka in nilai_siswa:
#     if angka >= kkm:
#         siswa_lulus += 1
#         nilai_lulus += angka

#     else:
#         siswa_tidak_lulus += 1

# if siswa_lulus > 0:
#     nilai_rata_rata = nilai_lulus / siswa_lulus
# else:
#     nilai_rata_rata = 0


# print(f'siswa yang lulus: {siswa_lulus}')
# print(f'siswa yang tidak lulus: {siswa_tidak_lulus}')
# print(f'nilai rata-rata: {nilai_rata_rata}')

# umur_pendaftar = [14, 22, 17, 35, 10, 50]
# kategori_anak = 0
# kategori_remaja = 0
# kategori_dewasa = 0

# for umur in umur_pendaftar:
#     if umur < 12:
#         kategori_anak += 1
#         print('kategori = anak-anak, belum boleh daftar')

#     elif  umur <= 17 and umur >= 12:
#         kategori_remaja += 1
#         print('kategori = remaja, izin orang tua')
#     else:
#         kategori_dewasa += 1
#         print('kategori = dewasa, diterima')

# print('\n==== daftar kategori pengunjung ====\n')

# print(f'jumlah pendaftar kategori anak-anak = {kategori_anak}')
# print(f'jumlah pendaftar kategori remaja = {kategori_remaja}')
# print(f'jumlah pendaftar kategori dewasa = {kategori_dewasa}')



# for i in range(1,10,2):
#     if i == 3:
#         print('angka 2 ditemukan')
#         break
#     print(i)

# total_pengunjung = 0
# total_harga = 0

# while True:
#     try:
#         umur = int(input('masukkan umur anda: '))

#         if umur < 12:
#             harga = 25000
#         elif umur <= 60:
#             harga = 50000
#         else:
#             harga = 35000

#         print('harga tiket: ', harga)

#         total_harga += harga
#         total_pengunjung += 1

#         pengunjung = input('apakah masih ada pengunjung lain (ya/tidak): ').strip().lower()

#         if pengunjung == 'tidak':
#             break 

#     except ValueError:
#         print('input harus berupa angka!!')

# print('\n=== rekapitulasi===\n')
# print(f'total pengunjung ada: {total_pengunjung}')
# print(f'total bayar: {total_harga}')


# def halo():
#     print('hello world')

# halo()


# def kuadrat(a, b):
#     return a ** b

# hasil = kuadrat(5, 2)

# print(hasil)

# def nilai(a, b):

#     return  a * b

# hasil = nilai(5, 3)

# print(hasil)


# def greet(sapa_pengguna = 'tamu'):
#     print(f'halo {sapa_pengguna}')

# greet()
# greet('afdal')

# def cetak_angka(*args):
#     total = sum(args)  # Akan mencetak dalam bentuk tupel
#     return total

# # Cara memanggilnya dengan banyak angka bebas:
# cetak_angka(1, 2, 3, 4, 5)

# def sapa_peseta(nama = 'pengunjung'):
#     print(f'selamat datang {nama}')

# sapa_peseta()
# sapa_peseta('afdal')

# def total_belanja(*args):
#     total = sum(args)
#     return total

# belanja = total_belanja(10000, 25000, 5000)
# print(f'total belanja anda adalah: {belanja}')

# def nama_usia(a, b):
#     print(f'nama saya {a} dan usia saya {b}')

# nama_usia(20, "afdal")


# def identitas( nama = 'afdal ginaya', usia = 20):
#     print(f'nama saya {nama}, dan usia saya {usia}, kamu bisa memanggil saya {nama}')

# identitas()


# def hitung_harga_akhir(harga_akhir, diskon): 

#     proses = harga_akhir - (harga_akhir * diskon)
#     return proses


# print(hitung_harga_akhir(100000, 0.2)) 

# def bagi_angka(a, b):
#     proses = a / b
#     return proses

# print(bagi_angka(10, 2))

# def hello():
#     print('halo')

# hello()

# def nama_peserta(peserta):
#     list_peserta = peserta.copy()
#     for i in list_peserta:
#         print(f'halo peserta: {i}')

# nama = ['afdal', 'arya', 'faiz']
# namaku = ['afdal']
# nama_peserta(nama)
# nama_peserta(namaku)


#fungsi dengan return

# def keliling(sisi):
#     hasil = 4 * sisi
#     return hasil

# print(keliling(4))

# def keliling(angka):
#     return 4*angka

# s = 10 + keliling(2)

# print(s)

# def penyambutan(nama):
#     list_tamu = nama.copy()
#     for i in list_tamu:
#         print(f'selamat datang: {i}')

# nama_tamu = ['afdal', 'arya']

# print(penyambutan(nama_tamu))


# def operasi_matematika(angka1, angka2):
#     kali = angka1 * angka2
#     tambah = angka1 + angka2
#     kurang = angka1 - angka2
#     return kali,tambah,kurang

# print(operasi_matematika(1,3))


# def nama(sifat = "orang baek", umur = 10):
#     print(f'berapa umur mu: {umur}, apa sifat kamu: {sifat}')

# afdal = nama(sifat = 'bad', umur = 21)

# print(afdal)
#print(f"{"-"*40:^40}")

# def perkenalan(nama, umur):
#     return f'nama saya: {nama}, umur saya: {umur}'

# print(perkenalan('afdal', 17))

# def kali(angka):


#def nama_fungsi(parameter):
    #badan fungsi


# nama_fungsi()

# def harga(kopi, jumlah):
#     tanpa_diskon = (kopi*jumlah)
#     setelah_diskon = tanpa_diskon - (tanpa_diskon*0.1)
#     return setelah_diskon

# print(harga(25000, 2))

# def penjumlahan(*angka):
#     rata2 = sum(angka)/len(angka)
#     return rata2

# print(f'rata-ratanya adalah: {penjumlahan(1,2,3,4,5)}')



# def angka(*nomor):
#     jumlah = 0
#     for i in nomor:
#         jumlah += i
#     return jumlah

# print(angka(1,2,3,4,5))

# def angka(*args):
#     jumlahkan = sum(args)
#     rata2 = jumlahkan/len(args)
#     return jumlahkan

# print(angka(1,2,3,4,5))

# def cetak_id_card(nama_lengkap, **info_tambahan):
#     print(f"=== KARTU IDENTITAS ===")
#     print(f"Nama: {nama_lengkap}")
    
#     # Mencetak semua info tambahan yang dikirim (jika ada)
#     for label, nilai in info_tambahan.items():
#         # Mengubah huruf pertama label menjadi kapital agar rapi
#         print(f"{label.capitalize()}: {nilai}")
        
#     print("========================\n")

# # ==========================================
# # SIMULASI PENGGUNAAN
# # ==========================================

# # 1. Karyawan A hanya punya data dasar dan nomor HP
# cetak_id_card("Budi Santoso", telepon="08123456789")

# # 2. Karyawan B punya data tambahan divisi, hobi, dan status
# cetak_id_card("Siti Rahma", divisi="Marketing", hobi="Membaca", status="Aktif")

# def cetak_laporan_nilai(nama, **nilai):
#     print('\n=====laporan nilai ujian====\n')
#     print(f'nama siswa: {nama}')
#     for kunci, label in nilai.items():
#         print(kunci, label)

# cetak_laporan_nilai(f"afdal ginaya zulham", matematika = 90, algopro = 90)


# for i in range(1,101):
#     print('fathur ganteng')

# while True:
#     try:
#         nama = str(input('masukkan nama: '))

#         if nama == 'afdalginaya':
#             print('ganteng')
#             break
#         elif nama == 'fathur':
#             print('rich')
#             continue

#     except ValueError:
#         print('input tidak boleh angka')

# def nama(orang='fathur'):
#     nama_saya = print(f'nama saya: {orang}')
#     return nama_saya
    

# nama('afdal')

#function = mengembalikan nilai. prosedur = tidak mengembalikan nilai 

# admin_judol = 'ibas'
# nama = input('masukkan nama: ')
# if nama == admin_judol:
#     print('beliau sangat hebat')
# else:
#     print('orang baek')

# passing_score = 80
# def check_pass(score):
#     if score >= passing_score:
#         print('anda lulus')
#     else:
#         print('anda tidak lulus')

# check_pass(55)
while True: 
    try:
        umur = int(input('masukkan umur: '))
        if umur > 12:
            kategori = 'remaja'
        else:
            kategori = 'anak2'

        print(f'umur kamu: {umur}')
        print(f'kamu dikategorikan: {kategori}')

        lanjut = input('apakah ingin lanjut (ya/tidak: )').strip()
        if lanjut == 'ya':
            continue
        elif lanjut == 'tidak':
            break

        
        
    except ValueError:
        print('input harus berupa angka')

print('\n====terima kasih telah berkunjung====\n')