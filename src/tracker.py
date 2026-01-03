"""Compare new vs old prices and track changes."""

import os
import pandas as pd


def get_last_price(url, csv_file="prices.csv"):
    """Retrieve old price from CSV"""
    if not os.path.exists(csv_file):
        return None
    try:

        df = pd.read_csv(csv_file)
    except pd.errors.EmptyDataError:
        return None
    row = df[df["product_url"] == url]
    if row.empty:
        return None
# We pull from "price" because that's where the last scrape ended up
    return row.iloc[0]["price"]


def save_price(url, new_scraped_price, csv_file="prices.csv"):
    """Save new price to CSV"""
    try:
        df = pd.read_csv(csv_file)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=["product_url", "last_price", "price"])
    if url in df["product_url"].values:
        # 1. Take what is currently in 'price' and move it to 'last_price'
        old_val = df.loc[df["product_url"] == url, "price"].values[0]
        df.loc[df["product_url"] == url, "last_price"] = old_val
        # 2. Update 'price' with the new scrape
        df.loc[df["product_url"] == url, "price"] = new_scraped_price
    else:
        new_row = pd.DataFrame(
            {"product_url": [url], "last_price": [None], "price": [new_scraped_price]}
        ).astype({"last_price": "float64", "price": "float64"})
        df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(csv_file, index=False)


def compare_price(last_price, new_scraped_price):
    """Compare old vs new price and return status + change"""
    if last_price is None:
        return "first_scrape", 0
    if new_scraped_price < last_price:
        return "decrease", round(last_price - new_scraped_price, 2)
    if new_scraped_price > last_price:
        return "increase", round(new_scraped_price - last_price, 2)

    return "no_change", 0
