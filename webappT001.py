from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.demoblaze.com')

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "hrefch")))

page_title = driver.title
print(f"Tytuł strony: {page_title}")

expected_title = "DEMO BLAZE"

if page_title == expected_title:
    print("Tytuł strony jest poprawny!")
else:
    print(f"Błąd: Oczekiwano tytułu '{expected_title}', ale znaleziono '{page_title}'")

driver.quit()