from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.demoblaze.com')

link = driver.find_element(By.LINK_TEXT, "Log in")
link.click()

time.sleep(5)

username = driver.find_element(By.ID, 'loginusername')
username.send_keys("Karolina123")

time.sleep(8)

password = driver.find_element(By.ID, 'loginpassword')
password.send_keys("haslo123")


time.sleep(8)

pagelocat = driver.find_element(By.ID, 'logInModal')
loc2 = pagelocat.find_element(By.CLASS_NAME, 'modal-dialog')
loc3 = loc2.find_element(By.CLASS_NAME, 'modal-content')
loc4 = loc3.find_element(By.CLASS_NAME, 'modal-footer')
button = loc4.find_element(By.CLASS_NAME, 'btn.btn-primary')
button.click()

time.sleep(20)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "logout2")))

try:

    logout_button = driver.find_element(By.ID, "logout2")
    assert logout_button.is_displayed(), "Użytkownik nie jest zalogowany"
    print("Użytkownik jest zalogowany!")
except AssertionError as e:
    print(e)

driver.quit()