#FEBRIYAN BIOPSA MINANDA
#5210411203

#Implementasi Overriding Class Mahasiswa
class Mahasiswa :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
#5210411203_Febriyan
    def tampil(self) :
        print(f"Nama\t\t: {self.nama} \nNim \t\t: {self.nim}\n")

class Hitung(Mahasiswa) :#5210411203_Febriyan
    def __init__(self, nama, nim, jmlhsks, sks) :
        super().__init__(nama, nim)
        self.jmlhsks = jmlhsks
        self.sks = sks
        #5210411203_Febriyan

    #Override Method
    def tampil(self):
        totalsks = self.jmlhsks + self.sks

        if totalsks>=100 :#5210411203_Febriyan
            print(f"Nama\t\t: {self.nama} \nNim \t\t: {self.nim}")
            print(f"Total Sks\t: {totalsks}")
            print("Diperbolehkan mengambil skripsi\n")
        else :
            print(f"Nama\t\t: {self.nama} \nNim \t\t: {self.nim}")
            print(f"Total Sks\t: {totalsks}")
            print("Tidak diperbolehkan mengambil skripsi\n")
        #5210411203_Febriyan
mahasiswa1 = Mahasiswa("Eren", 123180015)
mahasiswa2 = Hitung("Mikasa", 123190007, 84, 22)
#5210411203_Febriyan
mahasiswa1.tampil()
mahasiswa2.tampil()
#5210411203_Febriyan