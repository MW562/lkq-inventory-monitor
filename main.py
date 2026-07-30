import requests
from bs4 import BeautifulSoup

from config import (
    DISCORD_WEBHOOK,
    HEADERS,
    LOTS,
    REQUEST_TIMEOUT,
)
from database import create_database, save_vehicle
from filters import is_watched_vehicle
from notifier import send_discord_notification
from parser import parse_vehicles


def download_lot_inventory(lot):
    response = requests.get(
        lot["url"],
        headers=HEADERS,
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    vehicles = parse_vehicles(soup)

    for vehicle in vehicles:
        vehicle["lot_name"] = lot["name"]
        vehicle["lot_url"] = lot["url"]

    return vehicles


def main():
    create_database()

    total_vehicles = 0
    matched_vehicles = 0
    new_vehicles = 0

    for lot in LOTS:
        print()
        print("Checking lot:", lot["name"])

        try:
            vehicles = download_lot_inventory(lot)
        except requests.RequestException as error:
            print("Failed to download lot:", error)
            continue

        total_vehicles += len(vehicles)

        print("Parsed vehicles:", len(vehicles))

        for vehicle in vehicles:
            if not is_watched_vehicle(vehicle):
                continue

            matched_vehicles += 1

            if save_vehicle(vehicle):
                new_vehicles += 1

                print(
                    "NEW MATCH:",
                    vehicle["vehicle_name"],
                    "-",
                    vehicle["lot_name"],
                )

                send_discord_notification(
                    DISCORD_WEBHOOK,
                    vehicle,
                )

    print()
    print("Total vehicles checked:", total_vehicles)
    print("Watched vehicles found:", matched_vehicles)
    print("New watched vehicles:", new_vehicles)


if __name__ == "__main__":
    main()