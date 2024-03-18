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

    first_result_link = driver.find_elements(By.XPATH, '//a/h3')[0]
    first_result_link.click()

    time.sleep(3)

    img = driver.find_element(By.CSS_SELECTOR, '.large_photo_clickable')

    src = img.get_attribute('src')
    if src:
        with open(f'mabotofu.png', 'wb') as f:
            f.write(img.screenshot_as_png)

    driver.quit()


if __name__ == '__main__':
    url = 'https://google.com'
    main(url)
