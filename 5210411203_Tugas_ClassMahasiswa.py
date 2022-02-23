#FEBRIYAN BIOPSA MINANDA
#5210411203
class Mahasiswa :
    def __init__ (self, nama, nim, prodi) :
        self.nama = nama
        self.nim = nim      #5210411203_Febriyan
        self.prodi = prodi

mahasiswa1 = Mahasiswa("Febriyan", "5210411203", "Informatika")
mahasiswa2 = Mahasiswa("Zidni", "5210411217", "Informatika")
mahasiswa3 = Mahasiswa("Revy", "5210411227", "Informatika")
mahasiswa4 = Mahasiswa("Nadia", "5210411245", "Informatika")

kumpulan_mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("\n\tList Mahasiswa\n================================")
for mhs in kumpulan_mahasiswa :     #5210411203_Febriyan
    teks = '{} adalah mahasiswa {} dengan nim {}'. format(mhs.nama, mhs.prodi, mhs.nim )
    print(teks)
print("\n")