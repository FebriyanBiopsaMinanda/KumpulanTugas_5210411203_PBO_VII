#FEBRIYAN BIOPSA MINANDA
#5210411203
class Menu :
    def __init__(self, nama, deskripsi, harga, stok) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga      #5210411203_Febriyan
        self.__stok = stok

    def Tampil(self) :
        print(f"{self.nama} harga Rp {self.harga} \n---> {self.deskripsi} sisa stok {self.__stok}\n")

minuman1 = Menu("Jus Jambu", "Jus jambu merah tanpa gula", 8500, 10)
minuman2 = Menu("Jus Alpukat", "Jus alpukat dengan gula merah", 15000, 5)
minuman3 = Menu("Jus Alpukat Ektra Milk", "Jus alpukat dengan campuran susu cokelat dan tapuran kepingan choco", 15000, 4)
minuman4 = Menu("Red & Smooth", "Smoothie pisang susu dengan strawberry", 17500, 7)

makanan1 = Menu("Magelangan", "Magelangan dengan telur", 12000, 9)
makanan2 = Menu("Kerang Dara", "Kerang asam manis", 25000, 9)
makanan3 = Menu("Nasi Goreng", "Nasi Goreng dengan telur setengah matang", 8000, 11)
makanan4 = Menu("Ayam Geprek", "Ayam geprek dengan Es Teh", 10000, 5)

pilihan_makanan = [makanan1, makanan2, makanan3, makanan4]
pilihan_minuman = [minuman1, minuman2, minuman3, minuman4]  #5210411203_Febriyan

print("\nDaftar Menu Makanan\n==========================")
for mkn in pilihan_makanan :
    mkn.Tampil()
print("\nDaftar Menu Minuman\n==========================")
for mn in pilihan_minuman :         #5210411203_Febriyan
    mn.Tampil()
print("\n")
