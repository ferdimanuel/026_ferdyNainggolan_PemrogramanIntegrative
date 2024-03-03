def main():
    # Input bil. bulat dari pengguna
    bil_bulat = int(input("Masukkan bilangan bulat: "))
    
    # Membagi bil. bulat dengan 3
    hasil = bil_bulat / 3
    
    # Memeriksa hasil apakah desimal
    if hasil.is_integer():
        # Jika tidak print hasil
        print("Hasil:", int(hasil))
    else:
        # Jika ya dibulatkan ke 3 bil. desimal
        print("Hasil:", "{:.3f}".format(hasil))

if __name__ == "__main__":
    main()
