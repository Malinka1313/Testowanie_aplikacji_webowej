from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.demoblaze.com')

link = driver.find_element(By.LINK_TEXT, "Contact")
link.click()

time.sleep(5)

contactmail = driver.find_element(By.ID, 'recipient-email')
contactmail.send_keys("testing@naszafirma.com")

time.sleep(8)

contactname = driver.find_element(By.ID, 'recipient-name')
contactname.send_keys("Anna Nowak")

time.sleep(8)

message = driver.find_element(By.ID, 'message-text')
message.send_keys("Czy można prosić o rabat przy zakupie monitora ASUS Full HD?")

time.sleep(8)

loc1 = driver.find_element(By.CLASS_NAME, 'modal-open')
loc2 = loc1.find_element(By.ID, 'exampleModal')
loc3 = loc2.find_element(By.CLASS_NAME, 'modal-dialog')
loc4 = loc3.find_element(By.CLASS_NAME, 'modal-content')
buttonsend = loc4.find_element(By.CLASS_NAME, 'btn.btn-primary')
buttonsend.click()

time.sleep(10)

WebDriverWait(driver, 10).until(EC.alert_is_present())

alert = driver.switch_to.alert
assert "Thanks for the message!!" in alert.text

print("Wiadomość wysłana!")

alert.accept()

driver.quit()




