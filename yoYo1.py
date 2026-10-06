import os
import time
import pwinput

koleksi_game = []

akun = {
    "lelouch": {
        "password": "admin",
        "role": "admin"
    },
    "player01": {
        "password": "player",
        "role": "user"
    }
}


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def login():
    print("\n===== LOGIN SISTEM KOLEKSI GAME =====")

    salah = 0

    while True:
        username = input("Username: ")
        password = pwinput.pwinput("Password: ")

        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]

            print("\nLogin berhasil!")
            print("Selamat datang,", username)
            print("Role:", role)

            time.sleep(2)
            return role

        else:
            salah += 1

            print("\nUsername atau password salah!")
            print("Percobaan salah:", salah, "kali")

            if salah == 3:
                print("\nTerlalu banyak percobaan salah.")
                print("Tunggu 10 detik sebelum mencoba lagi.")

                for i in range(10, 0, -1):
                    print("Coba lagi dalam", i, "detik...")
                    time.sleep(1)

                salah = 0
                print("\nSilakan login kembali.")


def tambah_game():
    print("\n--- TAMBAH DATA GAME ---")

    nama = input("Masukkan nama game: ")
    genre = input("Masukkan genre game: ")
    platform = input("Masukkan platform: ")

    while True:
        print("\nStatus Game:")
        print("1. Belum dimainkan")
        print("2. Sedang dimainkan")
        print("3. Sudah tamat")

        status_pilihan = input("Pilih status (1-3): ")

        if status_pilihan == "1":
            status = "belum dimainkan"
            break
        elif status_pilihan == "2":
            status = "sedang dimainkan"
            break
        elif status_pilihan == "3":
            status = "sudah tamat"
            break
        else:
            print("Pilihan status tidak valid!")

    data_game = {
        "nama": nama,
        "genre": genre,
        "platform": platform,
        "status": status
    }

    koleksi_game.append(data_game)

    print("\nData game berhasil ditambahkan!")


def tampilkan_game():
    print("\n--- DATA KOLEKSI GAME ---")

    if len(koleksi_game) == 0:
        print("Belum ada data game.")
    else:
        for i in range(len(koleksi_game)):
            print("\nData ke-", i + 1)
            print("Nama Game :", koleksi_game[i]["nama"])
            print("Genre     :", koleksi_game[i]["genre"])
            print("Platform  :", koleksi_game[i]["platform"])
            print("Status    :", koleksi_game[i]["status"])


def ubah_game():
    print("\n--- UBAH DATA GAME ---")

    if len(koleksi_game) == 0:
        print("Belum ada data game yang dapat diubah.")
        return

    for i in range(len(koleksi_game)):
        print(i + 1, ".", koleksi_game[i]["nama"])

    while True:
        try:
            nomor = int(input("Pilih nomor data yang ingin diubah: "))

            if nomor >= 1 and nomor <= len(koleksi_game):
                break
            else:
                print("Nomor data tidak tersedia!")

        except ValueError:
            print("Masukkan nomor berupa angka!")

    index = nomor - 1

    print("\nData lama:")
    print("Nama Game :", koleksi_game[index]["nama"])
    print("Genre     :", koleksi_game[index]["genre"])
    print("Platform  :", koleksi_game[index]["platform"])
    print("Status    :", koleksi_game[index]["status"])

    nama_baru = input("\nMasukkan nama game baru: ")
    genre_baru = input("Masukkan genre baru: ")
    platform_baru = input("Masukkan platform baru: ")

    while True:
        print("\nStatus Game:")
        print("1. Belum dimainkan")
        print("2. Sedang dimainkan")
        print("3. Sudah tamat")

        status_pilihan = input("Pilih status (1-3): ")

        if status_pilihan == "1":
            status_baru = "belum dimainkan"
            break
        elif status_pilihan == "2":
            status_baru = "sedang dimainkan"
            break
        elif status_pilihan == "3":
            status_baru = "sudah tamat"
            break
        else:
            print("Pilihan status tidak valid!")

    koleksi_game[index] = {
        "nama": nama_baru,
        "genre": genre_baru,
        "platform": platform_baru,
        "status": status_baru
    }

    print("\nData game berhasil diubah!")


