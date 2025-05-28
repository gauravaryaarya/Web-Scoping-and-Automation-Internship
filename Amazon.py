from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from urllib.parse import urlparse, urljoin

options = Options()
options.headless = True
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = "https://www.amazon.in/"
driver.get(base_url)

time.sleep(3)

elements = driver.find_elements("tag name", "a")
all_links = set()

for element in elements:
    href = element.get_attribute("href")
    if href:
        href = urljoin(base_url, href)
        parsed = urlparse(href)
        if "amazon.in" in parsed.netloc:
            clean_link = parsed.scheme + "://" + parsed.netloc + parsed.path
            all_links.add(clean_link)

driver.quit()

with open("unique_amazon_links.txt", "w", encoding="utf-8") as f:
    for link in sorted(all_links):
        f.write(link + "\n")

print(f" {len(all_links)} unique links collected and saved to 'unique_amazon_links.txt'")
