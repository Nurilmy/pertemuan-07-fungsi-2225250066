

def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    print("\n=== MENU PROGRAM ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1..n")
    print("4. Faktorial")
    print("5. Keluar")


def program_utama():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi (1-5): ")

        if pilihan == "1":
            p = float(input("Masukkan panjang: "))
            l = float(input("Masukkan lebar: "))
            print("Luas persegi panjang =", luas_persegi_panjang(p, l))

        elif pilihan == "2":
            a = float(input("Masukkan alas: "))
            t = float(input("Masukkan tinggi: "))
            print("Luas segitiga =", luas_segitiga(a, t))

        elif pilihan == "3":
            n = int(input("Masukkan n: "))
            if n < 1:
                print("n harus minimal 1.")
            else:
                print("Jumlah 1..n =", jumlah_n(n))

        elif pilihan == "4":
            n = int(input("Masukkan n: "))
            if n < 0:
                print("n tidak boleh negatif.")
            else:
                print("Faktorial =", faktorial(n))

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")


if __name__ == "__main__":
    program_utama()
