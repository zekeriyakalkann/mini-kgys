from database import get_all_cameras
from database import add_camera, camera_exists, get_all_cameras
from database import (
    add_camera,
    camera_exists,
    get_all_cameras,
    delete_camera,
    get_camera_by_id,
    update_camera
)

from logger import info

def list_cameras():

    cameras = get_all_cameras()

    for camera in cameras:

        print(f"\nID: {camera['id']}")
        print(f"İsim: {camera['name']}")
        print(f"IP: {camera['ip']}")
        print(f"Durum: {camera['status']}")


def get_camera_count():

    cameras = get_all_cameras()

    return len(cameras)

def create_camera():

    name = input("\nKamera Adi: ")
    ip = input("IP Adresi: ")

    if camera_exists(ip):

        print("\nBu IP adresi zaten kayitli.")
        return

    add_camera(name, ip, "UNKNOWN")

    info(f"Yeni kamera eklendi: {name}")

    print("\nKamera basariyla eklendi.")

def delete_camera_menu():

    camera_id = input("\nSilinecek Kamera ID: ")

    cameras = get_all_cameras()

    found = False

    for camera in cameras:

        if camera["id"] == int(camera_id):

            found = True
            break

    if not found:

        print("\nBu ID'ye ait kamera bulunamadi.")
        return

    delete_camera(int(camera_id))

    info(f"Kamera silindi. ID: {camera_id}")

    print("\nKamera basariyla silindi.")

def update_camera_menu():

    camera_id = input("\nGuncellenecek Kamera ID: ")

    if not camera_id.isdigit():

        print("\nGecersiz ID.")
        return

    camera = get_camera_by_id(int(camera_id))

    if camera is None:

        print("\nBu ID'ye ait kamera bulunamadi.")
        return

    print(f"\nMevcut Isim : {camera['name']}")
    print(f"Mevcut IP   : {camera['ip']}")

    new_name = input("\nYeni Kamera Adi (Bos birak = degismesin): ")

    new_ip = input("Yeni IP Adresi (Bos birak = degismesin): ")

    if new_name == "":

        new_name = camera["name"]

    if new_ip == "":

        new_ip = camera["ip"]

    if new_ip != camera["ip"]:

        if camera_exists(new_ip):

            print("\nBu IP adresi zaten kayitli.")

            return

    update_camera(

        int(camera_id),

        new_name,

        new_ip

    )

    info(f"Kamera guncellendi. ID: {camera_id}")

    print("\nKamera basariyla guncellendi.")