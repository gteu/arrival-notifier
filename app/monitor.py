from selenium import webdriver
import os

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()

# Selenium Server に接続する
driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    options=options,
)

# Selenium 経由でブラウザを操作する
driver.get('https://qiita.com')
print(driver.current_url)

# ブラウザを終了する
driver.quit()