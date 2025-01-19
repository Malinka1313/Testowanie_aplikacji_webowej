from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.demoblaze.com')

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "hrefch")))

samsung = driver.find_element(By.CLASS_NAME, "hrefch")
samsung.click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add to cart')]")))

dodaj_do_koszyka = driver.find_element(By.XPATH, "//a[contains(text(), 'Add to cart')]")
dodaj_do_koszyka.click()

WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cartur")))

koszyk = driver.find_element(By.ID, "cartur")
koszyk.click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "page-wrapper")))

place_order = driver.find_element(By.ID, "page-wrapper")
place_order2 = place_order.find_element(By.CLASS_NAME, "btn.btn-success")
place_order2.click()

time.sleep(10)

imie = driver.find_element(By.ID, "name")
imie.send_keys("Anna Nowak")

kraj = driver.find_element(By.ID, "country")
kraj.send_keys("Poland")

miasto = driver.find_element(By.ID, "city")
miasto.send_keys("Wroclaw")

karta = driver.find_element(By.ID, "card")
karta.send_keys("123456123456")

miesiac = driver.find_element(By.ID, "month")
miesiac.send_keys("10")

rok = driver.find_element(By.ID, "year")
rok.send_keys("1995")

kup = driver.find_element(By.ID, "orderModal")
kup2 = kup.find_element(By.CLASS_NAME, "btn.btn-primary")
kup2.click()

time.sleep(10)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sweet-alert")))


try:

    okno = driver.find_element(By.CLASS_NAME, "sweet-alert")

    okno_text = okno.text

    expected_text = "Thank you for your purchase!"

    assert expected_text in okno_text, f"Modal nie zawiera oczekiwanego tekstu. Znaleziono: {okno_text}"

    print("Zakup się powiódł")

except Exception as e:
    print("Błąd: Nie udało się zakupić produktu", e)


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm.btn.btn-lg.btn-primary")))

ok_button = driver.find_element(By.CSS_SELECTOR, ".confirm.btn.btn-lg.btn-primary")
ok_button.click()

driver.quit()
