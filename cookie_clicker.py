import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b')
grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b')
factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b')
mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]/b')
shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b')
alchemy = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')
portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b')
time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')
money = driver.find_element(By.XPATH, '//*[@id="money"]').text

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes
while True:
    cookie.click()

    if time.time() > timeout:
        money = driver.find_element(By.XPATH, '//*[@id="money"]').text
        if "," in money:
            money = money.replace(",", "")
        try:
            if int(money) > int(time_machine.text.split("-")[1].strip().replace(",", "")):
                time_machine.click()
                time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')
            elif int(money) > int(portal.text.split("-")[1].strip().replace(",", "")):
                portal.click()
                portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]')
            elif int(money) > int(alchemy.text.split("-")[1].strip().replace(",", "")):
                alchemy.click()
                alchemy = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
            elif int(money) > int(shipment.text.split("-")[1].strip().replace(",", "")):
                shipment.click()
                shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]')
            elif int(money) > int(mine.text.split("-")[1].strip().replace(",", "")):
                mine.click()
                mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
            elif int(money) > int(factory.text.split("-")[1].strip().replace(",", "")):
                factory.click()
                factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
            elif int(money) > int(grandma.text.split("-")[1].strip().replace(",", "")):
                grandma.click()
                grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
            elif int(money) > int(cursor.text.split("-")[1].strip().replace(",", "")):
                cursor.click()
                cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')
        except selenium.common.exceptions.StaleElementReferenceException:
            if int(money) > int(time_machine.text.split("-")[1].strip().replace(",", "")):
                time_machine.click()
                time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')
            elif int(money) > int(portal.text.split("-")[1].strip().replace(",", "")):
                portal.click()
                portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]')
            elif int(money) > int(alchemy.text.split("-")[1].strip().replace(",", "")):
                alchemy.click()
                alchemy = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
            elif int(money) > int(shipment.text.split("-")[1].strip().replace(",", "")):
                shipment.click()
                shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]')
            elif int(money) > int(mine.text.split("-")[1].strip().replace(",", "")):
                mine.click()
                mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
            elif int(money) > int(factory.text.split("-")[1].strip().replace(",", "")):
                factory.click()
                factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
            elif int(money) > int(grandma.text.split("-")[1].strip().replace(",", "")):
                grandma.click()
                grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
            elif int(money) > int(cursor.text.split("-")[1].strip().replace(",", "")):
                cursor.click()
                cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')
        except selenium.common.exceptions.NoSuchElementException:
            cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b')
            grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b')
            factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b')
            mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]/b')
            shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b')
            alchemy = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')
            portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b')
            time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')
            if int(money) > int(time_machine.text.split("-")[1].strip().replace(",", "")):
                time_machine.click()
                time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')
            elif int(money) > int(portal.text.split("-")[1].strip().replace(",", "")):
                portal.click()
                portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]')
            elif int(money) > int(alchemy.text.split("-")[1].strip().replace(",", "")):
                alchemy.click()
                alchemy = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
            elif int(money) > int(shipment.text.split("-")[1].strip().replace(",", "")):
                shipment.click()
                shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]')
            elif int(money) > int(mine.text.split("-")[1].strip().replace(",", "")):
                mine.click()
                mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
            elif int(money) > int(factory.text.split("-")[1].strip().replace(",", "")):
                factory.click()
                factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
            elif int(money) > int(grandma.text.split("-")[1].strip().replace(",", "")):
                grandma.click()
                grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
            elif int(money) > int(cursor.text.split("-")[1].strip().replace(",", "")):
                cursor.click()
                cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')

        timeout = time.time() + random.randint(0, 15)

    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break



