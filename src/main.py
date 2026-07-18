from database import create_database
from monitoring import check_cameras
from logger import info
from menu import show_menu
from camera import (
    list_cameras,
    get_camera_count,
    create_camera,
    delete_camera_menu,
    update_camera_menu
)


def main():
    
    create_database()

    while True:

        choice = show_menu()

        if choice == "1":
            info("Kamera listesi goruntulendi")
            list_cameras()


        elif choice == "2":
            print("\n=== SISTEM BILGISI ===")
            print(f"Toplam Kamera Sayisi: {get_camera_count()}")

        elif choice == "3":

            check_cameras()
            print("\nKamera durumlari guncellendi.")

        elif choice == "4":
            
            create_camera()

        elif choice == "5":

            delete_camera_menu()

        elif choice == "6":

            update_camera_menu()
            
        elif choice == "0":
            print("\nMini KGYS kapatiliyor...")
            break

        else:
            print("\nGecersiz secim!")


if __name__ == "__main__":
    main()