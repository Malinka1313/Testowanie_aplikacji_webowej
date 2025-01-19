from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.demoblaze.com')

time.sleep(5)

samsung = driver.find_element(By.CLASS_NAME, "hrefch")
samsung.click()

time.sleep(5)

dodaj_do_koszyka = driver.find_element(By.XPATH, "//a[contains(text(), 'Add to cart')]")
dodaj_do_koszyka.click()

time.sleep(5)

WebDriverWait(driver, 10).until(EC.alert_is_present())

alert = driver.switch_to.alert
alert.accept()

time.sleep(10)

cart = driver.find_element(By.XPATH, '//a[@href="cart.html"]')
cart.click()


time.sleep(10)

try:

    delete_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Delete"))
    )
    assert delete_button.is_displayed(), "Produkt został dodany do koszyka."
    print("Produkt został dodany do koszyka.")
except AssertionError:
    print("Błąd!")


driver.quit()




