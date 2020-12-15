import time
import mysql.connector
from prettytable import from_db_cursor
from file.header import *
from file.sys import *


#check_width()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cekcok"
)
cursor = db.cursor()

#declare def utk memunculkan daftar makanan
def show_data_makanan():
    header()
    print(" ")
    #menampilkan prettytable dimulai
    cursor.execute("SELECT * FROM list_makanan")
    x = from_db_cursor(cursor)
    print(x)
    print(" ")


#declare def utk memunculkan list promo
def show_data_promo():
    header()
    print(" ")
    #mulai menampilkan prettytable
    cursor.execute("SELECT * FROM list_promo")
    x = from_db_cursor(cursor)
    print(x)
    print(" ")

#declare def utk memunculkan list promo
def show_data_pemesanan():
    header()
    print(" ")
    #mulai menampilkan prettytable
    cursor.execute("SELECT * FROM table_pemesanan")
    x = from_db_cursor(cursor)
    print(x)
    print(" ")


#def utk insert data ke database utk pemesanan
def add_pesanan():
    cursor = db.cursor()
    harga = 0
    disc = 0
    harga_akhir = 0
    show_data_makanan()
    print(" ")
    nama = input("\nMasukan Nama Pembeli : ")
    kode = input("Masukan Kode Makanan : ")
    cursor.execute("SELECT * FROM list_makanan WHERE kode_makanan LIKE '%"+kode+"%' ")
    hasil_makanan = cursor.fetchall()
    if len(hasil_makanan) >= 1:
        harga = hasil_makanan[0][3]
    else:
        print("Masukan yang benar !")
        time.sleep(1)
        add_pesanan()
    jumlah = int(input("Jumlah Pesanan : "))
    totalharga = harga * jumlah
    print("Total Harga : ",totalharga)
    show_data_promo()
    promo = input("Masukan Kode Promo Yang Tersedia (Apabila tidak ada promo isi 0) :")
    cursor.execute("SELECT * FROM list_promo WHERE code_promo LIKE '%"+promo+"%' ")
    hasil_promo = cursor.fetchall()
    if len(hasil_promo) >= 1:
        disc = hasil_promo[0][4]
        harga_akhir = totalharga * disc/100
    else:
        print("Pengisian Tidak Sesuai ! Ulang lagi !")
        clear()
        add_pesanan()
    uangpembeli = int(input("Masukan Uang Pembeli : "))
    metodepembayaran = input("Masukan Metode Pembayaran (Cash/Transfer) :")
    kembalian = uangpembeli - harga_akhir
    masukan = (nama,kode,jumlah,promo,uangpembeli,metodepembayaran,totalharga)
    print("-----RESULT----")
    print("nama = ", nama)
    print("kode makanan = ", kode)
    print("jumlah = ", jumlah)
    print("kode promo = ", promo)
    print("Discount = "+ str(disc) +"%")
    print("uang pembeli = ",uangpembeli)
    print("metode pembayaran",metodepembayaran)
    print("total harga = ", harga_akhir)
    print("Kembalian = ", kembalian)
    #-----Perintah masuk ke datbase dimulai------    
    sql = "INSERT INTO table_pemesanan (nama_pemesan, kode_makanan, jumlah_pesanan, kode_promo, uang_pembeli, metode_pembayaran, total_harga, kembalian, tanggal_pemesanan) VALUES (%s, %s, %s,%s, %s, %s,%s,%s, CURRENT_DATE())"
    cursor.execute(sql, masukan)
    db.commit()
    print("{} Pesanan telah dibuat !".format(cursor.rowcount))
    time.sleep(2)
   


#main menu2
def fixed_main_menu():

    try:
        menu = int(input("- Pilih Menu   : "))

        if (menu == 1):
            clear()
            show_data_makanan()
        elif (menu == 2):
            clear()
            show_data_promo()
        elif (menu == 3):
            clear()
            add_pesanan()
        elif (menu == 4):
            clear()
            show_data_pemesanan()
        elif (menu == 0):
            clear()
            quit()
        else:
            print("Warning : Maaf Menu Tidak tersedia !")

        if (menu != 0):
            input("\nTekan enter untuk kembali... ")
            clear()
            main_menu()
    except Exception as err:
        if (menu != 0):
            print(err)
        
        
#main menu 1
def main_menu():
    header()
    print('''
    +===================================================+
    |.::Selamat Datang di Aplikasi Kasir "Toast Dulu"::.|
    |===================================================|
    |[1] List Menu Makanan                              |
    |[2] List Promo                                     |
    |[3] Buat Pemesanan                                 |
    |[4] Riwayat Pemesanan                              |
    |[5] Tentang Aplikasi                               |
    |[0] Exit                                           |
    +===================================================+
    ''')
    fixed_main_menu()

#saat startup program memunculkan main_menu dan fixed_main_menu
try:
    main_menu()
except ConnectionRefusedError:
    print("Koneksi Tidak Ada!")
    time.sleep(2)