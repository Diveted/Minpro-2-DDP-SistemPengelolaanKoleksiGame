# Minpro-2-DDP-SistemPengelolaanKoleksiGame

Nama : Fery Sugiantoro

NIM : 2609116039

Kelas : A

## 1. Deskripsi Singkat Program

**Sistem Koleksi Game Fery Kumar** merupakan program berbasis Python yang digunakan untuk mengelola data koleksi game.

Program ini merupakan pengembangan dari Mini Project 1 dengan menambahkan beberapa fitur, yaitu sistem login menggunakan username dan password, pembagian hak akses berdasarkan role, penggunaan Dictionary dan Function, fitur pencarian data game, validasi input, serta error handling.

Data game yang disimpan terdiri dari:
- Nama game
- Genre game
- Platform
- Status game

Program memiliki 2 role pengguna, yaitu:

- **Admin**: memiliki akses penuh untuk menambah, menampilkan, mengubah, menghapus, dan mencari data game.
- **User**: hanya memiliki akses untuk menampilkan dan mencari data game.

Akun yang tersedia:

| Username | Password | Role |
|----------|----------|------|
| lelouch | admin | Admin |
| player01 | player | User |

---

# 2. Flowchart dan Penjelasan Alur

## Flowchart

<img width="3020" height="3190" alt="Diagram Tanpa Judul drawio (2) drawio (1)" src="https://github.com/user-attachments/assets/aad83852-d600-4172-8e12-f5fddf7a024e" />


Flowchart di atas merupakan pengembangan dari flowchart Mini Project 1 yang telah disesuaikan dengan alur program Mini Project 2.

## Penjelasan Alur Program

### A. Menu Awal

Ketika program dijalankan, sistem menampilkan menu awal yang terdiri dari:

1. Login
2. Keluar

Pengguna dapat memilih untuk masuk ke sistem atau keluar dari program.

### B. Proses Login

Jika pengguna memilih menu Login, program meminta:

- Username
- Password

Password dimasukkan menggunakan library `pwinput` sehingga password tidak ditampilkan secara langsung pada layar.

Program kemudian memeriksa apakah username dan password sesuai dengan data akun yang tersedia.

Jika benar, program mengambil role pengguna dan mengarahkan pengguna ke menu sesuai role.

Jika salah, jumlah percobaan login akan bertambah.

Setelah melakukan kesalahan sebanyak 3 kali, program menjalankan countdown selama 10 detik. Setelah countdown selesai, jumlah percobaan salah direset dan pengguna dapat mencoba login kembali.

### C. Pembagian Role

Setelah login berhasil, program memeriksa role pengguna.

Terdapat dua role:

**Admin**
- Tambah Data Game
- Tampilkan Data Game
- Ubah Data Game
- Hapus Data Game
- Cari Data Game
- Logout

**User**
- Tampilkan Data Game
- Cari Data Game
- Logout

Perbedaan hak akses tersebut membuat Admin memiliki akses CRUD lengkap, sedangkan User hanya dapat melihat dan mencari data.

### D. Tambah Data Game

Admin dapat menambahkan data game dengan memasukkan:

- Nama game
- Genre
- Platform
- Status game

Status game memiliki tiga pilihan:

1. Belum dimainkan
2. Sedang dimainkan
3. Sudah tamat

Program melakukan validasi menggunakan conditional statement. Jika pilihan status tidak sesuai, program akan meminta pengguna memasukkan pilihan kembali.

Data game kemudian disimpan dalam bentuk Dictionary dan dimasukkan ke dalam `koleksi_game`.

### E. Tampilkan Data Game

Program terlebih dahulu memeriksa apakah koleksi game kosong.

Jika belum terdapat data, program menampilkan pesan bahwa belum ada data game.

Jika terdapat data, program melakukan perulangan untuk menampilkan seluruh data game yang tersimpan.

Informasi yang ditampilkan meliputi:

- Nama game
- Genre
- Platform
- Status

### F. Ubah Data Game

