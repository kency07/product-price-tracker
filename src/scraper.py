"""scraping function"""
import requests
from bs4 import BeautifulSoup
from src.utils import clean_price, delay


def scrape_price(url):
    """Scrape current price from product page"""
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # TODO: Update this selector for the target site

        price_tag = soup.find("p", class_="price_color")
        if price_tag is None:
            print("price not found on the page")
            return None
        price_str = price_tag.text
        price = clean_price(price_str)

        delay()
        return price
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None
