## This script will search for a list of keywords on Google and print the titles of the first few results for each keyword.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver
driver = webdriver.Chrome()

# List of search terms to automate
search_terms = ["Python programming", "Selenium automation", "Data Science", "Artificial Intelligence"]

# Loop through each search term
for term in search_terms:
    # Open Google
    driver.get("https://www.google.com")
    
    # Find the search box, enter the search term, and submit
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(term)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the results to load and display the titles of the first few results
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    
    print(f"\nSearch results for '{term}':")
    for i, result in enumerate(results[:5]):  # Limit to the first 5 results
        print(f"{i+1}. {result.text}")
        
# Close the browser
driver.quit()
