#FEBRIYAN BIOPSA MINANDA
#5210411203

#Class Abstrak
from abc import ABC, abstractmethod
class Bentuk(ABC) :
    @abstractmethod
    def luas(self) :
        return self._sisi * self._sisi
#5210411203_Febriyan
    @abstractmethod
    def keliling(self) :
        return 4 * self._sisi

class Persegi(Bentuk) :
    def __init__(self, sisi) :
        self._sisi = sisi
    def luas(self) :#5210411203_Febriyan
        return self._sisi * self._sisi
    def keliling(self) :
        return 4 * self._sisi 
#5210411203_Febriyan
persegi = Persegi(6)
print(persegi.luas())
print(persegi.keliling())