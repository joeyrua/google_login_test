import undetected_chromedriver as uc
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
import time
URL = uc.Chrome()
wait = ui.WebDriverWait(URL, 10)
URL.get("http://www.google.com")  # 進入google首頁
URL.maximize_window()

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div/div/div/div[2]/a"))
login_btn = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div/div/div/div[2]/a").click()  # 登入按鈕

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))
email = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
email.send_keys("yellow145258789")  # 輸入帳號
email.send_keys(Keys.ENTER)  # 按下Enter

time.sleep(2)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))
password = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
password.send_keys("juan145258789145258789")  # 輸入密碼
password.send_keys(Keys.ENTER)  # 按下Enter

time.sleep(2)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/ul/li[2]"))
one = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/ul/li[2]").click()  # 選擇第一個驗證方式
