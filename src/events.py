from datetime import datetime

from database import get_connection


# -------------------------------------------------
# Create
# -------------------------------------------------

def add_event(
    camera_id,
    event_type,
    description
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO events
        (
            camera_id,
            event_type,
            description,
            event_time
        )
        VALUES (?, ?, ?, ?)
    """, (

        camera_id,

        event_type,

        description,

        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

    connection.commit()
    connection.close()


# -------------------------------------------------
# Read
# -------------------------------------------------

def get_all_events():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM events
        ORDER BY event_time DESC
    """)

    events = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return events


def get_last_events(limit=10):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM events
        ORDER BY event_time DESC
        LIMIT ?
    """, (limit,))

    events = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return events


def get_event_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM events
    """)

    count = cursor.fetchone()[0]

    connection.close()

    return count


# -------------------------------------------------
# Delete
# -------------------------------------------------

def clear_events():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM events
    """)

    connection.commit()
    connection.close()