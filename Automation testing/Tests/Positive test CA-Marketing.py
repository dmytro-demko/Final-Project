import random
import time
import datetime

from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

keys = Keys()
fake = Faker()
driver = webdriver.Chrome()
driver.get("https://qasvus.wixsite.com/ca-marketing")
time.sleep(3)
driver.maximize_window()

print("Current title is:", driver.title)
print("Current URL is:", driver.current_url)

# Проверяем соответствие главной страницы
# Входим в поле регистрации
driver.find_element(By.XPATH, '//*[@data-mesh-id="SITE_HEADERinlineContent"]')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@class="YT_9QV"]').click()
time.sleep(2)
driver.find_element(By.ID, "signUpHeadline_SM_ROOT_COMP736")
driver.find_element(By.ID, "switchToEmailLink_SM_ROOT_COMP736").click()

# Регистрация аккаунта
driver.find_element(By.ID, "input_input_emailInput_SM_ROOT_COMP736").send_keys(fake.email())
driver.find_element(By.ID, "input_input_passwordInput_SM_ROOT_COMP736").send_keys(fake.password())
time.sleep(2)
driver.find_element(By.ID, "okButton_SM_ROOT_COMP736").click()
time.sleep(2)
wait = WebDriverWait(driver, 2)
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="comp-k00e6z1w"]/div/button/div[2]')))
time.sleep(2)
element.click()

# Вход в аккаунт
wait = WebDriverWait(driver, 2)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="comp-k00e6z1w"]/div/nav[2]')))

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="comp-k00e6z1w"]/div/nav[2]/ul/li[3]/a/span').click()

# Подтверждаем нахождение на странице "My Addresses"
# НЕ СМОГ НАЙТИ ПОДХОДЯЩИХ ЛОКАТОРОВ
# ДАЖЕ ИСПОЛЬЗОВАЛ Selenium IDE
# ПОЭТОМУ ПРОДОЛЖАЮ Automation testing НА ДРУГОМ САЙТЕ

driver.quit()