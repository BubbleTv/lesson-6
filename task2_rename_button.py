from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")
    
    input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
    input_field.send_keys("SkyPro")
    
    update_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    update_button.click()
    button_text = update_button.text
    print(button_text)
    
finally:

    driver.quit()