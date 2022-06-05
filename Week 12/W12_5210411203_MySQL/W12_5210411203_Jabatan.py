#NAMA : FEBRIYAN BIOPSA MINANDA
#NIM  : 5210411203

import mysql.connector
import os

connect = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "week12pbo"
)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def kembali():#5210411203_FEBRIYAN
    print("\n")
    input("Tekan tombol enter untuk kembali...")
    clear_screen()

cur = connect.cursor()

#CREATE TABLE

#sql = (f"CREATE TABLE jabatan (kode_jabatan VARCHAR(3), nama_jabatan VARCHAR(30), gapok INT(10), tunjangan_jabatan INT(10))")
#cur.execute(sql)
#cur.close()
#connect.close()

# SELECT ALL
def select() :
    try :
        sql = f"SELECT * FROM jabatan"
        cur.execute(sql)#5210411203_FEBRIYAN
        print(f"\nData Jabatan")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Kode Jabatan      : {x[0]}")
            print(f"Nama Jabatan      : {x[1]}")
            print(f"Gapok             : {x[2]}")
            print(f"Tunjangan Jabatan : {x[3]}\n") 
        print("==============================================\n\n")
        kembali()
    except :#5210411203_FEBRIYAN
        print("\nEror")
        kembali()
    

# SELECT ONE
def search(kd_jabatan) :
    try :
        sql = cur.execute(f"SELECT * FROM jabatan  WHERE kode_jabatan LIKE '%{kd_jabatan}%'")
        cur.execute(sql)
        print(f"\nHasil Pencarian Dari {kd_jabatan}")#5210411203_FEBRIYAN
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Kode Jabatan      : {x[0]}")
            print(f"Nama Jabatan      : {x[1]}")
            print(f"Gapok             : {x[2]}")
            print(f"Tunjangan Jabatan : {x[3]}\n") 
        print("==============================================\n\n")
        kembali()
    except :
        print("\nEror")#5210411203_FEBRIYAN
        kembali()

# INSERT
def insert() :
    try :
        kd_jabatan = input("Masukan Kode Jabatan : ")
        nm_jabatan = input("Masukan Nama Jabatan : ")
        gpk = int(input("Masukan Gapok : "))
        tnj_jabatan = int(input("Masukan Tunjangan Jabatan : "))
        sql = ("INSERT INTO jabatan (kode_jabatan , nama_jabatan , gapok, tunjangan_jabatan) VALUES (%s,%s,%s,%s)")
        data = ( kd_jabatan, nm_jabatan, gpk, tnj_jabatan)
        cur.execute(sql,data)#5210411203_FEBRIYAN
        connect.commit()
        print ("\nData Berhasil Di Tambahkan")
        kembali()
    except :
        print ("\nEror / Data Tidak Berhasil Di Tambahkan")
        kembali()

# UPDATE
def update(kd_jabatan):
        cur.execute(f"SELECT * FROM jabatan WHERE kode_jabatan LIKE '%{kd_jabatan}%'")
        try :#5210411203_FEBRIYAN
            for x in cur.fetchall() :
                if kd_jabatan in x[0] :
                    print("\n==============================================")
                    gpk = int(input("Masukan Gapok Baru\t: "))
                    tnj_jabatan = int(input("Masukan Tunjangan Baru\t: "))
                    sql = ("UPDATE jabatan SET gapok = %s, tunjangan_jabatan = %s WHERE kode_jabatan LIKE %s")
                    data = (gpk, tnj_jabatan, kd_jabatan)
                    cur.execute(sql, data)#5210411203_FEBRIYAN
                    connect.commit()
                    print(f"\nKode {kd_jabatan} Berhasil Di Edit")
                    print("==============================================")
                    print(f"Nama Jabatan\t\t: {x[1]}")
                    print(f"Gapok\t\t\t: {gpk}")  
                    print(f"Tunjangan Jabatan\t: {tnj_jabatan}")
                    print("==============================================\n\n")
                    kembali()
        except :#5210411203_FEBRIYAN
            print("\nData Tidak Berhasil Di Edit")
            kembali()

# DELETE
def delete(kd_jabatan):
    cur.execute(f"SELECT * FROM jabatan  WHERE kode_jabatan LIKE '%{kd_jabatan}%'")
    try :
        for x in cur.fetchall() :#5210411203_FEBRIYAN
            if kd_jabatan in x[0] :
                cur.execute(f"DELETE FROM jabatan WHERE kode_jabatan LIKE '%{kd_jabatan}%'")
                connect.commit()
                print(f"\n Kode {kd_jabatan} Berhasil Di Hapus")
                kembali()
    except :
        print("Data Tidak Berhasil Di Hapus")
        kembali()#5210411203_FEBRIYAN

while True :
    clear_screen()
    print("=======================\n    Menu MySQL \n=======================")
    print("1. Tampil Jabatan")
    print("2. Tambah Jabatan")
    print("3. Cari Jabatan")
    print("4. Edit Jabatan")
    print("5. Hapus Jabatan")
    print("0. Selesai")#5210411203_FEBRIYAN
    pilihan = input("Masukan Pilihan : ")

    if pilihan == '1' :
        select()
    elif pilihan == '2' :
        insert()#5210411203_FEBRIYAN
    elif pilihan == '3' :
        search(
            kd_jabatan = input("Masukan Kode Jabatan : ")
        )
    elif pilihan == '4' :
        update(
            kd_jabatan = input("Masukan Kode Jabatan yg Ingin Di Ubah : ")
        )
    elif pilihan == '5' :
        delete(#5210411203_FEBRIYAN
            kd_jabatan = input("Masukan Kode Jabatan yg Ingin Di Hapus : ")
        )
    elif pilihan == '0' :
        clear_screen()
        break#5210411203_FEBRIYAN