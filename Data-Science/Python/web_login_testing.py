from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver
driver = webdriver.Chrome()

# Open the web application
driver.get("https://example.com/login")

# Find the username and password fields and enter data
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("testuser")
password.send_keys("testpassword")

# Submit the login form
password.send_keys(Keys.RETURN)

# Check if login was successful by looking for a specific element
try:
    driver.find_element(By.ID, "welcome-message")
    print("Login test passed.")
except:
    print("Login test failed.")

# Close the browser
driver.quit()
