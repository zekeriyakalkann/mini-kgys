from menu import show_menu
from camera import list_cameras, get_camera_count


def main():

    while True:

        choice = show_menu()

        if choice == "1":
            list_cameras()

        elif choice == "2":
            print("\n=== SISTEM BILGISI ===")
            print(f"Toplam Kamera Sayisi: {get_camera_count()}")

        elif choice == "0":
            print("\nMini KGYS kapatiliyor...")
            break

        else:
            print("\nGecersiz secim!")


if __name__ == "__main__":
    main()