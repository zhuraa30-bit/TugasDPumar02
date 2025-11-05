# TOKO MAINAN ANAK
NAMA = input("Masukkan nama pembeli: ")
Barang = input("Masukkan kode mainan: ")
Harga = int(input("Masukkan harga: "))
Jumlah = int(input("Masukkan jumlah: "))

total = Harga * Jumlah

print("=============================================")
print("Nama pembeli: ", NAMA)
print("Kode kue : ", Barang)
print("Harga: ", Harga)
print("Jumlah Barang:", Jumlah)
print("Total :", total)

var1 = 'hello python!'
var2 = var1[:6]
print(var1)
print("String update: ", var1[:6] + 'world')

#KARAKTER ESCAPE

print('''He said, "What's there?"''')
print('He said, "what\'s there?\"')
print("He said, \"What's there?\"")

#MENGETAHUI PANJANG STRING 
string = 'i love python'
print(len(string))

#MENGGABUNG STRING

str1 = 'hello'
str2 = 'python'
print('str1 + str2 =', str1+ str2)
print('str1 * 3 = ', str1 * 3)

#STRING

var1 = 'hello python'
var2 = "progamming with python"
print (var1)
print (var2)

#MENGAKSES NILAI STRING

var1 = 'hello python'
var2 = "i love python"
print("var1[0]", var1[0])
print("var2[0]", var2[0])

#MENGUPDATE NILAI STRING

var1 = "talon ajg"
print(var1)
print("String Update: ", var1[:6] + 'baik')

#MENGATUR FORMAT STRING
#1.default
default_order = "{}, {}, {}". format("budi", "galih", "ratna")
print('\n---urutan default---')
print(default_order)

#2.argument position
positional_order = "{2}, {0}, {1}". format("budi", "galih", "ratna")
print('\n---argument position---')
print(positional_order)

#METODE FORMAT

#FORMAT INTEGER
print("{0} bila diubah menjadi biner menjadi {0:b}".format(12))

