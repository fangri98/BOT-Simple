import calculate as cal
import time_date as td
import random as rd

print("BOT FANG")


while True:
    try:
        user_input = int(input("""
                --------Mau Menanyakan apa hari ini?--------
                        1. Kalkulator
                        2. Kalender
                        3. Tebak Angka
                        4. random pasword
                        5. Keluar
                           """))
    except ValueError:
        print("Tolong masukkan dengan angka.")
        continue
# INI ADALAH KALKULATOR
    if user_input == 1:
        print("Selamat datang di Kalkulator Sederhana!")
        while True:
            print("\nPilih operasi:")
            print("1. Tambah")
            print("2. Kurang")
            print("3. kali")
            print("4. Bagi")
            print("5. Keluar")

            try:
                choice = int(input("Masukkan pilihan (1/2/3/4/5): "))
            except ValueError:
                print("Tolong masukkan angka yang valid.")
                continue

            if choice == 5:
                print("Terima kasih telah menggunakan kalkulator. Sampai jumpa!")
                break
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))

            if choice == 1:
                result = cal.tambah(num1, num2)
                print(f"Hasil: {num1} + {num2} = {result}")
                break
            elif choice == 2:
                result = cal.kurang(num1, num2)
                print(f"Hasil: {num1} - {num2} = {result}")
                break
            elif choice == 3:
                result = cal.kali(num1, num2)
                print(f"Hasil: {num1} * {num2} = {result}")
                break
            elif choice == 4:
                result = cal.bagi(num1, num2)
                print(f"Hasil: {num1} / {num2} = {result}")
                break
            else:
                print("pilihan tidak valid. silahkan coba lagi.")
                
# INI ADALAH KALENDER
    elif user_input == 2:
        print("Selamat datang di Kalender!")
        while True:
            print("\nPilih opsi:")
            print("1. Tampilkan waktu sekarang")
            print("2. Tampilkan tanggal sekarang")
            print("3. Keluar")

            try:
                choice = int(input("Masukkan pilihan (1/2/3): "))
            except ValueError:
                print("Tolong masukkan angka yang valid.")
                continue

            if choice == 3:
                print("Terima kasih telah menggunakan kalender. Sampai jumpa!")
                break
            elif choice == 1:
                current_time = td.waktu_sekarang()
                print(f"Waktu sekarang: {current_time}")
                break
            elif choice == 2:
                current_date = td.tanggal_sekarang()
                print(f"Tanggal sekarang: {current_date}")
                break
            else:
                print("Pilihan tidak valid. Silahkan coba lagi.")
                
    # INI ADALAH PERMAINAN TEBAK ANGKA
    elif user_input == 3:
        print("Selamat datang di permainan Tebak Angka!")

        print("\nSaya telah memilih sebuah angka antara 1 dan 50.")
        print("Coba tebak angka tersebut!")

        secret_number = rd.randint(1, 50)
        attempts = 0

        while True:
            try:
                guess = int(input("Masukkan tebakan anda(jika ingin keluar ketik 0): "))
            except ValueError:
                print("Tolong masukkan angka yang valid.")
                continue

            if guess == 0:
                print("Terima kasih telah bermain. Sampai jumpa!")
                break

            try:
                guess = int(guess)
            except ValueError:
                print("Tolong masukkan angka yang valid.")
                continue

            attempts += 1

            if attempts >= 5:
                print(
                    f"Maaf, anda telah mencapai batas percobaan. Angka yang benar adalah {secret_number}."
                )
                break
            if guess == secret_number:
                print(
                    f"Selamat! Anda menebak angka yang benar {secret_number} dalam {attempts} percobaan."
                )
                break
            elif guess < secret_number:
                print("Tebakan anda terlalu rendah. Coba lagi!")
                attempts += 1
            else:
                print("Tebakan anda terlalu tinggi. Coba lagi!")
                
    # INI ADALAH GENERATOR PASSWORD ACAK
    elif user_input == 4:
        print("Selamat datang di generator password acak!")
        while True:
            try:
                length = int(input("Masukkan panjang password yang diinginkan: "))
                if length <= 0:
                    print("panjang password harus lebih dari 0.")
                    continue
            except ValueError:
                print("Tolong masukkan angka yang valid.")
                continue
            
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
            password = "".join(rd.choice(characters) for _ in range(length))
            print(f"Password acak yang dihasilkan: {password}")
            break

    # INI ADALAH UNTUK KELUAR
    
    elif user_input == 5:
        print("Terima kasih telah menggunakan BOT FANG. Sampai jumpa!")
        break
