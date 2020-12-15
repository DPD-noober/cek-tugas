import mysql.connector
import time

#----INSTALASI PERTAMA, APABILA BARU PAKAI PROGRAM INI, WAJIB INSTALL XAMPP DLU------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)

def create_db():
    cursor = db.cursor()
    print("Sedang membuat Database .....")
    time.sleep(3)
    cursor.execute("CREATE DATABASE IF NOT EXISTS cekcok")
    print("Database [Toast_Dulu] Berhasil Dibuat !")

def create_table():
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cekcok"
    )
    cursor = db.cursor()
    sql = """CREATE TABLE IF NOT EXISTS pemesanan (
        id_pemesanan INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(255),
        kode_makanan Varchar(255),
        jumlah int,
        kode_promo varchar(255),
        uang_pembeli int,
        total_harga int,
        kembalian int
    )
    """
    
    sql2 = """CREATE TABLE IF NOT EXISTS list_makanan (
        id_makanan INT AUTO_INCREMENT PRIMARY KEY,
        kode_makanan Varchar(255),
        nama_makanan Varchar(255),
        harga_makanan int
    )
    """

    menu = "INSERT INTO list_makanan (kode_makanan, nama_makanan, harga_makanan) VALUES (%s, %s, %s)"
    values = [
        ("TD001","Toast with Crispy Chicken","23000"),
        ("TD002","Toast with Creamy Shroom","23000"),
        ("TD003","Toast with Ham and Cheese","30000"),
        ("TD004","Toast with Egg and Cheese", "28000"),
        ("TD005","Toast with Curry Tuna","30000"),
        ("TD006","Toast with Thai Sweet Chili","22000")
    ]

    sql3 = """CREATE TABLE IF NOT EXISTS list_promo (
        id_promo INT AUTO_INCREMENT PRIMARY KEY,
        nama_promo VARCHAR(255),
        code_promo Varchar(50),
        keterangan_promo INT(255),
        diskon_promo INT(50),
        status_promo varchar(255)
    )
    """

    promo = "INSERT INTO list_promo (nama_promo, code_promo, keterangan_promo, diskon_promo, status_promo) VALUES (%s, %s, %s, %s, %s)"
    valuesp = [
        ("Promo Hemat","PROM1","50.000","10%","Active"),

    ]

    sql4 = """CREATE TABLE IF NOT EXISTS table_pemesanan (
        id_pesanan INT AUTO_INCREMENT PRIMARY KEY,
        nama_pemesan VARCHAR(255),
        kode_makanan Varchar(50),
        jumlah_pesanan int,
        kode_promo varchar(50),
        uang_pembeli int,
        metode_pembayaran varchar(50),
        total_harga int,
        kembalian int,
        tanggal_pemesanan varchar(50)
    )
    """

    #---------------------------SETUP DIMULAI-------------------------

    print("Membuat Table Pemesanan...")
    time.sleep(5)
    cursor.execute(sql)
    print("Membuat Table list_makanan...")
    time.sleep(5)
    cursor.execute(sql2)
    print("Membuat isi Table list_makanan...")
    time.sleep(5)
    for val in values:
        cursor.execute(menu, val)
        db.commit()
    
    print("Membuat Table list_promo...")
    time.sleep(5)
    cursor.execute(sql3)
    print("Membuat isi Table list_promo...")
    time.sleep(5)
    for valp in valuesp:
        cursor.execute(promo, valp)
        db.commit()
    print("{} Data ditambahkan".format(cursor.rowcount))
    time.sleep(2)
    print("Membuat Table table_pemesanan...")
    time.sleep(5)
    cursor.execute(sql4)
    print("Semua Data Telah Dibuat !")
    print("[SUKSES CREATING]")
    time.sleep(3)
    quit()

print("Mohon menunggu, Sedang menyiapkan sesuatu...")
create_db()
time.sleep(5)
create_table()