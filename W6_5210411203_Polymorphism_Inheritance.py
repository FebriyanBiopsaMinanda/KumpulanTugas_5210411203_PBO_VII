#FEBRIYAN BIOPSA MINANDA
#5210411203

#Polymorphism dengan Inheritance
class Burung :
    def intro(self) :
        print("Di dunia ini ada beberapa type berbeda dari spesies burung")
            #5210411203_Febriyan
    def terbang(self) :
        print("Hampir semua burung dapat terbang, namun ada beberapa yang tidak bisa terbang")

class Elang(Burung) :#5210411203_Febriyan
    def terbang(self):
        print("Elang dapat terbang")

class BurngUnta(Burung) :
    def terbang(self):#5210411203_Febriyan
        print("Burung unta tidak dapat terbang")

obj_burung = Burung()
obj_elang = Elang()
obj_burung_unta = BurngUnta()
#5210411203_Febriyan
obj_burung.intro()
obj_burung.terbang()

obj_elang.intro()
obj_elang.terbang()
#5210411203_Febriyan
obj_burung_unta.intro()
obj_burung_unta.terbang()