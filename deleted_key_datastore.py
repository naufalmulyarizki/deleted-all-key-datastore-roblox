import requests
import time

# ─── KONFIGURASI ──────────────────────────────────────────
API_KEY        = ""   # Kunci API dari Roblox Creator Dashboard
UNIVERSE_ID    = ""          # Universe/Experience ID
DATASTORE_NAME = ""       # Nama DataStore yang ingin dihapus semua keynya
SCOPE          = "global"                    # Scope default adalah "global"
DRY_RUN        = False                        # True = simulasi saja, False = hapus sungguhan
# ──────────────────────────────────────────────────────────

BASE_URL = "https://apis.roblox.com/datastores/v1"
HEADERS  = {"x-api-key": API_KEY}

def list_all_keys():
    keys    = []
    cursor  = None
    page_no = 1

    while True:
        params = {
            "datastoreName": DATASTORE_NAME,
            "scope":         SCOPE,
            "limit":         100,
        }
        if cursor:
            params["cursor"] = cursor

        url      = f"{BASE_URL}/universes/{UNIVERSE_ID}/standard-datastores/datastore/entries"
        response = requests.get(url, headers=HEADERS, params=params)

        if response.status_code != 200:
            print(f"[ERROR] Gagal mengambil key (halaman {page_no}): {response.status_code} — {response.text}")
            break

        data   = response.json()
        keys  += [entry["key"] for entry in data.get("keys", [])]
        cursor = data.get("nextPageCursor")

        print(f"  Halaman {page_no}: ditemukan {len(data.get('keys', []))} key")
        page_no += 1

        if not cursor:
            break

        time.sleep(0.1)

    return keys


def delete_key(key: str) -> bool:
    url    = f"{BASE_URL}/universes/{UNIVERSE_ID}/standard-datastores/datastore/entries/entry"
    params = {
        "datastoreName": DATASTORE_NAME,
        "scope":         SCOPE,
        "entryKey":      key,
    }
    response = requests.delete(url, headers=HEADERS, params=params)
    return response.status_code in (200, 204)


def main():
    print("=" * 60)
    print("  Roblox DataStore Key Deleter")
    print("=" * 60)
    print(f"  Universe ID    : {UNIVERSE_ID}")
    print(f"  DataStore Name : {DATASTORE_NAME}")
    print(f"  Scope          : {SCOPE}")
    print(f"  Mode           : {'DRY RUN (simulasi)' if DRY_RUN else '⚠ HAPUS SUNGGUHAN'}")
    print("=" * 60)

    print("\n[INFO] Mengambil daftar semua key...")
    keys = list_all_keys()

    if not keys:
        print("[INFO] Tidak ada key yang ditemukan. DataStore sudah kosong.")
        return

    print(f"\n[INFO] Total key ditemukan: {len(keys)}")

    if not DRY_RUN:
        confirm = input("\n⚠  Semua key akan dihapus permanen. Ketik 'YA' untuk melanjutkan: ")
        if confirm.strip().upper() != "YA":
            print("[INFO] Dibatalkan.")
            return

    success_count = 0
    fail_count    = 0

    for i, key in enumerate(keys, start=1):
        if DRY_RUN:
            print(f"  [DRY RUN] [{i}/{len(keys)}] Akan menghapus: {key}")
            success_count += 1
        else:
            ok = delete_key(key)
            status = "✓ Berhasil" if ok else "✗ Gagal"
            print(f"  [{i}/{len(keys)}] {status}: {key}")
            if ok:
                success_count += 1
            else:
                fail_count += 1
            time.sleep(0.1)

    print("\n" + "=" * 60)
    if DRY_RUN:
        print(f"  [DRY RUN] {success_count} key akan dihapus jika DRY_RUN=False")
    else:
        print(f"  Selesai! Berhasil: {success_count} | Gagal: {fail_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()