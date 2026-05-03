![preview1](https://r2.fivemanage.com/WX5Hv6yMgODTgG2WF6rml/images/backgroundgithub.png)

# 🗑️ Roblox DataStore Key Deleter

Script Python untuk menghapus **semua key** dalam sebuah DataStore Roblox secara otomatis menggunakan [Roblox Open Cloud API](https://create.roblox.com/docs/cloud/open-cloud).

---

## 📋 Fitur

- Mengambil semua key dari DataStore secara otomatis (mendukung pagination)
- **Mode DRY RUN** — simulasi tanpa benar-benar menghapus data
- **Mode HAPUS** — menghapus semua key secara permanen dengan konfirmasi
- Menampilkan progress tiap key yang diproses
- Ringkasan hasil di akhir eksekusi

---

## ⚠️ Peringatan

> **Penghapusan bersifat PERMANEN dan tidak dapat dibatalkan.**
> Selalu gunakan `DRY_RUN = True` terlebih dahulu untuk memastikan key yang akan dihapus sudah benar.

---

## 🐍 Instalasi Python

### 1. Download Python

1. Buka [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Klik tombol **"Download Python 3.x.x"** (versi terbaru)
3. Jalankan installer yang sudah didownload

### 2. Instal Python

- Pada layar installer, **centang** opsi **"Add Python to PATH"** sebelum klik Install
- Klik **"Install Now"**
- Tunggu hingga selesai, lalu klik **"Close"**

### 3. Verifikasi Instalasi

Buka **Command Prompt** (tekan `Win + R`, ketik `cmd`, tekan Enter) lalu jalankan:

```bash
python --version
```

Output yang diharapkan:
```
Python 3.x.x
```

### 4. Install Library yang Diperlukan

```bash
pip install requests
```

---

## 🔑 Cara Mendapatkan API Key

API Key digunakan untuk mengautentikasi script agar bisa mengakses DataStore game kamu.

1. Buka [https://create.roblox.com/dashboard/credentials](https://create.roblox.com/dashboard/credentials)
2. Login dengan akun Roblox kamu
3. Klik tombol **"Create API Key"**
4. Isi form berikut:
   - **Name**: Bebas, contoh: `datastore-deleter`
   - **API System**: Pilih **"DataStore"**
   - **Experience** : Pilih experience/game yang ingin diakses
   - **Operations**: Centang **"Read"** dan **"Delete"** (minimal keduanya)
5. Pada bagian **"Accepted IP Addresses"**, masukkan IP kamu atau pilih **"Allow All IP Addresses"** untuk kemudahan
6. Klik **"Save & Generate Key"**
7. **Salin API Key yang muncul** — simpan dengan aman, karena tidak akan ditampilkan lagi

> Jika API Key hilang, kamu harus membuat yang baru.

---

## 🌐 Cara Mendapatkan Universe ID

Universe ID adalah ID unik dari game/experience kamu di Roblox.

### Cara 1 — Melalui Creator Dashboard

1. Buka [https://create.roblox.com/dashboard/creations](https://create.roblox.com/dashboard/creations)
2. Klik pada game yang ingin kamu kelola
3. Lihat URL di browser, formatnya:
   ```
   https://create.roblox.com/dashboard/creations/experiences/XXXXXXXXXX/overview
   ```
4. Angka **XXXXXXXXXX** di URL tersebut adalah **Universe ID** kamu

### Cara 2 — Melalui Roblox Website

1. Buka halaman game kamu di [roblox.com](https://www.roblox.com)
2. Lihat URL di browser, formatnya:
   ```
   https://www.roblox.com/games/XXXXXXXXXX/nama-game
   ```
3. Namun perlu diperhatikan, angka di URL ini adalah **Place ID**, bukan Universe ID
4. Untuk mengkonversi, gunakan API:
   ```
   https://apis.roblox.com/universes/v1/places/PLACE_ID/universe
   ```
   Ganti `PLACE_ID` dengan angka dari URL game kamu

---

## 📦 Cara Mendapatkan Nama DataStore

Nama DataStore adalah nama yang kamu gunakan saat memanggil `game:GetService("DataStoreService"):GetDataStore("NamaDataStore")` di script Roblox Studio kamu.

### Cara Menemukan Nama DataStore di Script Roblox Studio

1. Buka **Roblox Studio** dan buka project game kamu
2. Cari di **Explorer** → **ServerScriptService** (atau tempat lain dimana script server berada)
3. Buka script yang menggunakan DataStore
4. Cari baris seperti:

```lua
local DataStore = game:GetService("DataStoreService"):GetDataStore("PlayerData")
```

5. Nama dalam tanda kutip (`"PlayerData"`) adalah **nama DataStore** kamu

### Cara Melihat DataStore yang Ada (Melalui Open Cloud API)

Kamu juga bisa melihat daftar DataStore yang tersedia dengan menjalankan perintah berikut di terminal (ganti nilai yang sesuai):

```bash
curl -X GET "https://apis.roblox.com/datastores/v1/universes/UNIVERSE_ID/standard-datastores" -H "x-api-key: API_KEY_KAMU"
```

---

## ⚙️ Konfigurasi Script

Buka file `deleted_key_datastore.py` dengan teks editor (Notepad, VS Code, dll), lalu isi bagian konfigurasi di awal file:

```python
API_KEY        = "your-api-key-here"     # API Key dari Creator Dashboard
UNIVERSE_ID    = "1234567890"            # Universe ID game kamu
DATASTORE_NAME = "PlayerData"            # Nama DataStore yang ingin dihapus keynya
SCOPE          = "global"                # Biarkan "global" jika tidak tahu
DRY_RUN        = True                    # True = simulasi, False = hapus sungguhan
```

### Penjelasan Parameter

| Parameter | Keterangan |
|---|---|
| `API_KEY` | Kunci API dari Roblox Creator Dashboard |
| `UNIVERSE_ID` | ID unik experience/game kamu |
| `DATASTORE_NAME` | Nama DataStore yang ingin dihapus semua keynya |
| `SCOPE` | Scope DataStore, biasanya `"global"` |
| `DRY_RUN` | `True` = hanya simulasi, `False` = hapus permanen |

---

## ▶️ Cara Menjalankan Script

### Langkah 1 — Buka Terminal / Command Prompt

Tekan `Win + R`, ketik `cmd`, lalu tekan Enter.

### Langkah 2 — Navigasi ke Folder Script

```bash
cd "C:\path\ke\folder\script"
```

Contoh:
```bash
cd "C:\Users\NamaKamu\Downloads\deleted_key_datastore"
```

### Langkah 3 — Jalankan Script

```bash
python deleted_key_datastore.py
```

---

## 🔄 Alur Penggunaan yang Disarankan

```
1. Isi konfigurasi di script
         ↓
2. Set DRY_RUN = True
         ↓
3. Jalankan script → lihat daftar key yang akan dihapus
         ↓
4. Pastikan key yang muncul sudah benar
         ↓
5. Set DRY_RUN = False
         ↓
6. Jalankan script lagi → ketik 'YA' untuk konfirmasi
         ↓
7. Semua key terhapus ✓
```

---

## 📊 Contoh Output

### Mode DRY RUN
```
============================================================
  Roblox DataStore Key Deleter
============================================================
  Universe ID    : 1234567890
  DataStore Name : PlayerData
  Scope          : global
  Mode           : DRY RUN (simulasi)
============================================================

[INFO] Mengambil daftar semua key...
  Halaman 1: ditemukan 100 key
  Halaman 2: ditemukan 45 key

[INFO] Total key ditemukan: 145
  [DRY RUN] [1/145] Akan menghapus: Player_12345678
  [DRY RUN] [2/145] Akan menghapus: Player_87654321
  ...

============================================================
  [DRY RUN] 145 key akan dihapus jika DRY_RUN=False
============================================================
```

### Mode HAPUS
```
============================================================
  Roblox DataStore Key Deleter
============================================================
  Universe ID    : 1234567890
  DataStore Name : PlayerData
  Scope          : global
  Mode           : ⚠ HAPUS SUNGGUHAN
============================================================

[INFO] Mengambil daftar semua key...
  Halaman 1: ditemukan 100 key

[INFO] Total key ditemukan: 100

⚠  Semua key akan dihapus permanen. Ketik 'YA' untuk melanjutkan: YA
  [1/100] ✓ Berhasil: Player_12345678
  [2/100] ✓ Berhasil: Player_87654321
  ...

============================================================
  Selesai! Berhasil: 100 | Gagal: 0
============================================================
```

---

## ❗ Troubleshooting

### Error: `ModuleNotFoundError: No module named 'requests'`
Install library requests:
```bash
pip install requests
```

### Error: `401 Unauthorized`
- Pastikan `API_KEY` sudah benar dan tidak ada spasi di depan/belakang
- Pastikan API Key memiliki permission **Read** dan **Delete** untuk DataStore
- Pastikan API Key dikaitkan dengan Universe ID yang benar

### Error: `403 Forbidden`
- Pastikan game kamu sudah **dipublish** (bukan hanya disimpan lokal)
- Pastikan IP address kamu diizinkan di pengaturan API Key

### Error: `404 Not Found`
- Periksa kembali `UNIVERSE_ID` — pastikan angkanya benar
- Periksa kembali `DATASTORE_NAME` — nama bersifat **case-sensitive** (huruf besar/kecil berbeda)

### `[INFO] Tidak ada key yang ditemukan. DataStore sudah kosong.`
- DataStore memang sudah kosong, atau
- Nama DataStore salah, atau
- Scope salah (coba ganti `SCOPE = "global"`)

---

## 📄 Lisensi

Script ini bebas digunakan dan dimodifikasi sesuai kebutuhan.
