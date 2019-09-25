import re
import uuid
from typing import Dict
from bs4 import BeautifulSoup
from selenium import webdriver
from dataclasses import dataclass, field
from models.model import Model

@dataclass(eq=False)
class Item(Model):
    collection: str = field(init=False, default="items")
    url: str
    tag_name: str
    query: Dict
    price: float = field(default=None)
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def load_price(self) -> float:
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        chrome_driver_location = "C:\\Users\\Steve\\Documents\\OSU\\Side Projects\\Python\\chromedriver.exe"
        browser = webdriver.Chrome(chrome_driver_location, chrome_options=options)
        browser.get(self.url)
        page_html = browser.page_source

        soup = BeautifulSoup(page_html, "html.parser")
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        price_no_comma = string_price.replace(',', '')

        pattern = re.compile(r"(\d*\.?(\d\d))")
        match = pattern.search(price_no_comma)
        found_price = match.group(1)
        self.price = float(found_price)
        browser.close()
        return self.price

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "query": self.query,
            "price": self.price
        }
