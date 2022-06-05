#NAMA : FEBRIYAN BIOPSA MINANDA
#NIM  : 5210411203

import mysql.connector
import os

connect = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "" , #5210411203_FEBRIYAN
    database = "week12pbo"
)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    #5210411203_FEBRIYAN
def kembali():
    print("\n")
    input("Tekan tombol enter untuk kembali...")
    clear_screen()
cur = connect.cursor()

#5210411203_FEBRIYAN

#CREATE TABLE

#sql = (f"CREATE TABLE gaji (bulan VARCHAR(20), nip VARCHAR(20), masuk INT(5), sakit INT(5), izin INT(5), alfa INT(5), lembur INT(5), potongan INT(10))")
#cur.execute(sql)
#cur.close()
#connect.close()

# SELECT ALL
def select() :
    try :#5210411203_FEBRIYAN
        sql = f"SELECT * FROM gaji"
        cur.execute(sql)
        print(f"\nData Gaji")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Bulan {x[0]}\t Nip {x[1]}")
            print(f"Masuk    : {x[2]}")
            print(f"Sakit    : {x[3]}")
            print(f"Izin     : {x[4]}")#5210411203_FEBRIYAN
            print(f"Alfa     : {x[5]}")
            print(f"Lembur   : {x[6]}")
            print(f"Potongan : {x[7]}\n") 
        print("==============================================\n\n")
        kembali()#5210411203_FEBRIYAN
    except :
        print("\nEror")
        kembali()#5210411203_FEBRIYAN

# SELECT ONE
def search(nip) :
    try :#5210411203_FEBRIYAN
        sql = cur.execute(f"SELECT * FROM gaji  WHERE nip LIKE '%{nip}%'")
        cur.execute(sql)
        print(f"\nHasil Pencarian Dari {nip}")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Bulan {x[0]}\t Nip {x[1]}")
            print(f"Masuk    : {x[2]}")
            print(f"Sakit    : {x[3]}")
            print(f"Izin     : {x[4]}")
            print(f"Alfa     : {x[5]}")
            print(f"Lembur   : {x[6]}")#5210411203_FEBRIYAN
            print(f"Potongan : {x[7]}\n")  
        print("==============================================\n\n")
        kembali()
    except :#5210411203_FEBRIYAN
        print("\nEror")
        kembali()

# INSERT
def insert() :
    try :
        bulan = input("Masukan Bulan\t\t: ")
        nip = input("Masukan NIP\t\t: ")
        masuk = int(input("Masukan Kehadiran\t: "))
        sakit = int(input("Masukan Data Sakit\t: "))
        izin = int(input("Masukan Data Izin\t: "))
        alfa = int(input("Masukan Data Alfa\t: "))
        lembur = int(input("Masukan Data Lembur\t: "))#5210411203_FEBRIYAN
        potongan = int(input("Masukan Potongan\t: "))
        sql = ("INSERT INTO gaji (bulan, nip, masuk, sakit, izin, alfa, lembur, potongan) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
        data = (bulan, nip, masuk, sakit, izin, alfa, lembur, potongan)
        cur.execute(sql,data)
        connect.commit()#5210411203_FEBRIYAN
        print ("\nData Berhasil Di Tambahkan")
        kembali()
    except :
        print ("\nEror / Data Tidak Berhasil Di Tambahkan")
        kembali()#5210411203_FEBRIYAN

# UPDATE
def update(nip):
    cur.execute(f"SELECT * FROM gaji WHERE nip LIKE '%{nip}%'")
    try :#5210411203_FEBRIYAN
        for x in cur.fetchall() :
            if nip in x[1] :
                print("\n==============================================")
                masuk = int(input("Masukan Kehadiran\t: "))
                sakit = int(input("Masukan Data Sakit\t: "))
                izin = int(input("Masukan Data Izin\t: "))
                alfa = int(input("Masukan Data Alfa\t: "))
                lembur = int(input("Masukan Data Lembur\t: "))#5210411203_FEBRIYAN
                potongan = int(input("Masukan Potongan\t: "))
                sql = ("UPDATE gaji SET masuk = %s, sakit = %s, izin = %s, alfa = %s, lembur = %s, potongan = %s WHERE nip LIKE %s")
                data = (masuk, sakit, izin, alfa, lembur, potongan, nip)
                cur.execute(sql, data)
                connect.commit()#5210411203_FEBRIYAN
                print(f"\nNIP {nip} Berhasil Di Edit")
                print("==============================================")
                print(f"Bulan {x[0]}\t Nip {x[1]}")
                print(f"Masuk   : {masuk}")
                print(f"Sakit   : {sakit}")
                print(f"Izin    : {izin}")
                print(f"Alfa    : {alfa}")
                print(f"Lembur  : {lembur}")#5210411203_FEBRIYAN
                print(f"Potongan : {potongan}\n")
                print("==============================================\n\n")
                kembali()
    except :#5210411203_FEBRIYAN
        print("\nData Tidak Berhasil Di Edit")
        kembali()

# DELETE
def delete(nip):
    cur.execute(f"SELECT * FROM gaji  WHERE nip LIKE '%{nip}%'")
    try :#5210411203_FEBRIYAN
        for x in cur.fetchall() :
            if nip in x[1] :
                cur.execute(f"DELETE FROM gaji WHERE nip LIKE '%{nip}%'")
                connect.commit()
                print(f"\nNIP {nip} Berhasil Di Hapus")
                kembali()
    except :
        print("Data Tidak Berhasil Di Hapus")
        kembali()
#5210411203_FEBRIYAN
while True :
    clear_screen()
    print("=======================\n    Menu MySQL \n=======================")
    print("1. Tampil Gaji")
    print("2. Tambah Gaji")
    print("3. Cari Gaji")
    print("4. Edit Gaji")
    print("5. Hapus Gaji")
    print("0. Selesai")
    pilihan = input("Masukan Pilihan : ")
#5210411203_FEBRIYAN
    if pilihan == '1' :
        select()
    elif pilihan == '2' :#5210411203_FEBRIYAN
        insert()
    elif pilihan == '3' :
        search(
            nip = input("Masukan NIP : ")
        )
    elif pilihan == '4' :
        update(
            nip = input("Masukan NIP yg Ingin Di Ubah : ")
        )#5210411203_FEBRIYAN
    elif pilihan == '5' :
        delete(
            nip = input("Masukan NIP yg Ingin Di Hapus : ")
        )#5210411203_FEBRIYAN
    elif pilihan == '0' :
        clear_screen()
        break#5210411203_FEBRIYAN