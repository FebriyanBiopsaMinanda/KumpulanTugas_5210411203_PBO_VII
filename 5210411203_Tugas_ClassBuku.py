#FEBRIYAN BIOPSA MINANDA
#5210411203
class Buku :
    def __init__(self, judul, pengarang, tahun_terbit) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit        #5210411203_Febriyan

buku1 = Buku("Sang pemimpi", "Andrea Hirata", 2006)
buku2 = Buku("Sebuah seni untuk bersikap bodo amat", "Mark Manson", 2018)
buku3 = Buku("Kamu terlalu banyak bercanda", "Marchella FP", 2019)

kumpulan_buku = [buku1, buku2, buku3]
print("\n\tList Buku\n================================")
for buku in kumpulan_buku :     #5210411203_Febriyan
    teks = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul, buku.pengarang, buku.tahun_terbit)
    print(teks) 
print("\n")