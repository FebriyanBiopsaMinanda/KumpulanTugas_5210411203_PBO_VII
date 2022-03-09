#FEBRIYAN BIOPSA MINANDA
#5210411203

class ComputerPart:
    def __init__(self, pabrikan, nama, jenis, harga) :
        self.pabrikan = pabrikan
        self.nama = nama #5210411203_Febriyan
        self.jenis = jenis
        self.harga = harga

class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed) :
        super().__init__(pabrikan, nama, 'processor', harga)
        self.jumlah_core = jumlah_core
        self.speed = speed
#5210411203_Febriyan
class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas) :
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas = kapasitas #5210411203_Febriyan
    
class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm) :
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm  #5210411203_Febriyan

p = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz')
m = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)
#5210411203_Febriyan
parts = [p, m, hdd]
for part in parts :#5210411203_Febriyan
    print('{} {} produksi {}'.format(part.jenis, part.nama, part.pabrikan))