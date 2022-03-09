#FEBRIYAN BIOPSA MINANDA
#5210411203

#Hierarchial Inheritance
class Mahasiswa() :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
#5210411203_Febriyan
class Siswa1(Mahasiswa) :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
        #5210411203_Febriyan
    def detSiswa1(self) :
        print(self.nama, "Alamat : Wall Rose")

class Siswa2(Mahasiswa) :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim  #5210411203_Febriyan

    def detSiswa2(self) :
        print(self.nama, "Jurusan : Informatika")

mahasiswa1 = Siswa1("Mikasa", 135105)
mahasiswa2 = Siswa2("Nezuko", 135117)

print(mahasiswa1.nim)   #5210411203_Febriyan
mahasiswa1.detSiswa1()
print(mahasiswa2.nim)
mahasiswa2.detSiswa2()
#5210411203_Febriyan