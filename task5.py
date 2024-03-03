def main():
    # Deklarasi variabel total
    total = 0
    
    # Input angka
    print("Masukkan angka-angka (ketik -1 untuk mengakhiri):")
    while True:
        inputan = input()
        if inputan == "-1":
            break
        # Jika input dalam bentuk array dipisahkan berdasarkan spasi
        angka_list = inputan.split()  
        for angka in angka_list:
            total += int(angka)
    
    # Output total
    print("Jumlah dari semua angka yang dimasukkan adalah:", total)

if __name__ == "__main__":
    main()
