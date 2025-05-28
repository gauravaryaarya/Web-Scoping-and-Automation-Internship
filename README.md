# Web-Scoping-and-Automation-Internship
# Amazon Unique Links

This uses **Python + Selenium** to extract all **unique internal links** from the homepage of [Amazon India](https://www.amazon.in/).

---

## 🛠️ Tech Stack

- **Python**
- **Selenium** 
- **webdriver-manager** 
- **Chrome Headless Mode**

---

## How It Works

1. The script launches a headless Chrome browser.
2. It loads the Amazon India homepage (`https://www.amazon.in/`).
3. All anchor (`<a>`) tags are collected.
4. Links are cleaned and filtered to include only **internal** Amazon URLs.
5. All **unique** links are saved in a file `unique_amazon_links.txt`.


