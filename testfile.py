from bs4 import BeautifulSoup
from selenium import webdriver
import re


# test links

#url = "https://www.amiami.com/eng/detail?scode=FIGURE-051943&rank="
#tag_name = "span"
#query = {"class":"item-detail__price_selling-price"}

#url = "https://www.gundamplanet.com/1-10-gundam-girls-generation-mirai-kamiki.html"
#tag_name = "span"
#query = {"class":"price"}

#url = "https://www.rei.com/product/895780/kelty-redwing-44-pack-mens"
#tag_name = "span"
#query = {"class":"product-current-price"}


url = "http://www.cdjapan.co.jp/product/VVCL-1493"
tag_name = "div"
query = {"class":"price-exchange"}


# working
wurl = "https://otakumode.com/shop/5bf617f7b59f18ff1e5bb18e/Saekano-How-to-Raise-a-Boring-Girlfriend-Flat-Michiru-Hyodo-Swimsuit-Ver-1-7-Scale-Figure"
wtag_name = "span"
wquery = {"class":"p-price__price"}


options = webdriver.ChromeOptions()
options.add_argument("headless")

chrome_driver_location = "C:\\Users\\Steve\\Documents\\OSU\\Side Projects\\Python\\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver_location, chrome_options=options)
browser.get(url)
page_html = browser.page_source

soup = BeautifulSoup(page_html, "html.parser")
#print(soup.prettify())
element = soup.find(tag_name, query)
#print('element is' + element.text)
string_price = element.text.strip()
price_no_comma = string_price.replace(',', '')

pattern = re.compile(r"(\d*\.?(\d\d))")
match = pattern.search(price_no_comma)

found_price = match.group(1)
price = float(found_price)

browser.close()
print(price)