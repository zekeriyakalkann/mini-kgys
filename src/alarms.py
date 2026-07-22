from datetime import datetime
from database import get_connection

def create_alarm(
    camera_id,
    alarm_type,
    severity,
    description
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO alarms
        (
            camera_id,
            alarm_type,
            severity,
            description,
            status,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (

        camera_id,

        alarm_type,

        severity,

        description,

        "ACTIVE",

        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

    connection.commit()
    connection.close()

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

def active_alarm_exists(camera_id, alarm_type):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM alarms
        WHERE camera_id = ?
          AND alarm_type = ?
          AND status = 'ACTIVE'
    """, (

        camera_id,
        alarm_type

    ))

    exists = cursor.fetchone() is not None

    connection.close()

    return exists


def get_active_alarm_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM alarms
        WHERE status = 'ACTIVE'
    """)

    count = cursor.fetchone()[0]

    connection.close()

    return count