""" Main Execution Script for [product-price-tracker]"""

from product_links import products
from src.scraper import scrape_price
from src.tracker import compare_price, save_price, get_last_price


for url in products:
    last_price = get_last_price(url)  # from CSV/DB
    print(f"processing: {url}")
    new_scraped_price = scrape_price(url)
    if new_scraped_price is None:
        continue

    status, change = compare_price(last_price, new_scraped_price)
    save_price(url, new_scraped_price)

    if status == "decrease":
        print(f"price decrease by ${change}")

    elif status == "increase":
        print(f"price increase by ${change}")

    elif status == "first_scrape":
        print(f"First time scraping this product. Current price: ${new_scraped_price}")
    else:
        print("no change in price")
