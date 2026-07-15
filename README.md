# Warehouse Inventory Management System

Aplikasi Python sederhana untuk mengelola stok gudang melalui Command Line Interface (CLI).

## Features

* Add new items
* View all items
* View item details
* Update existing items
* Delete items
* Input validation
* Item code format validation using Regular Expression

## Run Application

```bash
python 0008_Jovan.py
```

## Main Menu

```text
=== SISTEM GUDANG ===

1. Tambah Barang
2. Lihat Barang
3. Update Barang
4. Hapus Barang
5. Keluar
```

## Example Usage

### Add Item

```text
Masukkan kode barang: A-001
Masukkan nama barang: Keyboard
Masukkan jumlah barang: 10
```

### View Item

```text
Kode: A-001
Nama: Keyboard
Jumlah: 10
```

### Update Item

```text
Masukkan kode barang yang ingin diupdate: A-001
Masukkan nama barang baru: Mechanical Keyboard
Masukkan jumlah barang baru: 20
```

### Delete Item

```text
Masukkan kode barang yang ingin dihapus: A-001
```

## Data Structure

```python
gudang = {
    "A-001": {
        "nama": "Keyboard",
        "jumlah": 10
    }
}
```

## Validation Rules

* Kode barang harus mengikuti format `A-001`
* Kode barang tidak boleh duplikat
* Nama barang tidak boleh kosong
* Jumlah barang tidak boleh negatif
* Input angka akan divalidasi

## Limitations

* Data disimpan di memory menggunakan Python dictionary
* Data akan hilang saat program ditutup
* Belum menggunakan database
* Single user application
