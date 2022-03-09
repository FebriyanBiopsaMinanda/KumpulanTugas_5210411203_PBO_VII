#FEBRIYAN BIOPSA MINANDA
#5210411203

# Single Inheritance

#Parent Class
class Hewan :   #5210411203_Febriyan
    def bersuara(self) :
        print("Kucing Bersuara")

# Anak class mewarisi parent class
class Kucing(Hewan) :
    def suara(self) :
        print("meong...meong")
#5210411203_Febriyan

#Objek
cat = Kucing()
cat.suara()#5210411203_Febriyan
cat.bersuara()
#5210411203_Febriyan