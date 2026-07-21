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


def print_banner():

    print("\n========================================")
    print("          MINI-KGYS v1.0")
    print("========================================")


def initialize_system():

    print("\nInitializing System...")

    create_database()

    print("Database      : OK")
    print("System        : READY")


def show_system_info():

    print("\n=========== SYSTEM INFO ===========")

    print(f"Camera Count : {get_camera_count()}")

    print("===================================")


def start_monitoring():

    print("\nStarting Monitoring...\n")

    check_cameras()

    print("\nMonitoring Completed.")


def main():

    print_banner()

    initialize_system()

    show_system_info()

    while True:

        choice = show_menu()

        if choice == "1":

            info("Kamera listesi goruntulendi")

            list_cameras()

        elif choice == "2":

            show_system_info()

        elif choice == "3":

            start_monitoring()

        elif choice == "4":

            create_camera()

        elif choice == "5":

            delete_camera_menu()

        elif choice == "6":

            update_camera_menu()

        elif choice == "0":

            print("\nMini-KGYS kapatiliyor...")

            break

        else:

            print("\nGecersiz secim!")


if __name__ == "__main__":

    main()