Admin dapat mengubah data game yang sudah tersimpan.

Program terlebih dahulu memeriksa apakah terdapat data game.

Jika terdapat data, program menampilkan daftar game dan meminta pengguna memilih nomor data yang ingin diubah.

Nomor data divalidasi agar berada dalam rentang data yang tersedia.

Program juga menggunakan `try-except` untuk menangani kesalahan ketika pengguna memasukkan selain angka.

Setelah data dipilih, pengguna dapat memasukkan data baru berupa nama, genre, platform, dan status game.

Data lama kemudian diganti dengan data baru.

### G. Hapus Data Game

Admin dapat menghapus data game.

Program terlebih dahulu memeriksa apakah terdapat data game.

Jika terdapat data, pengguna memilih nomor data yang ingin dihapus.

Nomor data divalidasi menggunakan conditional statement dan error handling.

Sebelum data dihapus, program meminta konfirmasi:

`y/n`

Jika pengguna memilih `y`, data game akan dihapus.

Jika pengguna memilih selain `y`, proses penghapusan dibatalkan.

### H. Cari Data Game

Admin dan User dapat menggunakan fitur pencarian game.

Pengguna memasukkan nama atau kata kunci game yang ingin dicari.

Program kemudian melakukan perulangan terhadap data game dan mencocokkan kata kunci dengan nama game.

Jika game ditemukan, program menampilkan informasi game tersebut.

Jika tidak ditemukan, program menampilkan pesan bahwa game tidak ditemukan.

### I. Logout

Admin dan User memiliki menu Logout.

Jika pengguna memilih Logout, pengguna akan keluar dari menu role dan kembali ke menu awal.

Dari menu awal, pengguna dapat login kembali atau keluar dari program.

### J. Keluar Program

Jika pengguna memilih menu Keluar pada menu awal, program menampilkan pesan terima kasih dan program selesai.

---

# 3. Dokumentasi Program & Output

## A. Tampilan Menu Awal

Menu awal digunakan sebagai halaman pertama program.

Terdapat dua pilihan:

1. Login
2. Keluar

Contoh output:

<img width="447" height="178" alt="Screenshot 2026-10-06 155343" src="https://github.com/user-attachments/assets/e430c795-92f0-48f7-8820-980b67cd04bc" />


---

B. Login Berhasil

Pengguna memasukkan username dan password yang benar.

Contoh:

<img width="415" height="327" alt="Screenshot 2026-10-06 172309" src="https://github.com/user-attachments/assets/ba1e13d1-6e55-4f2b-8516-74f7cfbe54db" />


Setelah login berhasil, pengguna diarahkan ke menu sesuai role.


---

C. Login Salah dan Countdown

Jika username atau password salah, program menampilkan jumlah percobaan yang salah.

Setelah 3 kali kesalahan, program menjalankan countdown selama 10 detik.

Contoh:

<img width="427" height="720" alt="image" src="https://github.com/user-attachments/assets/7e07f8a8-24ca-4709-a49e-c9f52a74d40d" />



---

D. Menu Admin

Admin memiliki akses penuh terhadap data game.

Contoh output:

<img width="451" height="257" alt="image" src="https://github.com/user-attachments/assets/838966c3-71af-41eb-8c10-b8e8d080f2e4" />



---

E. Menambahkan Data Game

Admin dapat memasukkan data game baru.

Contoh:

<img width="380" height="300" alt="image" src="https://github.com/user-attachments/assets/af7a0213-a061-4ec4-ac50-9df3fe850795" />



---

F. Menampilkan Data Game

Setelah data berhasil ditambahkan, data dapat ditampilkan melalui menu Tampilkan Data Game.

Contoh:

<img width="387" height="846" alt="image" src="https://github.com/user-attachments/assets/e21c1dc3-718f-43b1-9744-cef0de9f150e" />



---

G. Mengubah Data Game

Admin dapat memilih data berdasarkan nomor data yang tersedia.

Contoh:

