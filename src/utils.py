"""Helper function"""
import random
import time


def clean_price(price_str):
    """Convert price string to float e.g. '$99.88'> 99.88"""
    if price_str is None:
        return None
    return float(
        price_str.replace("Â", "")
        .replace("£", "")
        .replace("$", "")
        .replace(",", "")
        .strip()
    )


def delay(min_sec=1, max_sec=3):
    time.sleep(random.uniform(min_sec, max_sec))
