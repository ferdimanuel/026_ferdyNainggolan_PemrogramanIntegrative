import math

def main():
    # User input gaji tahunan
    gaji_tahunan = float(input("Masukkan gaji tahunan Anda: "))
    
    # Menghitung gaji bulanan
    gaji_bulanan = gaji_tahunan / 12
    
    # Membulatkan gaji bulanan
    gaji_bulanan_bulat = math.ceil(gaji_bulanan)
    
    # Output gaji bulanan
    print("Gaji bulanan Anda adalah:", gaji_bulanan_bulat)

if __name__ == "__main__":
    main()
