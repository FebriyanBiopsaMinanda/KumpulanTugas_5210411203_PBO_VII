#FEBRIYAN BIOPSA MINANDA
#5210411203
class Mahasiswa :
    def __init__ (self, nama, nim, prodi, universitas) :
        self.nama = nama
        self.nim = nim      #5210411203_Febriyan
        self.prodi = prodi
        self.__universitas = universitas

    def Tampil(self) :
        print(f"{self.nama} adalah mahasiswa {self.__universitas} prodi {self.prodi} dengan nim {self.nim}")

mahasiswa1 = Mahasiswa("Febriyan", "5210411203", "Informatika", "Universitas Teknologi Yogyakarta")
mahasiswa2 = Mahasiswa("Zidni", "5210411217", "Informatika", "Universitas Teknologi Yogyakarta")
mahasiswa3 = Mahasiswa("Revy", "5210411227", "Informatika", "Universitas Teknologi Yogyakarta")
mahasiswa4 = Mahasiswa("Nadia", "5210411245", "Informatika", "Universitas Teknologi Yogyakarta")

kumpulan_mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("\n\tList Mahasiswa\n================================")
for mhs in kumpulan_mahasiswa :     #5210411203_Febriyan
    mhs.Tampil()
print("\n")