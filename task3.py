def main():
    # User input sebuah angka
    angka = float(input("Masukkan sebuah angka: "))
    
    # Memeriksa angka < 100
    if angka < 100:
        print("Small")
    # Memeriksa angka diantara 100 dan 200
    elif 100 <= angka <= 200:
        print("Medium")
    # Jika angka > 200
    else:
        print("Large")

if __name__ == "__main__":
    main()
