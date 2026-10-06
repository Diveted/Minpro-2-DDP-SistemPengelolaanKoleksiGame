# Minpro-2-DDP-SistemPengelolaanKoleksiGame

# Minpro-2-DDP-SistemKoleksiGame

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

![Flowchart Sistem Koleksi Game](flowchart_minpro2.png)

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

```text
==========================================
   SISTEM KOLEKSI GAME FERY KUMAR
==========================================
1. Login
2. Keluar
==========================================
Pilih menu (1-2):
