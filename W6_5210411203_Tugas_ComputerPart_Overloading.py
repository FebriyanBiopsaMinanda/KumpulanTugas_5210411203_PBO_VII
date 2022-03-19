#FEBRIYAN BIOPSA MINANDA
#5210411203

#Implementasi Overloading Method pada class Computer Part
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
        print("\nTampil dari sub class Processor")
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga\t\t: {rupiah(self.harga)}")

class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama    #5210411203_Febriyan
        self.harga = harga

    #Overload Method
    def Tampil(self, kapasitas) :  #5210411203_Febriyan
        print("\nTampil dari sub class RandomAccessMemory")
        print(f"{self.nama} produk dari {self.pabrikan}\nKapasitas\t: {kapasitas}")
        print(f"Harga\t\t: {rupiah(self.harga)}")

class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama    #5210411203_Febriyan
        self.harga = harga

    #Overload Method
    def Tampil(self, kapasitas, rpm) :  #5210411203_Febriyan
        print("\nTampil dari sub class HardDiskSATA")
        print(f"{self.nama} produk dari {self.pabrikan}\nKapasitas\t: {kapasitas}")
        print(f"RPM\t\t: {rpm}\nHarga\t\t: {rupiah(self.harga)}")

#5210411203_Febriyan
p = Processor('Intel', 'Core i7 7740X', 4350000)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000)
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000)

print("\n\t\t\tOVERLOADING COMPUTER PART")
print("=================================================================================")
p.Tampil()#5210411203_Febriyan
ram.Tampil("4GB")
hdd.Tampil("500GB", 7200)#5210411203_Febriyan
print("=================================================================================\n")