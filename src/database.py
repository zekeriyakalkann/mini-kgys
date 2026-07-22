import sqlite3
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "data" / "database.db"


# -------------------------------------------------
# Connection
# -------------------------------------------------

def get_connection():

    connection = sqlite3.connect(DATABASE_FILE)

    connection.row_factory = sqlite3.Row

    connection.execute("PRAGMA foreign_keys = ON")

    return connection


# -------------------------------------------------
# Database
# -------------------------------------------------

def create_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cameras (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            ip TEXT NOT NULL UNIQUE,

            status TEXT NOT NULL,

            last_ping REAL,

            last_http REAL,

            last_image TEXT,

            last_check TEXT

        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            camera_id INTEGER NOT NULL,

            event_type TEXT NOT NULL,

            description TEXT NOT NULL,

            event_time TEXT NOT NULL,

            FOREIGN KEY (camera_id)
            REFERENCES cameras(id)

        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alarms (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            camera_id INTEGER NOT NULL,

            alarm_type TEXT NOT NULL,

            severity TEXT NOT NULL,

            description TEXT NOT NULL,

            status TEXT NOT NULL,

            created_at TEXT NOT NULL,

            resolved_at TEXT,

            FOREIGN KEY (camera_id)
            REFERENCES cameras(id)

        )
    """)

    connection.commit()
    connection.close()


# -------------------------------------------------
# Create
# -------------------------------------------------

def add_camera(name, ip, status="UNKNOWN"):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO cameras
        (
            name,
            ip,
            status
        )
        VALUES (?, ?, ?)
    """, (name, ip, status))

    connection.commit()
    connection.close()


# -------------------------------------------------
# Read
# -------------------------------------------------

def get_all_cameras():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM cameras
        ORDER BY id
    """)

    cameras = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return cameras


def get_camera_by_id(camera_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM cameras
        WHERE id = ?
    """, (camera_id,))

    camera = cursor.fetchone()

    connection.close()

    if camera:
        return dict(camera)

    return None


def get_camera_status(camera_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT status
        FROM cameras
        WHERE id = ?
    """, (camera_id,))

    result = cursor.fetchone()

    connection.close()

    if result:
        return result["status"]

    return None


def camera_exists(ip):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM cameras
        WHERE ip = ?
    """, (ip,))

    exists = cursor.fetchone() is not None

    connection.close()

    return exists


# -------------------------------------------------
# Update
# -------------------------------------------------

def update_camera(camera_id, name, ip):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE cameras
        SET
            name = ?,
            ip = ?
        WHERE id = ?
    """, (name, ip, camera_id))

    connection.commit()
    connection.close()


def update_camera_status(camera_id, status):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE cameras
        SET status = ?
        WHERE id = ?
    """, (status, camera_id))

    connection.commit()
    connection.close()


def update_camera_monitoring(
    camera_id,
    status,
    ping_time,
    http_time,
    image_path
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE cameras
        SET

            status = ?,

            last_ping = ?,

            last_http = ?,

            last_image = ?,

            last_check = ?

        WHERE id = ?
    """, (

        status,

        ping_time,

        http_time,

        image_path,

        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        camera_id

    ))

    connection.commit()
    connection.close()


# -------------------------------------------------
# Delete
# -------------------------------------------------

def delete_camera(camera_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM cameras
        WHERE id = ?
    """, (camera_id,))

    connection.commit()
    connection.close()


# -------------------------------------------------
# Dashboard
# -------------------------------------------------

def get_camera_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM cameras
    """)

    count = cursor.fetchone()[0]

    connection.close()

    return count


def get_online_camera_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM cameras
        WHERE status = 'ONLINE'
    """)

    count = cursor.fetchone()[0]

    connection.close()

    return count


def get_offline_camera_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM cameras
        WHERE status = 'OFFLINE'
    """)

    count = cursor.fetchone()[0]

    connection.close()

    return count


def get_last_monitoring_time():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT MAX(last_check)
        FROM cameras
    """)

    result = cursor.fetchone()[0]

    connection.close()

    return result


def get_online_cameras():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM cameras
        WHERE status = 'ONLINE'
        ORDER BY name
    """)

    cameras = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return cameras


def get_offline_cameras():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM cameras
        WHERE status = 'OFFLINE'
        ORDER BY name
    """)

    cameras = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return cameras


def get_dashboard_cameras():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM cameras
        ORDER BY name
    """)

    cameras = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return cameras


def get_last_image_name(camera_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT last_image
        FROM cameras
        WHERE id = ?
    """, (camera_id,))

    result = cursor.fetchone()

    connection.close()

    if result is None:
        return "-"

    image_path = result["last_image"]

    if image_path is None:
        return "-"

    return Path(image_path).name


def get_dashboard_data():

    return {

        "camera_count": get_camera_count(),

        "online_count": get_online_camera_count(),

        "offline_count": get_offline_camera_count(),

        "last_check": get_last_monitoring_time()

    }

def get_active_alarms():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM alarms
        WHERE status = 'ACTIVE'
        ORDER BY created_at DESC
    """)

    alarms = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return alarms