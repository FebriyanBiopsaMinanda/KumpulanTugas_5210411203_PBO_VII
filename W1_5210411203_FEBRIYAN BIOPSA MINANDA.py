#FEBRIYAN BIOPSA MINANDA 
#5210411203
def luas_permukaan(r, t) :
    Lpermukaan = 2*3.14*r*(r+t)
    return Lpermukaan

def volume(r, t) :
    Volume = 3.14*r*r*t
    return Volume

print("==========================\n\t TABUNG \n==========================\n")
r = float(input("Masukan Jari-jari\t: "))
t = float(input("Masukan Tinggi\t\t: "))

print(f"\nLuas Permukaan Tabung = {luas_permukaan(r,t)}")
print(f"Volume Tabung = {volume(r,t)}")