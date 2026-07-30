# LKQ Inventory Monitor

A Python application that monitors multiple LKQ Pick Your Part inventory locations for newly available vehicles, and automatically sends Discord notifications when vehicles matching user-defined filters are found.

This project was built to solve a real-world problem: manually checking multiple LKQ inventory pages throughout the day for specific vehicles. Instead of refreshing websites repeatedly, the application performs the monitoring automatically and only alerts the user when new matching inventory appears.

---

## Features

- Monitor multiple LKQ Pick Your Part locations
- Filter vehicles by make, model, and year
- Store previously seen vehicles in a SQLite database
- Prevent duplicate notifications
- Send Discord webhook notifications for new matching vehicles
- Deploy on a Raspberry Pi for continuous operation
- Automatically run on a schedule using systemd timers
- Configure sensitive information using environment variables

---

## How It Works

```
             LKQ Inventory Pages
                     │
                     ▼
          Download HTML with Requests
                     │
                     ▼
      Parse Vehicle Data (BeautifulSoup)
                     │
                     ▼
      Compare Against Watch List Filters
                     │
                     ▼
       Check SQLite Database for Duplicates
                     │
          ┌──────────┴──────────┐
          │                     │
     Already Seen          New Vehicle
          │                     │
          ▼                     ▼
      Ignore Entry       Send Discord Alert
```

---

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- SQLite
- Discord Webhooks
- Raspberry Pi
- Linux
- systemd
- Git
- GitHub

---

## Project Structure

```
LKQ-AlertScript/
│
├── main.py              # Main application logic
├── parser.py            # HTML parsing
├── database.py          # SQLite database functions
├── filters.py           # Vehicle filtering
├── notifier.py          # Discord notifications
├── config.py            # Configuration values
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/lkq-inventory-monitor.git

cd lkq-inventory-monitor
```

Create a virtual environment.

```bash
python3 -m venv .venv
```

Activate it.

Linux / Raspberry Pi

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file from the example.

```bash
cp .env.example .env
```

Add your Discord webhook.

```env
DISCORD_WEBHOOK=https://discord.com/api/webhooks/your-webhook
```

Configure the inventory locations and vehicle filters inside the project.

Example vehicle filter:

```python
WATCH_LIST = [
    {
        "make": "Volvo",
        "model": "940",
        "min_year": 1991,
        "max_year": 1995,
    }
]
```

---

## Running the Application

Run manually.

```bash
python main.py
```

Or run using the configured systemd service.

```bash
sudo systemctl start lkq-alert.service
```

View logs.

```bash
journalctl -u lkq-alert.service -f
```

---

## Raspberry Pi Deployment

This application is designed to run continuously on a Raspberry Pi.

A systemd timer automatically executes the scraper every 15 minutes during configured operating hours, allowing the system to monitor inventory without user interaction.

---

## Example Notification

![Discord Notification](images/Notification.png)

---

### Preventing Duplicate Notifications

A SQLite database stores previously discovered stock numbers. Before sending a notification, each vehicle is checked against the database to ensure that alerts are only sent once.

### Long-Term Deployment

Rather than running only from a development computer, the application was deployed to a Raspberry Pi using Linux systemd services and timers so it can operate continuously with no user interaction.

### Secure Configuration

Sensitive information such as Discord webhook URLs is stored using environment variables instead of being hardcoded into the source code.

---

## Lessons Learned

Building this project provided hands-on experience with:

- Designing a complete Python application
- Parsing real-world HTML data
- Working with SQLite databases
- Deploying applications on Linux
- Scheduling automated tasks using systemd
- Managing project configuration securely
- Using Git and GitHub for version control

---

## Disclaimer

This project is intended for educational and personal use.

It is not affiliated with, endorsed by, or maintained by LKQ Corporation.
