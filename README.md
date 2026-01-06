# TUGAS-1-DESAIN-ANALISIS-ALGORITMA-KELAS-E
---

# Anggota Kelompok:

                  Endang Adiningsih (105841117723)

                  Miftahul Jannah   (105841116023)
---
                  
## 📌 Deskripsi Kasus

Pesawat perintis memiliki kapasitas muatan yang terbatas sehingga tidak semua paket logistik darurat dapat dibawa sekaligus. Oleh karena itu, diperlukan metode optimasi untuk memilih kombinasi barang yang memberikan nilai bantuan (profit) maksimum tanpa melebihi batas kapasitas muatan pesawat.

**Permasalahan ini dimodelkan sebagai **0/1 Knapsack Problem**, di mana setiap barang hanya dapat dipilih satu kali (diambil atau tidak diambil).**

---

## 🎯 Tujuan
- Menentukan kombinasi barang terbaik yang dapat dimuat ke dalam pesawat.
- Memaksimalkan total nilai bantuan (profit).
- Memastikan total berat tidak melebihi kapasitas maksimum pesawat.

---

## 📦 Data Barang
| No | Nama Barang | Berat | Profit |
|----|-------------|-------|--------|
| 1 | Genset Portable | 15 | 40 |
| 2 | Kotak Obat | 3 | 15 |
| 3 | Makanan Kaleng | 8 | 10 |
| 4 | Selimut Tebal | 5 | 8 |
| 5 | Tenda Darurat | 10 | 25 |
| 6 | Alat Komunikasi | 2 | 30 |
| 7 | Baterai Cadangan | 4 | 12 |
| 8 | Filter Air | 6 | 20 |
| 9 | Pakaian Kering | 7 | 8 |
| 10 | Peralatan Medis Berat | 12 | 35 |

**Jumlah item (n)** : 10  
**Kapasitas maksimum (M)** : 60  
---

## 🧠 Metode Penyelesaian
Metode yang digunakan adalah **Algoritma Backtracking** untuk menyelesaikan masalah **0/1 Knapsack**.  
Pendekatan ini membangun **state space tree**, di mana setiap node merepresentasikan keputusan mengambil atau tidak mengambil suatu item. Cabang pencarian akan **dipangkas (pruning)** apabila total berat melebihi kapasitas, sehingga proses pencarian menjadi lebih efisien dibandingkan brute force.
---

## ✅ Hasil Solusi Optimal
- **Total Berat** : 60  
- **Total Profit Maksimum** : 187  

### Barang yang Terpilih:
- Genset Portable  
- Kotak Obat  
- Makanan Kaleng  
- Tenda Darurat  
- Alat Komunikasi  
- Baterai Cadangan  
- Filter Air  
- Peralatan Medis Berat  
---

## ⚖️ Perbandingan dengan Brute Force
Pendekatan brute force mengevaluasi seluruh kemungkinan kombinasi barang, sehingga membutuhkan waktu komputasi yang lebih besar. Sebaliknya, algoritma backtracking hanya mengevaluasi kombinasi yang memungkinkan dengan melakukan pruning pada cabang yang melanggar batas kapasitas, sehingga lebih efisien namun tetap menghasilkan solusi optimal.

---
