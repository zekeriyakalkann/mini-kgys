import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "data" / "database.db"

def create_database():

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cameras (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            ip TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_camera(name, ip, status):

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO cameras (name, ip, status)
        VALUES (?, ?, ?)
    """, (name, ip, status))

    connection.commit()
    connection.close()


def get_all_cameras():

    connection = sqlite3.connect(DATABASE_FILE)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM cameras
    """)

    rows = cursor.fetchall()

    cameras = [dict(row) for row in rows]

    connection.close()

    return cameras


def update_camera_status(camera_id, status):

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE cameras
        SET status = ?
        WHERE id = ?
    """, (status, camera_id))

    connection.commit()

    connection.close()

def camera_exists(ip):

    connection = sqlite3.connect(DATABASE_FILE)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM cameras
        WHERE ip = ?
    """, (ip,))

    camera = cursor.fetchone()

    connection.close()

    return camera is not None

def delete_camera(camera_id):

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM cameras
        WHERE id = ?
    """, (camera_id,))

    connection.commit()

    connection.close()

def get_camera_by_id(camera_id):

    connection = sqlite3.connect(DATABASE_FILE)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM cameras
        WHERE id = ?
    """, (camera_id,))

    camera = cursor.fetchone()

    connection.close()

    if camera:

        return dict(camera)

    return None


def update_camera(camera_id, name, ip):

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE cameras
        SET name = ?, ip = ?
        WHERE id = ?
    """, (name, ip, camera_id))

    connection.commit()

    connection.close()