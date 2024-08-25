## In this script, we'll automate the process of loading a product page on an e-commerce site with selenium, 
## click a button to load more products, and then scrape the product names and prices with bs4.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# Set up the WebDriver
driver = webdriver.Chrome()

# Open the e-commerce site
driver.get("https://example-ecommerce.com/products")

# Scroll down to load more products or click a 'Load More' button if necessary
load_more_button = driver.find_element(By.XPATH, "//button[text()='Load More']")
for _ in range(3):  # Click 'Load More' button 3 times to load more products
    load_more_button.click()
    time.sleep(2)  # Wait for the products to load (page load)

# Use Selenium to get the page source (HTML content of the page) after all products are loaded
page_source = driver.page_source

# Close the Selenium browser
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract product names and prices
products = soup.find_all('div', class_='product-item')

for product in products:
    product_name = product.find('h2', class_='product-title').text.strip()
    product_price = product.find('span', class_='product-price').text.strip()
    print(f"Product: {product_name}, Price: {product_price}")
