from time import sleep
from selenium. webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary # pip install chromedriver-binary==108.0.5359.71
import pandas as pd
import config

# INPORT NEW DATA #
df          = pd.read_csv("スマレジ商品価格改定シート.csv", encoding='shift_jis')
df          = df.replace(',', '', regex=True)
df          = df[~pd.to_numeric(df["新価格"], errors="coerce").isnull()]
jan_list    = df["JAN"].to_list()
price_list  = df["新価格"].to_list()
date_list  = df["更新日"].to_list()

print(date_list)

# print(jan_list)

# START SELENIUM #
df_noChange = pd.DataFrame()

#driver = webdriver.Remote('http://selenium:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME) # docker UNAVAI
driver = webdriver.Chrome()

fin_index = 0

# while True:

try:
    driver.get("https://accounts.smaregi.jp/login?client_id=pos")

    element = driver.find_element(By.NAME, "identifier")
    element.send_keys(config.user)

    element = driver.find_element(By.NAME, "password")
    element.send_keys(config.pw)

    element = driver.find_element(By.ID, "doLogin")
    element.click()

    
    for i in range(fin_index, len(jan_list)):

        jan = jan_list[i]
        price = price_list[i]
        date = date_list[i]

        driver.get("https://www1.smaregi.jp/control/master/product/")

        print(jan)

        element = driver.find_element(By.ID, "searchQuery")
        element.clear()
        element.send_keys(str(int(jan)))

        element = driver.find_element(By.NAME, "doSearch")
        element.click()

        try:
            # pick a top listed item 
            element = driver.find_element(By.XPATH, '//*[@id="Product"]/div[1]/div[3]/div[3]/div/div[8]/div[1]/table/tbody/tr/td[2]/div/span[2]/a')
            element.click()

            # Inside of the item page

            element = driver.find_element(By.XPATH,'//*[@id="PDMaster"]/div/div[1]/div[9]/div[2]/div/span/a[1]')
            element.click()
            
            sleep(1) # NEED TO WAIT...
            element = driver.find_element(By.ID, "id_product_price_modal_record_add")
            element.click()

            element = driver.find_element(By.NAME, "productPriceInfo[price][]")
            element.send_keys(str(int(price)))

            element = driver.find_element(By.NAME, "productPriceInfo[startDate][]")
            element.send_keys(str(date))

            element = driver.find_element(By.ID, "id_product_price_modal_create")
            element.click()

            print(f"Success {i+1}/{len(jan_list)}. JANコード {jan} -> {price}円 {date}")
            fin_index = i

        except:
            sleep(1)
            print(f"Faild {i+1}/{len(jan_list)}. JANコード {jan} -> {price}円 {date}")
            df_noChange["JAN"] = jan
            df_noChange["NewPrice"] = price

            fin_index = i

            continue

    print(f"{fin_index}/{len(jan_list)-1}")

    if fin_index == len(jan_list)-1:
        print(f"全ての価格変更が終了しました")
        # break
    
except Exception as e:
    print(e)
#     sleep(5)
#     continue


driver.quit()