def hapus_game():
    print("\n--- HAPUS DATA GAME ---")

    if len(koleksi_game) == 0:
        print("Belum ada data game yang dapat dihapus.")
        return

    for i in range(len(koleksi_game)):
        print(i + 1, ".", koleksi_game[i]["nama"])

    while True:
        try:
            nomor = int(input("Pilih nomor data yang ingin dihapus: "))

            if nomor >= 1 and nomor <= len(koleksi_game):
                break
            else:
                print("Nomor data tidak tersedia!")

        except ValueError:
            print("Masukkan nomor berupa angka!")

    index = nomor - 1

    print("\nData yang dipilih:", koleksi_game[index]["nama"])

    konfirmasi = input("Yakin ingin menghapus data? (y/n): ")

    if konfirmasi.lower() == "y":
        koleksi_game.pop(index)
        print("Data game berhasil dihapus!")
    else:
        print("Penghapusan data dibatalkan.")


def cari_game():
    print("\n--- CARI DATA GAME ---")

    if len(koleksi_game) == 0:
        print("Belum ada data game.")
        return

    kata_kunci = input("Masukkan nama game yang dicari: ")

    ditemukan = False

    for game in koleksi_game:
        if kata_kunci.lower() in game["nama"].lower():
            print("\nGame ditemukan!")
            print("Nama Game :", game["nama"])
            print("Genre     :", game["genre"])
            print("Platform  :", game["platform"])
            print("Status    :", game["status"])

            ditemukan = True

    if ditemukan == False:
        print("Game tidak ditemukan.")


def menu_admin():
    while True:
        print("\n===== SISTEM KOLEKSI GAME FERY KUMAR =====")
        print("ROLE: ADMIN")
        print("1. Tambah Data Game")
        print("2. Tampilkan Data Game")
        print("3. Ubah Data Game")
        print("4. Hapus Data Game")
        print("5. Cari Data Game")
        print("6. Logout")
        print("==========================================")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_game()
        elif pilihan == "2":
            tampilkan_game()
        elif pilihan == "3":
            ubah_game()
        elif pilihan == "4":
            hapus_game()
        elif pilihan == "5":
            cari_game()
        elif pilihan == "6":
            print("\nBerhasil logout.")
            time.sleep(1)
            break
        else:
            print("\nPilihan menu tidak valid!")
            print("Silakan masukkan angka 1-6.")


def menu_user():
    while True:
        print("\n===== SISTEM KOLEKSI GAME FERY KUMAR =====")
        print("ROLE: USER")
        print("1. Tampilkan Data Game")
        print("2. Cari Data Game")
        print("3. Logout")
        print("==========================================")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            tampilkan_game()
        elif pilihan == "2":
            cari_game()
        elif pilihan == "3":
            print("\nBerhasil logout.")
            time.sleep(1)
            break
        else:
            print("\nPilihan menu tidak valid!")
            print("Silakan masukkan angka 1-3.")


while True:
    bersihkan_layar()

    print("==========================================")
    print("   SISTEM KOLEKSI GAME FERY KUMAR")
    print("==========================================")
    print("1. Login")
    print("2. Keluar")
    print("==========================================")

    pilihan_awal = input("Pilih menu (1-2): ")

    if pilihan_awal == "1":
        role = login()

        if role == "admin":
            menu_admin()
        elif role == "user":
            menu_user()

    elif pilihan_awal == "2":
        print("\nTerima kasih telah menggunakan sistem.")
        break

    else:
        print("\nPilihan menu tidak valid!")
        print("Silakan masukkan angka 1-2.")

        time.sleep(1)