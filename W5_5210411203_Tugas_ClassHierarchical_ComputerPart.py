#FEBRIYAN BIOPSA MINANDA
#5210411203

#Hierarchical Inheritance
def rupiah(uang) :
    x = str(uang)
    if len(x) <= 3 :
        return "Rp." + x
    else :  #5210411203_Febriyan
        a = x[:-3]
        b = x[-3:]
        return rupiah(a) + '.' + b
    
class ComputerPart:
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama    #5210411203_Febriyan
        self.harga = harga

class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        
    def Tampil(self) :  #5210411203_Febriyan
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga : {rupiah(self.harga)}")

class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas) :
        self.pabrikan = pabrikan
        self.nama = nama #5210411203_Febriyan
        self.harga = harga
        self.kapasitas = kapasitas

    def Tampil(self) :  #5210411203_Febriyan
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"Harga : {rupiah(self.harga)}")

class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        self.kapasitas = kapasitas
        self.rpm = rpm
#5210411203_Febriyan
    def Tampil(self) :
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"RPM : {self.rpm}")
        print(f"Harga : {rupiah(self.harga)}")
#5210411203_Febriyan
p = Processor('Intel', 'Core i7 7740X', 4350000)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, "4GB")
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)

parts = [p, ram, hdd]   #5210411203_Febriyan
print("\n\t\t\tHIERARCHIAL COMPUTER PART")
print("=================================================================================")
for part in parts :
    part.Tampil()
    print("")   #5210411203_Febriyan
print("=================================================================================\n")