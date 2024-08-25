# Web Scraping using Selenium

from selenium import webdriver

# Set up the webdriver
driver = webdriver.Chrome() 

# Navigate to the webpage
driver.get("https://www.example.com")

# Extract the title of the page
title = driver.title
print(title)

# Close the webdriver
driver.quit()
