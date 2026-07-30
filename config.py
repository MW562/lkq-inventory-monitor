import os

from dotenv import load_dotenv


load_dotenv()

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
REQUEST_TIMEOUT = 30

LOTS = [
    {
        "name": "Ontario",
        "url": "https://www.pyp.com/inventory/ontario-1280/",
    },
    {
        "name": "Anaheim",
        "url": "https://www.pyp.com/inventory/anaheim-1265/",
    },
    {
        "name": "Bloomington",
        "url": "https://www.pyp.com/inventory/rialto-1284/"
    },
    {
        "name": "Fontana",
        "url": "https://www.pyp.com/inventory/fontana-1285/"
    },
    {
        "name": "Hesperia",
        "url": "https://www.pyp.com/inventory/hesperia-1292/"
    },
    {
        "name": "Monrovia",
        "url": "https://www.pyp.com/inventory/monrovia-1281/"
    },
    {
        "name": "Riverside",
        "url": "https://www.pyp.com/inventory/riverside-1290/"
    },
    {
        "name": "San-Bernardino",
        "url": "https://www.pyp.com/inventory/san-bernardino-1291/"
    },
    {
        "name": "Victorville",
        "url": "https://www.pyp.com/inventory/victorville-1287/"
    },
    {
        "name": "Wilmington",
        "url": "https://www.pyp.com/inventory/wilmington-help-yourself-1262/"
    }
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,image/apng,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.pyp.com/",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
}


if not DISCORD_WEBHOOK:
    raise RuntimeError(
        "DISCORD_WEBHOOK was not found. Check your .env file."
    )