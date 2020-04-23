def non_return_func(praktikan1, praktikan2):
    print(f"Selamat Datang di Praktikum DKP MOdul 4 {praktikan1} dan {praktikan2}")

non_return_func("Afifa", "Dheyan")



daftar = [["Piring", 10000], ["Gelas", 8000], ["Botol", 5000], ["Wadah Makan", 7000]] 
def daftar_barang():
    print("\nSilahkan memilih barang yang ingin Anda beli \nMasukkan nomor barang, lalu tekan enter") 
    print("-------------------------------------") 
    print(" No | Nama Barang | Harga ") 
    print("-------------------------------------") 
    i = 1 
    for item in daftar: 
        print(str(i) + " | " + item[0] + " | " + str(item[1])) 
        i += 1 
    print("-------------------------------------") 
    print(" 0 | Selesai memilih ") 
    print("-------------------------------------") 
    return 

daftar_barang() 
jawaban = "" 
catatan_pilihan = [] 
while jawaban != "0": 
    jawaban = input("Pilih barang yang akan dibeli ") 
    daftar_barang() 
    if jawaban != "0": 
        catatan_pilihan.append(int(jawaban)-1) 
        
no = 1 
print("Barang yang anda beli : ") 
total = 0 
for pilihan in catatan_pilihan: 
    print("Barang ke-" + str(no) + " = " + daftar[pilihan][0] + " Harga + " + str(daftar[pilihan][1])) 
    no += 1 
    total = total + daftar[pilihan][1] 
    
    print("Total pembayaran " + str(total))

print("\nProgram selesai")