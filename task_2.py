import requests  
from selenium import webdriver  
from openpyxl import Workbook  
from selenium.webdriver.common.by import By  
import time

chrome = webdriver.Chrome()  
  
chrome.get("https://global.wildberries.ru/catalog?category=9492")  
time.sleep(10)

work_book = Workbook()  
work_sheet = work_book.active  
  
item_names = chrome.find_elements(By.CLASS_NAME, "product-card__name")  
price = chrome.find_elements(By.CLASS_NAME, "price__lower" )

number = 1
for item in item_names:
    work_sheet["A" + str(number)] = item.text
    number += 1

number = 1
for i in price:
    work_sheet["B" + str(number)] = i.text + "p"
    number += 1

work_sheet.column_dimensions['A'].width = 70

work_book.save("main.xlsx")

