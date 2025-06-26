from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# You must have chromedriver installed and available in PATH
driver = webdriver.Chrome()

try:
    # Open the frontend (served with http.server or Live Server)
    driver.get("http://localhost:5500")  # Adjust if using a different port

    # Find the input field and type a keyword
    input_field = driver.find_element(By.ID, "keyword")
    input_field.send_keys("Farmers")

    # Click the search button
    driver.find_element(By.TAG_NAME, "button").click()

    # Wait for results to load
    time.sleep(5)

    # Get result items
    results = driver.find_elements(By.TAG_NAME, "li")

    assert len(results) > 0
    print(f"✅ {len(results)} results loaded successfully.")

    # Print out first few headlines
    for item in results[:3]:
        print("🔹", item.text)

finally:
    driver.quit()
