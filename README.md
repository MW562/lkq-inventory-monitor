# LKQ Inventory Monitor

A Python application that monitors multiple LKQ Pick Your Part inventory pages for newly available vehicles and sends Discord notifications when matching vehicles are found.

## Features

- Monitors multiple LKQ locations
- Filters vehicles by make, model, and year range
- Stores seen vehicles in SQLite to prevent duplicate notifications
- Sends Discord webhook alerts for new matches
- Runs automatically on a Raspberry Pi using systemd
- Uses environment variables to protect sensitive configuration

## Technologies Used

- Python
- Requests
- BeautifulSoup
- SQLite
- Discord Webhooks
- Linux
- Raspberry Pi
- systemd
- Git and GitHub

## How It Works

1. The script requests inventory pages from configured LKQ locations.
2. BeautifulSoup parses vehicle details from the HTML.
3. Vehicles are checked against the configured watch list.
4. SQLite records previously seen stock numbers.
5. New matching vehicles trigger a Discord notification.
6. A systemd timer runs the script automatically every 15 minutes during configured hours.

## Project Structure

```text
LKQ-AlertScript/
├── config.py
├── database.py
├── filters.py
├── main.py
├── notifier.py
├── parser.py
├── requirements.txt
├── .env.example
└── README.md
