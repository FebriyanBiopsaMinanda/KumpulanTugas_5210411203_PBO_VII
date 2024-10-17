#KELOMPOK 2
#5210411203_Febriyan Biopsa Minanda
#5210411227_Revy Ravly Sabbathino Sahetapy
#5210411245_Nadia Ashari
#5210411246_Febriana Fatimah Putri

class Kalkulator :
    def __init__(self, x, y) :
        self.a = x
        self.b = y  #Kelompok 2

class Tambah(Kalkulator) :
    def __init__(self, x, y):
        super().__init__(x, y)

    def tambah(self) :
        print("\nHASIL PENJUMLAHAN\n=======================")
        self.hasil = self.a + self.b    #Kelompok 2
        print(f"{x} + {y} = {self.hasil}")
        print("=======================")

class Kurang(Kalkulator) :
    def __init__(self, x, y):
        super().__init__(x, y)

    def kurang(self) :
        print("\nHASIL PENGURANGAN\n=======================")
        self.hasil = self.a - self.b
        print(f"{x} - {y} = {self.hasil}")  #Kelompok 2
        print("=======================")


class Kali(Kalkulator) :
    def __init__(self, x, y):
        super().__init__(x, y)

    def kali(self) :
        print("\nHASIL PERKALIAN\n=======================")
        self.hasil = self.a * self.b    #Kelompok 2
        print(f"{x} x {y} = {self.hasil}")
        print("=======================")
        #Kelompok 2

class Bagi(Kalkulator) :
    def __init__(self, x, y):
        super().__init__(x, y)

    def bagi(self) :
        print("\nHASIL PEMBAGIAN\n=======================")
        if self.b == 0 :
            print("Erorr (Pembagian dengan nol")
        else :  #Kelompok 2
            self.hasil = self.a / self.b
            print(f"{x} / {y} = {self.hasil}")
        print("=======================")

while True :#Kelompok 2
    print("=======================\n    PILIHAN MENU \n=======================")
    print("1. Tambah ")  
    print("2. Kurang")
    print("3. Kali")    #Kelompok 2
    print("4. Bagi")
    print("0. selesai")
    menu = input("Pilihan Menu : ")
    print("=======================") 

    if menu == '1' :    #Kelompok 2
        print("\nPENJUMLAHAN\n=======================")
        x = int(input("Masukan Angka A : "))
        y = int(input("Masukan Angka B : "))
        object = Tambah(x, y)
        object.tambah() #Kelompok 2

    elif menu == '2' :        
        print("\nPENGURANGAN\n=======================")
        x = int(input("Masukan Angka A : "))
        y = int(input("Masukan Angka B : "))
        object = Kurang(x, y)   #Kelompok 2
        object.kurang()

    elif menu == '3' :    #Kelompok 2
        print("\nPERKALIAN\n=======================")            
        x = int(input("Masukan Angka A : "))
        y = int(input("Masukan Angka B : "))
        object = Kali(x, y)
        object.kali()   #Kelompok 2

    elif menu == '4' :  
        print("\nPEMBAGIAN\n=======================")              
        x = int(input("Masukan Angka A : "))
        y = int(input("Masukan Angka B : "))
        object = Bagi(x, y)
        object.bagi()   #Kelompok 2

    elif menu == '0':
        print("\nTerima Kasih :)\n")
        break   #Kelompok 2

    else :  #Kelompok 2
        print("\nPilihan Tidak Ada Di Menu \n")
    input("\nEnter Untuk Melanjutkan.....")