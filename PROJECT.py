#soal nomer 1
def mean():
    angka = map(float,input("masukkan angka pakai spasi : ").split()) 
    total = 0
    jumlah = 0
    for num in(angka):
        total += num
        jumlah += 1
    return total/jumlah 
print(mean()) 

#soal nomer 3
def sort_array(array, pilihan):
    n = 0
    for p in array:
        n += 1
    for i in range(1,n):
        key = array[i]
        j = i - 1
        if pilihan == 1:  # Ascending
            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
        elif pilihan == 2:  # Descending
            while j >= 0 and array[j] < key:
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key
input_data = input("Masukkan angka-angka yang dipisahkan dengan spasi: ")
array = list(map(int, input_data.split())) 
pilihan = int(input("Pilih (1) untuk Ascending dan (2) untuk Descending: "))
print("Sebelum diurutkan:", array)
sort_array(array, pilihan)
print("Sesudah diurutkan:", array) 

#soal nomer 4
def cari_nilai(a,b):
    if a == 0:
        return "nilai a tidak boleh 0"
    x = -b / a
    return x  
a = int(input("masukkan nilai a : "))
b = int(input("masukkan nilai b : "))
hasil = cari_nilai(a,b)
print(hasil) 

#soal nomer 13
def massa_jenis(m,v) :
    rho = m / v 
    print("massa jenis nya adalah", rho)

def kecepatan(s,t) :
    v = s / t 
    print("kecepatannya adalah", v)

print("1. massa jenis")
print("2. kecepatan ")
(pilihan) = int(input("masukkan pilihan anda 1 atau 2 = "))

if (pilihan == 1 ) :
    m = int(input("masukkan nilai m (massa) = "))
    v = int(input("masukkan nilai v (volume) = "))
    massa_jenis(m,v)
elif (pilihan == 2 ) :
    s = int(input("masukkan nilai s (jarak) = "))
    t = int(input("masukkan nilai t (wwaktu) = "))
    kecepatan(s,t)
else :
    print("maaf pilihan anda tidak ada") 


#soal nomer 17
def hitung_percepatan():
    print("mari menghitung kecepatan")
    delta_v_jarak = int(input("masukkan jarak: "))
    delta_t_waktu = int(input("masukkan waktu: "))
    kecepatan = delta_v_jarak / delta_t_waktu
    print("kecepatan= ", kecepatan)

hitung_percepatan()

#soal nomer 19
print(" Teorema Pythagoras mencari c ")
def pythagoras(a, b):
    c = (a ** 2 + b ** 2) ** (0.5)
    print ("nilai c adalah ", c)
   
a = int(input("masukkan nilai a = "))
b = int(input("masukkan nilai b = "))
pythagoras(a, b) 

#soal nomer 22
def persamaan_2variabel(a, b, c, x, y):

    if a * x + b * y == c:
        return "persamaan benar"
    else:
        return "persamaan salah"

a = int(input("masukkan nilai a: "))
b = int(input("masukkan nilai b: "))
c = int(input("masukkan nilai c: "))
x = int(input("masukkan nilai x: "))
y = int(input("masukkan nilai y: "))

result =  persamaan_2variabel(a, b, c, x, y)
print(result)



