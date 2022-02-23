str = "aku cinta Indonesia"
print(str)

str = str[:10] + "tanah air ku" + str[9:]
print(str)

str = " "
print(str)

str1 = "aku cinta tanah air ku Indonesia"
str1 = str1[:9] + "" + str1[22:]
print(str1)

kelas = "Praktikum pemrograman berorientasi objek"
up = kelas.upper()
low = kelas.lower()
print(kelas)
print(up)
print(low)

s = "     Python     "
strip = s.strip()
lstrip= s.lstrip()
rsrtip = s.rstrip()
print(s)
print(lstrip)
print(rsrtip)

jumlah = len(kelas)
print(f"Jumlah string adalah : {jumlah}")

s1 = "Python "
s2 = "Programming"
s3 = s1 + s2
print(s3)

print(kelas.index("a"))

kelas2 = kelas.replace("Praktikum", "praktik")
print(kelas2)

a = "satu"
b = "dua"
c = "tiga"
print("saya mempunyai %s mangga"%(c))

split = kelas2.split()
print(split)

input = input("Hari ini adalah : ")
print(input)

data1 = int(input("Masukan Angka 1 : "))
data2 = int(input("Masukan Angka 2 : "))
hasil = data1 * data2
print(f"{data1} x {data2} = {hasil}")

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list[0])
print(list[5])
print(list[:3])
print(len(list))
print(list[10-3:])
print(list[2:9])
print(list[-10])

list.append(10)
print(list)
list.insert(1,11)
print(list)

list2 = ["hallo"]
list.extend(list2)
print(list)

list.extend("hai")
print(list)

del list[1]
print(list)

list.remove(10)
print(list)

list.pop()
print(list)

list.pop(2)
print(list)

list2 = [50, 10, 20, 30, 40]
lista = sorted(list2)
print(lista)

list2.sort(reverse=True)
print(list2)

print(max(list2))
print(min(list2))

dictionary = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
print(dictionary)
print(dictionary[2])
print(dictionary.get(4))
print(dictionary.keys())
print(dictionary.values())

del dictionary[1]
print(dictionary)

baru = dictionary.copy()
print(baru)

dictionary.clear()
print(dictionary)

tupel = (100, 200, 300, 400)
print(tupel)
print(tupel[0])
print(tupel[3])
print(tupel.index(200))

tupel2 = (10, 20, 10, 30, 10, 40, 20)
print(tupel2.count(20))
print(tupel2.count(10))
print(tupel2.count(30))