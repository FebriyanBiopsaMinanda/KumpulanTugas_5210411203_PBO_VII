#FEBRIYAN BIOPSA MINANDA
#5210411203

#Multilevel Inheritance

#Parent Class
class Hewan :#5210411203_Febriyan
    def bersuara(self) :
        print("Kucing Bersuara")

#Anak class mewarisi class hewan
class Kucing(Hewan) :
    def suara(self) :   #5210411203_Febriyan
        print("meong...meong")

#Anak class Anakkucing mewarisi dari class hewan
class AnakKucing(Kucing) :
    def minum(self) :   #5210411203_Febriyan
        print("Minum Susu")

#Objek
kitten = AnakKucing()
kitten.bersuara()
kitten.suara()
kitten.minum()
#5210411203_Febriyan