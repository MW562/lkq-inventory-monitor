from urllib.parse import urljoin


BASE_URL = "https://www.pyp.com"


def parse_vehicle(vehicle_row):
    vehicle_name_element = vehicle_row.select_one("a.pypvi_ymm")

    if vehicle_name_element is None:
        return None

    vehicle_name = vehicle_name_element.get_text(" ", strip=True)
    stock_number = vehicle_row.get("id", "")

    color = ""
    vin = ""

    for item in vehicle_row.select(".pypvi_detailItem"):
        text = item.get_text(" ", strip=True)

        if text.startswith("Color:"):
            color = text.replace("Color:", "", 1).strip()

        elif text.startswith("VIN:"):
            vin = text.replace("VIN:", "", 1).strip()

    available_element = vehicle_row.select_one("time")

    available_date = (
        available_element.get_text(" ", strip=True)
        if available_element
        else ""
    )

    detail_path = vehicle_name_element.get("href", "")
    detail_url = urljoin(BASE_URL, detail_path)

    image_element = vehicle_row.select_one("a.pypvi_image img")

    image_url = (
        image_element.get("src", "")
        if image_element
        else ""
    )

    return {
        "vehicle_name": vehicle_name,
        "stock_number": stock_number,
        "color": color,
        "vin": vin,
        "available_date": available_date,
        "detail_url": detail_url,
        "image_url": image_url,
    }


def parse_vehicles(soup):
    vehicle_rows = soup.select("div.pypvi_resultRow")
    vehicles = []

    for vehicle_row in vehicle_rows:
        vehicle = parse_vehicle(vehicle_row)

        if vehicle is not None:
            vehicles.append(vehicle)

    return vehicles