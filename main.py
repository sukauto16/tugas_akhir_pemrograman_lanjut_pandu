from shape.circle import Circle
from shape.rectangle import Rectangle

def main():
    while True:
        print("Pilih bentuk yang ingin dihitung:")
        print("1. Lingkaran")
        print("2. Persegi Panjang")
        print("3. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3): ")
        
        if pilihan == '1':
            radius = float(input("Masukkan jari-jari lingkaran: "))
            circle = Circle(radius)
            print(f"Area Lingkaran: {circle.area()}")
            print(f"Keliling Lingkaran: {circle.perimeter()}")
        
        elif pilihan == '2':
            width = float(input("Masukkan lebar persegi panjang: "))
            height = float(input("Masukkan tinggi persegi panjang: "))
            rectangle = Rectangle(width, height)
            print(f"Area Persegi Panjang: {rectangle.area()}")
            print(f"Keliling Persegi Panjang: {rectangle.perimeter()}")
        
        elif pilihan == '3':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
        print("\n")

if __name__ == "__main__":
    main()
