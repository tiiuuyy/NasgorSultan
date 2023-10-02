import os
import csv
from datetime import datetime
import time

nama = []
jumlah = []
harga1 = []
hargaTotal = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def awal():
    print('=' * 35)
    print('=Selamat Datang di Nasgor Sultan='.center(35,' '))
    print('=' * 35)
    print('''
        1. Login
        2. Logout
        ''')
    user = input('Masukkan pilihan Anda \n>>> ')
    if user == '1':
        clear_screen()
        login()
    elif user == '2':
        logout()
    else:
        print('Kamu menginputkan nomor yang salah. Coba input dengan benar ya!')
        clear_screen()
        awal()

def login():
    print('=' *35)
    nama = input('Nama Anda \n>>> ')
    pw = input('Password \n>>> ')
    if (nama == 'tiara' or 'aisha') and (pw == '1234'):
        print('Login Berhasil')
        time.sleep(2)
        clear_screen()
        daftarmenu()
    else:
        print('Data login tidak valid. Silahkan kembali ke menu awal.')
        input('Tekan enter untuk kembali ke menu awal >>> ')
        time.sleep(2)
        clear_screen()
        awal()

def daftarmenu():
    print('=========== DAFTAR MENU ==========='.center(45,' '))
    print('============= MAKANAN ============='.center(45,' '))

    print(''' 
    |   Nasi Goreng          | Rp 27000 |
    |   Nasi Goreng Spesial  | Rp 32000 |
    |   Nasi Goreng Tom Yum  | Rp 32000 |
    |   Nasi Goreng Cabe Ijo | Rp 35000 |
    |   Nasi Goreng Sosis    | Rp 37000 |
        ''')

    print('     ============= MINUMAN ============= ')
    print(''' 
    |   Teh Tarik            | Rp 18000 |
    |   Thai Tea             | Rp 18000 |
    |   Milkshake Strawberry | Rp 17000 |
    |   Milkshake Chocolate  | Rp 17000 |
    |   Lemon Tea            | Rp 16000 |
    |   Lychee Tea           | Rp 17000 |
        ''')
    pesanMenu()

def pesanMenu():
    print('=========== PESAN MENU ==========='.center(45,' '))
    print('''
    1. Pesan
    2. Hapus
    3. Lihat Pesanan
    4. Bayar
    ''')
    pesan = input('Masukkan pilihan \n>>> ')
    if pesan == '1':
        pesanan()
    elif pesan == '2':
        hapus()
    elif pesan == '3':
        lihat()
    elif pesan == '4':
        bayar()
    else:
        clear_screen()
        print('Yah, sayang banget pilihan kamu tidak bisa kita proses. Coba cek kembali nomor yang kamu input ya!')
        time.sleep(1)
        clear_screen()
        pesananKu()
        daftarmenu()
        pesanMenu()

def pesananKu():
        print('='* 63)
        ket = [ "NO", "PESANAN", "JUMLAH", "HARGA", "TOTAL"]
        print(f'{ket[0]:<8}{ket[1]:<27}{ket[2]:<12}{ket[3]:<10}{ket[4]:<15}')
        print('='*63)
        for x in range(len(nama)):
                print(f'{x+1:<8}{nama[x]:<27}{jumlah[x]:<12}{harga1[x]:<10}{hargaTotal[x]:<15}')
        print('='*63)


def pesanan():       
        num = input('Pesanan Nomor : ')
        item = input('Mau pesan menu apa? \n> ')
        count = int(input('Beli berapa porsi? \n> '))
        price = int(input('Harga per porsi? \n> '))

        nama.append(item)
        jumlah.append(int(count))
        harga1.append(int(price))
        totalprice = count * price
        hargaTotal.append(int(totalprice))

        with open('iCart.csv', 'w', newline='') as file:
                kolom = ['NO','PESANAN','JUMLAH', 'HARGA', 'TOTAL HARGA']
                writer = csv.DictWriter(file, delimiter=",", fieldnames=kolom)
                dataBaru = {"NO" : num, "PESANAN" : item, "JUMLAH" : count, "HARGA" : price, "TOTAL HARGA" : totalprice}
                writer.writerow(dataBaru)
                clear_screen()
                print(f'\nKamu menambahkan {item} sebanyak {count} dengan total harga {totalprice} \nke dalam daftar pesananmu')
                time.sleep(2)
                clear_screen()
                pesananKu()
                daftarmenu()
                pesanMenu()

def hapus():
    with open('iCart.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        hapus = int(input('Pilih nomor: ')) - 1
        nama.pop(hapus)
        jumlah.pop(hapus)
        harga1.pop(hapus)
        hargaTotal.pop(hapus)
        for i in range(len(nama)):
            newFile = [nama[i], jumlah[i], harga1[i], hargaTotal[i]]
            writer.writerow(newFile)
        file.close()
        clear_screen()
        daftarmenu()
        print('HAPUS DATA BERHASIL')
        pesananKu()

def lihat():
    clear_screen()
    pesananKu()
    pesanMenu()

def bayar():
    print()
    print("="* 35)
    print("Jumlah harga yang dibayarkan \t: Rp ", sum(hargaTotal))
    pembayaran = (int(input("Masukkan nominal uang yang diberikan \t: Rp " )))
    kembalian = pembayaran - sum(hargaTotal)
    if kembalian == 0:
        print("-")
    elif kembalian == hargaTotal<pembayaran:
        print("Mohon maaf nominal yang Anda Masukkan kurang")
        pembayaran2 = (int(input("Masukkan kembali nominal uang Anda : Rp. ")))
        kembalian2 = pembayaran2 - sum(hargaTotal)
        print("Kembalian Anda adalah Rp. ", kembalian2)
    else:
        time.sleep(1)
        print("Kembalian Anda adalah Rp. ", kembalian)
        time.sleep(1)
        clear_screen()
        struck()
        

def struck():
    print(' STRUCK PEMBAYARAN '.center(63,'='))
    print(' NASI GORENG SULTAN '.center(63,'='))
    print('Waktu Transaksi ', datetime.now())
    input('Pesanan atas nama : ')
    print('=' * 63)
    print("Jumlah harga yang dibayarkan   \t: Rp ", sum(hargaTotal))
    print('Dengan rincian pesanan sebagai berikut: ')
    pesananKu()
    print('=' * 63)
    print('Pembayaran Telah Dilakukan'.center(63,' '))
    print('Silahkan tunggu pesanan Anda'.center(63,' '))
    print('Semoga Harimu Menyenangkan <3'.center(63,' '))
    print('=' * 63)
    cek = input('Apakah anda ingin membuat pesanan lagi? y/t \n>>>')
    if cek == 'y':
        clear_screen()
        time.sleep(1)
        awal()
    elif cek == 't':
        time.sleep(1)
        clear_screen()
        awal()
    else:
        print('')

def logout():
    lo = input('Apakah anda yakin ingin keluar program? y/t \n> ')
    if lo == 'y':
        print('Sampai jumpa di pesanan selanjutnya')
        exit()
    elif lo == 't':
        daftarmenu()
        pesanMenu()
    else:
        print('Kami tidak bisa memproses perintah Anda. Harap input kembali')
        logout()

awal()