#FEBRIYAN BIOPSA MINANDA
#5210411203

#Multiple Inheritance

#Parent Class 1
class Perhitungan1 :
    def penjumlahan(self, a, b) :
        return a + b

#Parent Class 2
class Perhitungan2 :
    def perkalian(self, a, b) :
        return a * b    #5210411203_Febriyan

#Anak Class
class Hitung(Perhitungan1, Perhitungan2) :
    def pembagian(self, a, b):
        return a / b    #5210411203_Febriyan

#Objek
h = Hitung()    #5210411203_Febriyan
print(h.penjumlahan(20, 20))
print(h.perkalian(5, 4))
print(h.pembagian(6, 12))
#5210411203_Febriyan