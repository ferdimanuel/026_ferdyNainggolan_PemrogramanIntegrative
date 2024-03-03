def main():
    # User input angka
    angka = int(input("Masukkan sebuah angka: "))
    
    # Mendeklarasikan variabel total
    total = 0
    
    # Melakukan loop dari 1 sampai angka yang di input
    for i in range(1, angka + 1):
        total += i
    
    # Output total
    print("Jumlah semua nilai dari 1 hingga", angka, "adalah:", total)

if __name__ == "__main__":
    main()
