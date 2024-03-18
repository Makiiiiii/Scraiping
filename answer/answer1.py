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

    search_results = driver.find_elements(By.XPATH, '//a/h3')

    results = []
    for elem_h3 in search_results:
        title = elem_h3.text
        results.append([title])

    # CSVファイルに結果を書き込む
    with open('search_results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Title"])  # ヘッダーを書き込み
        writer.writerows(results)  # 検索結果を書き込み

    driver.quit()


if __name__ == '__main__':
    url = 'https://google.com'
    main(url)
