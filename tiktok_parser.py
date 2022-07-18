import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def tikitoki(link, directory):
    global driver
    try:
        path = os.getcwd()
        options = webdriver.ChromeOptions()
        preferences = {"download.default_directory": rf"{path}\{directory}", "safebrowsing.enabled": "false"}
        options.add_experimental_option("prefs", preferences)

        driver = webdriver.Chrome(options=options)
        driver.get("https://uk.savefrom.net/")
        inp_line = driver.find_element_by_name("sf_url")
        inp_line.send_keys(link)
        inp_line.send_keys(Keys.ENTER)
        time.sleep(1)
        time.sleep(2)
        btn = driver.find_element_by_class_name("link")
        btn.click()
    except Exception as e:
        driver.quit()
        print(e)
        tikitoki(link, directory)
    finally:
        time.sleep(3.5)
        driver.quit()
