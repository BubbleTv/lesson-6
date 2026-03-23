from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "landscape"))
    )
    
    driver.implicitly_wait(2)
    
    images = driver.find_elements(By.XPATH, "//img")
    
   
    expected_count = 4
    actual_count = len(images)
    
    if actual_count >= 3:
       
        third_image = images[2]
        src_value = third_image.get_attribute("src")
        
       
        print(f"SRC третьей картинки: {src_value}")
        print(f"Всего загружено картинок: {actual_count}")
    else:
        print(f"Ошибка: ожидалось минимум 3 картинки, загружено {actual_count}")
    
finally:
    driver.quit()