<img width="467" height="612" alt="image" src="https://github.com/user-attachments/assets/ad10c25d-a0b5-43ad-8ec7-a5568bc76368" />


Setelah itu admin dapat memasukkan data baru.

Jika nomor yang dimasukkan bukan angka, program akan menampilkan pesan kesalahan tanpa menghentikan program.


---

H. Menghapus Data Game

Admin dapat memilih data yang ingin dihapus.

Program akan meminta konfirmasi sebelum menghapus data.

Contoh:

<img width="440" height="317" alt="image" src="https://github.com/user-attachments/assets/3cbc5a90-969c-4e6d-9447-4328fc386980" />



---

I. Mencari Data Game

Admin dan User dapat mencari game berdasarkan nama atau kata kunci.

Contoh:

<img width="515" height="191" alt="image" src="https://github.com/user-attachments/assets/6de61128-42ff-4804-985a-47e3c62ef502" />


Jika data tidak ditemukan:

Game tidak ditemukan.


---

J. Menu User

User memiliki hak akses yang berbeda dengan Admin.

Contoh:

<img width="422" height="522" alt="image" src="https://github.com/user-attachments/assets/b40cdb35-cf2b-4da6-9a25-0b1eeede9f98" />


User tidak memiliki akses untuk menambah, mengubah, atau menghapus data game.


---

4. Nilai Tambah

Program ini menerapkan beberapa nilai tambah sesuai dengan ketentuan Mini Project 2.

A. Error Handling

Program menggunakan try-except untuk menangani kesalahan input angka pada proses pemilihan data.

Contoh penerapan:

<img width="701" height="252" alt="Screenshot 2026-10-06 182149" src="https://github.com/user-attachments/assets/5447f42d-14cf-4959-8511-ed108fad6e91" />


Dengan adanya error handling, ketika pengguna memasukkan input yang bukan angka, program tidak langsung berhenti atau mengalami error.

Program akan menampilkan pesan kesalahan dan meminta input kembali.

Error handling juga diterapkan pada proses penghapusan data.


---

B. Penggunaan 3 Library Python

Program menggunakan 3 library/module Python sesuai dengan kebutuhan program.

1. os

Digunakan untuk membersihkan tampilan layar pada program.

<img width="135" height="20" alt="Screenshot 2026-10-06 181604" src="https://github.com/user-attachments/assets/f3e985a1-5df8-4e83-846e-2d997a38d154" />


Digunakan pada fungsi:

<img width="542" height="65" alt="image" src="https://github.com/user-attachments/assets/f2494c1a-dee5-4938-9e3b-3d4f7913adf5" />



Dan dipanggil dengan:

<img width="230" height="32" alt="Screenshot 2026-10-06 184740" src="https://github.com/user-attachments/assets/229ae749-720b-423a-b384-623d35100517" />


2. time

Digunakan untuk memberikan jeda pada program dan menjalankan countdown ketika pengguna melakukan kesalahan login sebanyak 3 kali.

<img width="150" height="27" alt="Screenshot 2026-10-06 181548" src="https://github.com/user-attachments/assets/3ccb4708-818c-4a85-832a-7e046e0f75c0" />



Contoh penggunaannya:

<img width="275" height="55" alt="Screenshot 2026-10-06 185036" src="https://github.com/user-attachments/assets/1f1d9b9e-f84c-4c97-aef7-b5455fc28f84" />


3. pwinput

Digunakan untuk menyembunyikan password ketika pengguna melakukan login.

<img width="170" height="32" alt="Screenshot 2026-10-06 181554" src="https://github.com/user-attachments/assets/58b1c972-dfbb-499e-8ba7-2819bb02862c" />


Contoh penggunaannya:

<img width="533" height="40" alt="Screenshot 2026-10-06 185631" src="https://github.com/user-attachments/assets/4d791525-6a0b-4147-978c-2a929419e56e" />


Library pwinput perlu di-install terlebih dahulu menggunakan:

pip install pwinput


---
