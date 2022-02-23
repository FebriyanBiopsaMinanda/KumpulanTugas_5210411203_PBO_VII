#NAMA : FEBRIYAN BIOPSA MINANDA
#NPM : 5210411203

# Membuat Set

#Menggunakan kurung kurawal
siswa = {"Febriyan", "Revy", "William", "Havin"}
print(siswa)

#Mengkonversi list ke dalam set
buah = set(["mangga", "jambu", "apel"])
print(buah)

#Set dengan Tipe data campuran
campuran = {"manusia", 5, True}
print(campuran)

#Fungsi Pada Set
print("\nFUNGSI SET")
set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# menambahkan anggota baru
set.add(10) 
print(f"\nMenambahkan Anggota\n{set}")

#mengcopy anggota
setcopy = set.copy()
print(f"\nMengcopy Anggota\n{setcopy}")

#menghapus anggota

#fungsi discard() tidak akan memunculkan error jika anggota yang ingin dihapus tidak ada di dalam set
set.discard(0) 
print(f"\nMenghapus Anggota\n{set}")
#sedangkan remove() sebaliknya.
set.remove(9)
print(set)
#fungsi clear() untuk menghapus keseluruhan anggota
setcopy.clear()
print(f"{setcopy}\n")

#Operasi Set
print("\nOPERASI SET")
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9}

#Gabungan
#Operasi gabungan bisa menggunakan fungsi union() atau menggunakan operator palang (|)
print(f"\nGabungan\n{a|b}")
gabungan = a.union(b)
print(gabungan)

#Irisan
#Operasi irisan bisa menggunakan fungsi intersection() atau menggunakan operator jangkar (&)
print(f"\nIrisan\n{a&b}")
irisan = a.intersection(b)
print(irisan)

#Selisih
#Operasi selisih bisa menggunakan fungsi difference() atau menggunakan operator kurang (-)
print(f"\nSelisih\n{a-b}")
selisih = a.difference(b)
print(selisih)

#Komplemen
#Operasi komplemen bisa menggunakan fungsi symmetric_difference() atau menggunakan operator pangkat (^)
print(f"\nKomplemen\n{a^b}")
komplemen = a.symmetric_difference(b)
print(komplemen)