# Product Price Tracker

Product Price Tracker is a Python-based tool designed to scrape, track, and monitor product prices across e-commerce websites. It helps businesses and individuals monitor price changes, discounts, and trends over time in an automated and reliable way.
This project is currently under development.

---

## Project Objectives

- Scrape product prices from e-commerce websites

- Track and store historical price data

- Detect price changes over time

- Provide insights into price trends
----

## Planned Features

- Web scraping using Python

- Support for multiple e-commerce websites

- Price history tracking

- Price change detection

- (Optional) Price drop alerts

- (Optional) Data visualization
----

## Tech Stack

- Language: Python

- Web Scraping: BeautifulSoup, Requests (Playwright/Selenium if needed)

- Data Storage: CSV / SQLite

- Environment: Virtualenv

- Version Control: Git & GitHub
----

## Project Status

- Project planning completed

- Coding not started yet

- Initial price scraper implementation
----

## Planned Project Structure
```
product-price-tracker/
│
├── src/
│   ├── scraper.py        # Scrape product pages for current price
│   ├── tracker.py        # Compare new vs old prices
│   └── utils.py          # Helper functions (clean price, delay, retries)
│
├── product_links.py      # List of product URLs
├── main.py               # Entry point: loops through URLs and runs tracker
├── prices.csv            # Stores historical prices (created automatically)
├── requirements.txt
└── README.md

```
----
## Setup (Coming Soon)

Setup instructions will be added once development begins.

----

## License

MIT License

---
## Disclaimer

This project is intended for responsible and ethical web scraping. Users are responsible for ensuring compliance with the terms of service of the websites being scraped.

---