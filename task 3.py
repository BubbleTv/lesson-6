from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("")
    button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
    button.click()
    
    green_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )
    text = green_label.text
    
    print(text)
    
finally:
    driver.quit()