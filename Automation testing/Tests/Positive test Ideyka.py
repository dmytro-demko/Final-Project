import random
import time
import datetime


from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


keys = Keys()
fake = Faker()
driver = webdriver.Chrome()
driver.get("https://ideyka.com.ua/")
driver.maximize_window()

print("Current title is:", driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, "//a[@data-url='https://ideyka.com.ua/en']").click()
# driver.find_element(By.XPATH, "//a[@class='form__button button--blick']").click()
time.sleep(1)
try:
    assert driver.title == "Ideyka online store: paintings by numbers, goods for creativity and hobbies in Ukraine"
except AssertionError:
    print('Title is different. Current title is :', driver.title)

driver.find_element(By.XPATH, '//*[@height="20px"]').click()
time.sleep(1)
try:
    assert driver.title == "Login to your personal account"
except AssertionError:
    print('Title is different. Current title is :', driver.title)

driver.find_element(By.XPATH, "//body/div[@id='fn_content']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/a[1]").click()
time.sleep(1)
try:
    assert driver.title == "Registration"
except AssertionError:
    print('Title is different. Current title is :', driver.title)

driver.find_element(By.XPATH,"//body/div[@id='fn_content']/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]").send_keys(fake.name())

driver.find_element(By.NAME, "last_name").send_keys(fake.last_name())

driver.find_element(By.NAME, "email").send_keys(fake.email())


def generate_phone_number():
    first_three_digits = random.choice(['050', '067'])
    last_seven_digits = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    return f'{first_three_digits}{last_seven_digits}'

phone_number = generate_phone_number()

driver.find_element(By.XPATH, '//body[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[4]/input[1]').send_keys(phone_number)

driver.find_element(By.NAME, "address").send_keys(fake.address())

driver.find_element(By.XPATH,'//*[@name="password"]').send_keys(fake.password())


month = random.randint(1, 12)
day = random.randint(1, 28)
year = random.randint(1950, 2005)
birthday = datetime.date(year, month, day).strftime("%m%d%Y")

driver.find_element(By.XPATH,"//body/div[@id='fn_content']/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[10]/input[1]").send_keys(birthday)

driver.find_element(By.NAME, "sex").send_keys(random.choice("male, female"))

driver.find_element(By.XPATH,'//*[@value="Sign Up"]').click()
# Сохраняем данные
# Scroll down the page by one page
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
time.sleep(3)
driver.find_element(By.XPATH,'//*[@name="user_save"]').click()


driver.quit()
# driver.close()
