import sqlite3


DATABASE_FILE = "vehicles.db"


def create_database():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS vehicles (
            stock_number TEXT PRIMARY KEY,
            vehicle_name TEXT,
            color TEXT,
            vin TEXT,
            available_date TEXT,
            detail_url TEXT,
            image_url TEXT,
            lot_name TEXT,
            lot_url TEXT
        )
        """
    )

    connection.commit()
    connection.close()


def save_vehicle(vehicle):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT stock_number
        FROM vehicles
        WHERE stock_number = ?
        """,
        (vehicle["stock_number"],),
    )

    existing_vehicle = cursor.fetchone()

    if existing_vehicle is not None:
        connection.close()
        return False

    cursor.execute(
        """
        INSERT INTO vehicles (
            stock_number,
            vehicle_name,
            color,
            vin,
            available_date,
            detail_url,
            image_url,
            lot_name,
            lot_url
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            vehicle["stock_number"],
            vehicle["vehicle_name"],
            vehicle["color"],
            vehicle["vin"],
            vehicle["available_date"],
            vehicle["detail_url"],
            vehicle["image_url"],
            vehicle["lot_name"],
            vehicle["lot_url"],
        ),
    )

    connection.commit()
    connection.close()

    return True


def delete_vehicle(stock_number):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM vehicles
        WHERE stock_number = ?
        """,
        (stock_number,),
    )

    connection.commit()
    connection.close()