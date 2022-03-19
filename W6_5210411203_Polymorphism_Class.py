#FEBRIYAN BIOPSA MINANDA
#5210411203

#Polymorphism dengan Class
class kucing :
    def __init__(self, nama, umur) :
        self.nama = nama
        self.umur = umur
    #5210411203_Febriyan
    def bersuara(self) :
        print("Meow")

class dog :#5210411203_Febriyan
    def __init__(self, nama, umur) :
        self.nama = nama
        self.umur = umur
    #5210411203_Febriyan
    def bersuara(self) :
        print("Guk...Guk...")

kucing1 = kucing("Tom", 3)
anjing1 = dog("Spike", 4)
#5210411203_Febriyan
for hewan in (kucing1, anjing1) :
    hewan.bersuara()