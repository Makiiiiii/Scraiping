from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

import time


def main(url):
    path = "/Applications/chromedriver"
    driver = webdriver.Chrome(executable_path=path)
    driver.get(url)

    searchForm = driver.find_element(By.XPATH, "//textarea[@title='検索']")
    searchForm.send_keys("麻婆豆腐")
    searchButton = driver.find_element(By.XPATH, "//input[@value='Google 検索']")
    searchButton.click()

    time.sleep(3)

    ## ここに処理を記述してね！

    driver.quit()

if __name__ == '__main__':
    url = 'https://google.com'
    main(url)
