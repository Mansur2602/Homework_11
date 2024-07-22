
from selenium import webdriver 
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=options)

driver.get('https://pomenyay.kz/?ref=vc.ru')

usd_element = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/div/table/tbody/tr[1]/td[3]/div')
print(f"Курс доллара: {usd_element.text}")

driver.quit()
