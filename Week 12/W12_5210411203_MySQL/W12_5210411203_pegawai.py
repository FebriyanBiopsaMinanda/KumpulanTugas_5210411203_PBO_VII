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

#sql = (f"CREATE TABLE pegawai (nip VARCHAR(20), nama_pegawai VARCHAR(40), kode_jabatan VARCHAR(3), kode_golongan VARCHAR(3), status VARCHAR(15), jumlah_anak INT(2))")
#cur.execute(sql)
#cur.close()
#connect.close()

# SELECT ALL
def select() :#5210411203_FEBRIYAN
    try :
        sql = f"SELECT * FROM pegawai"
        cur.execute(sql)
        print(f"\nData Pegawai")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Nama Pegawai\t: {x[1]}")
            print(f"NIP\t\t: {x[0]}")
            print(f"Kode Jabatan\t: {x[2]}")
            print(f"Kode Golongan\t: {x[3]}")
            print(f"Status\t\t: {x[4]}")
            print(f"Jumlah Anak\t: {x[5]}")
        print("==============================================\n\n")
        kembali()
    except :#5210411203_FEBRIYAN
        print("\nEror")
        kembali()

# SELECT ONE
def search(nip) :
    try :
        sql = cur.execute(f"SELECT * FROM pegawai  WHERE nip LIKE '%{nip}%'")
        cur.execute(sql)#5210411203_FEBRIYAN
        print(f"\nHasil Pencarian Dari {nip}")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Nama Pegawai\t: {x[1]}")
            print(f"NIP\t\t: {x[0]}")
            print(f"Kode Jabatan\t: {x[2]}")
            print(f"Kode Golongan\t: {x[3]}")
            print(f"Status\t\t: {x[4]}")
            print(f"Jumlah Anak\t: {x[5]}") 
        print("==============================================\n\n")
        kembali()#5210411203_FEBRIYAN
    except :
        print("\nEror")
        kembali()

# INSERT
def insert() :
    try :
        nip = input("Masukan NIP\t\t: ")
        nm_pegawai = input("Masukan Nama Pegawai\t: ")
        kd_jabatan = input("Masukan Kode Jabatan\t: ")
        kd_golongan = input("Masukan Kode Golongan\t: ")
        status = input("Masukan Status\t\t: ")#5210411203_FEBRIYAN
        jmlh_anak = int(input("Masukan Jumlah Anak\t: "))
        sql = ("INSERT INTO pegawai (nip, nama_pegawai, kode_jabatan, kode_golongan, status, jumlah_anak) VALUES (%s,%s,%s,%s,%s,%s)")
        data = (nip, nm_pegawai, kd_jabatan, kd_golongan, status, jmlh_anak)
        cur.execute(sql,data)
        connect.commit()
        print ("\nData Berhasil Di Tambahkan")
        kembali()
    except :
        print ("\nEror / Data Tidak Berhasil Di Tambahkan")
        kembali()

# UPDATE
def update(nip):
    cur.execute(f"SELECT * FROM pegawai WHERE nip LIKE '%{nip}%'")
    try :
        for x in cur.fetchall() :#5210411203_FEBRIYAN
            if nip in x[0] :
                print("\n==============================================")
                kd_golongan = input("Masukan Kode Golongan baru\t: ")
                status = input("Masukan Status Baru\t\t: ")
                jmlh_anak = int(input("Masukan Jumlah Anak Baru\t: "))
                sql = ("UPDATE pegawai SET kode_golongan = %s, status = %s, jumlah_anak = %s WHERE nip LIKE %s")
                data = (kd_golongan, status, jmlh_anak, nip)
                cur.execute(sql, data)
                connect.commit()#5210411203_FEBRIYAN
                print(f"\nNIP {nip} Berhasil Di Edit")
                print("==============================================")
                print(f"Nama Pegawai\t: {x[1]}")
                print(f"NIP\t\t: {x[0]}")
                print(f"Kode Jabatan\t: {x[2]}")
                print(f"Kode Golongan\t: {kd_golongan}")
                print(f"Status\t\t: {status}")
                print(f"Jumlah Anak\t: {jmlh_anak}") #5210411203_FEBRIYAN
                print("==============================================\n\n")
                kembali()
    except :
        print("\nData Tidak Berhasil Di Edit")
        kembali()

# DELETE
def delete(nip):#5210411203_FEBRIYAN
    cur.execute(f"SELECT * FROM pegawai  WHERE nip LIKE '%{nip}%'")
    try :
        for x in cur.fetchall() :
            if nip in x[0] :
                cur.execute(f"DELETE FROM pegawai WHERE nip LIKE '%{nip}%'")
                connect.commit()
                print(f"\nNIP {nip} Berhasil Di Hapus")
                kembali()
    except :#5210411203_FEBRIYAN
        print("Data Tidak Berhasil Di Hapus")
        kembali()

while True :
    clear_screen()
    print("=======================\n    Menu MySQL \n=======================")
    print("1. Tampil Pegawai")
    print("2. Tambah Pegawai")
    print("3. Cari Pegawai")
    print("4. Edit Pegawai")
    print("5. Hapus Pegawai")
    print("0. Selesai")#5210411203_FEBRIYAN
    pilihan = input("Masukan Pilihan : ")

    if pilihan == '1' :
        select()
    elif pilihan == '2' :
        insert()
    elif pilihan == '3' :#5210411203_FEBRIYAN
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
        )
    elif pilihan == '0' :
        clear_screen()
        break#5210411203_FEBRIYAN