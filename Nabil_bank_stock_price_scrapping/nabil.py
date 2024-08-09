from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = 'https://www.sharesansar.com/company/nabil'

driver = webdriver.Chrome()
driver.get(url)

price_history = driver.find_element(By.ID, 'btn_cpricehistory')
price_history.click()

SN = []
Date = []
Open = []
High = []
Low = []
Ltp = []
Change = []
Qty = []
Turnover = []

page = 1

while True:
    print(f"Scraping page {page}...")
    
    tbody = driver.find_elements(By.TAG_NAME, 'tbody')
    for table_rows in tbody:
        table_data = table_rows.find_elements(By.XPATH, './tr[@role="row"]')
        for data in table_data:
            SN.append(data.find_element(By.XPATH, './td[1]').text)
            Date.append(data.find_element(By.XPATH, './td[2]').text)
            Open.append(data.find_element(By.XPATH, './td[3]').text)
            # High.append(data.find_element(By.XPATH, './td[4]').text)
            h = (data.find_element(By.XPATH, './td[4]').text)
            High.append(h)
            Low.append(data.find_element(By.XPATH, './td[5]').text)
            Ltp.append(data.find_element(By.XPATH, './td[6]').text)
            Change.append(data.find_element(By.XPATH, './td[7]').text)
            Qty.append(data.find_element(By.XPATH, './td[8]').text)
            Turnover.append(data.find_element(By.XPATH, './td[9]').text)
            
    next_button = driver.find_element(By.ID, 'myTableCPriceHistory_next')
    next_button_class = next_button.get_attribute('class')
        
    if 'disabled' in next_button_class:
        print("Reached the last page.")
        break
    next_button.click()
    
    page += 1
    time.sleep(1)
        
df = pd.DataFrame({
    "S.N.": SN,
    "Date": Date,
    "Open": Open,
    "High": High,
    "Low": Low,
    "Ltp": Ltp,
    "% Change": Change,
    "Qty": Qty,
    "Turnover": Turnover
})

df.to_csv('nabil.csv', index=False)
        
time.sleep(4)
# driver.close()