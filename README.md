# Product Price Tracker

A Python-based Product Price Tracker that scrapes product pages, stores historical prices in a CSV file, and detects price changes (increase, decrease, or no change) over time.

## This project is implemented as a modular, script-based tracker and is currently demonstrated using the demo website BooksToScrape.

## Features (Implemented)

- Scrape current product prices from web pages

- Track prices across multiple runs

- Store price history in a CSV file

- Detect price changes:

  - First scrape
  - Price increase
  - Price decrease
  - No change

- Built-in random delay to reduce aggressive requests

---

## Example Use Case

This tool can be used to:

- Track product prices for e-commerce monitoring
- Detect discounts and price drops
- Automate price tracking for research or analysis

## How It Works

- Product URLs are defined in product_links.py

- main.py loops through each URL

- scraper.py fetches the product page and extracts the price

- tracker.py:

- Reads the last stored price from prices.csv
- Compares it with the newly scraped price
- Updates the CSV file

- Results are printed to the console

---

## Tech Stack

- **Language**: Python

- **Web Scraping**: BeautifulSoup, Requests (Playwright/Selenium if needed)

- **Data Storage**: CSV / SQLite

- **Environment**: Virtualenv

- **Version Control**: Git & GitHub

---

## Project Structure

```
product-price-tracker/
│
├── src/
│   ├── scraper.py        # Core logic for fetching and parsing HTML content
│   ├── tracker.py        # Logic for comparing prices and updating the CSV database
│   └── utils.py          # Helper functions (clean price, delay, retries)
│
├── product_links.py      # List of product URLs
├── main.py               # Entry point: loops through URLs and runs tracker
├── prices.csv            # Stores historical prices (created automatically)
├── requirements.txt      # Project dependencies
└── README.md

```

---

## File Overview

### scraper.py

- Uses requests and BeautifulSoup

- Extracts product price using a CSS selector

- Selector is site-specific and can be changed per website

- Adds a random delay after each successful scrape

---

### tracker.py

- Manages CSV-based price storage

- Columns used:

  - product_url
  - last_price
  - price

- Compares old vs new prices and returns status + difference

---

### utils.py

- clean_price() – Converts price strings into float values

- delay() – Adds a random delay between requests to reduce server load

---

### product_links.py

- Contains a Python list of product URLs to track

---

### main.py

- Orchestrates the entire flow

- Calls scraper, tracker, and comparison logic

- Prints readable output to the console

---

## Setup Instructions

- Clone the repository

- Create and activate a virtual environment

- Install the required Python libraries:

```
pip install -r requirements.txt
```

- Your requirements.txt should include:

```
beautifulsoup4
requests
pandas
```

## Usage

- Add the product URLs you want to track in product_links.py:

```
products = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
]
```

- Run the tracker:

```
python main.py
```

- On first run, prices.csv will be created with current prices.

- On subsequent runs, it will fill last_price and compare price changes.

---

### Output

- The CSV will have this structure:

```
product_url,last_price,price
https://example.com/p1,,49.99           # First run
https://example.com/p1,49.99,47.50      # Next run after price change

```

- last_price: previous run value

- price: current run value

---

## Current Limitations

- Price selector must be manually adjusted per website

- Uses CSV instead of a database

- No alert system (email / Telegram) yet

---

## Planned Improvements

- Config-based selectors for multiple websites

- Logging instead of print statements

- Timestamped price history

- Email / Telegram alerts

- Optional SQLite database support

- Basic price trend visualization

---

## Project Status

- Core scraping logic implemented

- CSV-based price tracking working

- Tested on BooksToScrape demo website

- Actively improving and refactoring

---

## License

MIT License

---

## Disclaimer

This project is intended for responsible and ethical web scraping. Users are responsible for ensuring compliance with the terms of service of the websites being scraped.

---
