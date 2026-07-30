WATCH_LIST = [
    {
        "make": "VOLVO",
        "model": "940",
    },
    {
	"make": "VOLVO",
	"model": "740",
    },
    {
	"make": "VOLVO",
	"model": "960",
    },
    {
        "make": "VOLKSWAGEN",
        "model": "JETTA",
        "min_year": 1999,
        "max_year": 2005,
    },
    {
        "make": "VOLKSWAGEN",
        "model": "JETTA",
        "min_year": 2011,
        "max_year": 2018,
    }
]

def split_vehicle_name(vehicle_name):
    parts = vehicle_name.upper().split(maxsplit=2)

    if len(parts) < 3:
        return None

    try:
        year = int(parts[0])
    except ValueError:
        return None

    make = parts[1]
    model = parts[2]

    return {
        "year": year,
        "make": make,
        "model": model,
    }


def matches_filter(vehicle, rule):
    vehicle_details = split_vehicle_name(vehicle["vehicle_name"])

    if vehicle_details is None:
        return False

    year = vehicle_details["year"]
    make = vehicle_details["make"]
    model = vehicle_details["model"]

    if "make" in rule:
        if make != rule["make"].upper():
            return False

    if "model" in rule:
        if rule["model"].upper() not in model:
            return False

    if "min_year" in rule:
        if year < rule["min_year"]:
            return False

    if "max_year" in rule:
        if year > rule["max_year"]:
            return False

    return True


def is_watched_vehicle(vehicle):
    if not WATCH_LIST:
        return True

    for rule in WATCH_LIST:
        if matches_filter(vehicle, rule):
            return True

    return False
