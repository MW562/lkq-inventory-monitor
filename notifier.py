import requests


def send_discord_notification(webhook_url, vehicle):
    message = {
        "content": (
            f"New watched vehicle found!\n"
            f"**{vehicle['vehicle_name']}**\n"
            f"Lot: {vehicle['lot_name']}\n"
            f"Stock: {vehicle['stock_number']}\n"
            f"Color: {vehicle['color']}\n"
            f"VIN: {vehicle['vin']}\n"
            f"Available: {vehicle['available_date']}\n"
            f"{vehicle['detail_url']}"
        )
    }

    response = requests.post(
        webhook_url,
        json=message,
        timeout=30,
    )

    response.raise_for_status()