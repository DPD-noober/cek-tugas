import time
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cekcok"
)

def show_data():
    cursor = db.cursor()
    sql = "SELECT * FROM list_makanan"
    cursor.execute(sql)

    results = cursor.fetchall()
    #menampilkan isi table pada database dalam bentuk baris.
    for row in results:
        print('='*30)
        print('Pembelian Ke- : ',+row[0])
        print('Nama : '+row[1])
        print('Alamat : '+row[2])
        print('='*30)
show_data()
