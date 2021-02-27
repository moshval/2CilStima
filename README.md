# Memorable MatKul Scheduler

Tugas Kecil 2 IF2211 Strategi Algoritma 2020/21\
Disusun oleh : Mohammad Sheva Almeyda Sofjan (13519018 | K01)

---
# Deskripsi Singkat
Program mampu menyusun rencana pengambilan mata kuliah.\
Implementasi Topological Sort pada graf asiklik berarah (Directed Acyclic Graph).\
Dibuat menggunakan bahasa pemrograman python.\
Input berupa graf dalam file dengan ekstensi .txt dengan format berikut :
```
<kode_kuliah_1>,<kode  kuliah prasyarat -1>,  <kode  kuliah  prasyarat -2>,  <kode  kuliah prasyarat -3>.
<kode_kuliah_2>,<kode kuliah prasyarat -1>, <kode kuliah prasyarat -2>.
<kode_kuliah_3>,<kode  kuliah  prasyarat -1>,  <kode  kuliah  prasyarat -2>,  <kode  kuliah prasyarat -3>, <kodekuliah prasyarat -4>.<kode_kuliah_4>.

```
Contoh input : (contoh lain terdapat pada folder test)
```
c1, c3.
c2, c1, c4.
c3.
c4, c1, c3.
c5, c2, c4.

```
---
# How To Run :
0. Pastikan python 3 sudah terinstal pada sistem operasi anda
1. Pindah ke direktori src, lalu run main.py
2. Akan muncul tampilan berikut:
```
=======================================================
            <<Memorable MatKul Scheduler>>
  Dapat menyusun rencana pengambilan mata kuliah anda
            Cr : Mohammad Sheva (13519018)
=======================================================

Masukkan Nama File (dengan ekstensi, sebagai contoh : tc1.txt) :
```
3. Ikuti instruksi pada layar
4. Selamat menikmati

# Contoh Eksekusi Program :
```
=======================================================
            <<Memorable MatKul Scheduler>>
  Dapat menyusun rencana pengambilan mata kuliah anda
            Cr : Mohammad Sheva (13519018)
=======================================================

Masukkan Nama File (dengan ekstensi, sebagai contoh : tc1.txt) : tc1.txt

Input :
c1,c3.
c2,c1,c4.
c3.
c4,c1,c3.
c5,c2,c4.

Output :
Semester 1 : c3
Semester 2 : c1
Semester 3 : c4
Semester 4 : c2
Semester 5 : c5

Lama eksekusi :  0.01565098762512207  detik
```
