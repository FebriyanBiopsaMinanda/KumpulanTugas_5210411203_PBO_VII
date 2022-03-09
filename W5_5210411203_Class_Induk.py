#FEBRIYAN BIOPSA MINANDA
#5210411203

#Hierarchical Inheritance

#Parent Class
class Induk :
    def fungsiinduk(self) :#5210411203_Febriyan
        print("Fungsi pada parent class.")

#Class turunan 1
class Anak1(Induk) :
    def fungsianak1(self) :
        print("Fungsi pada anak 1.")

#Class turunan 2
class Anak2(Induk) :
    def fungsianak2(self) :#5210411203_Febriyan
        print("Fungsi pada anak 2.")

#Objek
child1 = Anak1()
child2 = Anak2()
#5210411203_Febriyan
child1.fungsiinduk()
child1.fungsianak1()
#5210411203_Febriyan
child2.fungsiinduk()
child2.fungsianak2()
#5210411203_Febriyan