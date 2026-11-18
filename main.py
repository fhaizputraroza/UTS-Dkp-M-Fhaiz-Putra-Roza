"""
UTS Dasar Komputer dan Pemrograman - Mini Project Individual
Kelompok B (Telekomunikasi): Monitoring Kualitas Sinyal / SNR

Nama : M. Fhaiz Putra Roza
NIM  : 03041382631163

Aturan status:
    SNR < 10 dB          -> RENDAH
    10 <= SNR < 20 dB    -> BAIK
    SNR >= 20 dB         -> SANGAT BAIK
"""

BATAS_RENDAH = 10        # dB, batas bawah kategori BAIK
BATAS_SANGAT_BAIK = 20   # dB, batas bawah kategori SANGAT BAIK

# 20 data SNR (dB): 15 data inti dari soal + 5 data tambahan
data_snr = [
    # --- 15 data inti (nilai sesuai soal) ---
    5, 8, 11, 14, 18, 22, 27, 9, 16, 24, 12, 30, 7, 20, 15,
    # --- 5 data tambahan (pilihan sendiri) ---
    2, 9.9, 10, 19.9, 35,
]


def kualitas_sinyal(snr):
    """Menentukan kategori kualitas sinyal dari nilai SNR (dB).

    Parameter:
        snr (float): nilai SNR dalam dB.
    Return:
        str: "RENDAH", "BAIK", atau "SANGAT BAIK".
    """
    if snr < BATAS_RENDAH:
        return "RENDAH"
    elif snr < BATAS_SANGAT_BAIK:
        return "BAIK"
    else:
        return "SANGAT BAIK"


def hitung_kategori(data):
    """Menghitung jumlah data pada setiap kategori kualitas sinyal.

    Parameter:
        data (list): daftar nilai SNR (dB).
    Return:
        dict: jumlah data per kategori.
    """
    jumlah = {"RENDAH": 0, "BAIK": 0, "SANGAT BAIK": 0}
    for snr in data:
        jumlah[kualitas_sinyal(snr)] += 1
    return jumlah


def rata_rata(data):
    """Menghitung nilai rata-rata dari daftar angka.

    Parameter:
        data (list): daftar angka.
    Return:
        float: rata-rata data.
    """
    return sum(data) / len(data)


def main():
    print("===== MONITORING KUALITAS SINYAL (SNR) =====")
    for nomor, snr in enumerate(data_snr, start=1):
        status = kualitas_sinyal(snr)
        print(f"{nomor:02d} SNR = {snr:5.1f} dB -> {status}")

    jumlah = hitung_kategori(data_snr)
    print()
    print("===== RINGKASAN =====")
    print(f"Total data       : {len(data_snr)}")
    print(f"RENDAH           : {jumlah['RENDAH']}")
    print(f"BAIK             : {jumlah['BAIK']}")
    print(f"SANGAT BAIK      : {jumlah['SANGAT BAIK']}")
    print(f"Rata-rata SNR    : {rata_rata(data_snr):.2f} dB")
    print(f"Maksimum SNR     : {max(data_snr):.1f} dB")
    print(f"Minimum SNR      : {min(data_snr):.1f} dB")


if __name__ == "__main__":
    main()
