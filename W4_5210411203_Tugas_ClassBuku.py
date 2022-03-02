#FEBRIYAN BIOPSA MINANDA
#5210411203
class Buku :
    def __init__(self, judul, pengarang, tahun_terbit, jmlh_halaman) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit        #5210411203_Febriyan
        self.__jmlh_halaman = jmlh_halaman

    def Tampil(self) :
        print(f"Buku {self.judul} karangan {self.pengarang} pertama kali diterbitkan tahun {self.tahun_terbit}")
        print(f"Buku {self.judul} jumlah halamannya adalah {self.__jmlh_halaman}\n")

buku1 = Buku("Sang pemimpi", "Andrea Hirata", 2006, 292)
buku2 = Buku("Sebuah seni untuk bersikap bodo amat", "Mark Manson", 2018, 246)
buku3 = Buku("Kamu terlalu banyak bercanda", "Marchella FP", 2019, 194)

kumpulan_buku = [buku1, buku2, buku3]
print("\n\tList Buku\n================================")
for buku in kumpulan_buku :     #5210411203_Febriyan
     buku.Tampil()
print("\n")