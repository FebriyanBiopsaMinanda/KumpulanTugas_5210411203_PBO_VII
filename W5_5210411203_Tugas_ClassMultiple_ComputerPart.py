#FEBRIYAN BIOPSA MINANDA
#5210411203

#Multiple Inheritance
def rupiah(uang) :
    x = str(uang)
    if len(x) <= 3 :
        return "Rp." + x
    else :
        a = x[:-3]
        b = x[-3:]      #5210411203_Febriyan
        return rupiah(a) + '.' + b
    
class ComputerPart1():
    def __init__(self, pabrikan, nama) :
        self.pabrikan = pabrikan
        self.nama = nama

class ComputerPart2() : #5210411203_Febriyan
    def __init__(self, harga) :
        self.harga = harga

class Processor(ComputerPart1, ComputerPart2) :
    def __init__(self, pabrikan, nama, harga) :
        ComputerPart1.__init__(self, pabrikan, nama)
        ComputerPart2.__init__(self, harga)
        
    def Tampil(self) :      #5210411203_Febriyan
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga : {rupiah(self.harga)}")

class RandomAccessMemory(ComputerPart1, ComputerPart2) :
    def __init__(self, pabrikan, nama, harga) :
        ComputerPart1.__init__(self, pabrikan, nama)
        ComputerPart2.__init__(self, harga)

    def Tampil(self) :
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga : {rupiah(self.harga)}")

class HardDiskSATA(ComputerPart1, ComputerPart2) :
    def __init__(self, pabrikan, nama, harga) :
        ComputerPart1.__init__(self, pabrikan, nama)
        ComputerPart2.__init__(self, harga)

    def Tampil(self) :  #5210411203_Febriyan
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga : {rupiah(self.harga)}")

p = Processor('Intel', "Core i7 7740X", 4350000)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000)
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000)

parts = [p, ram, hdd]   #5210411203_Febriyan
print("\n\t\t\tMULTIPLE COMPUTER PART")
print("=================================================================================")
for part in parts :
    part.Tampil()
    print("")   #5210411203_Febriyan
print("=================================================================================\n")