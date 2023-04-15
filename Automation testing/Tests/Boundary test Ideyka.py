import random
import time
import datetime


from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


keys = Keys()
fake = Faker()
driver = webdriver.Chrome()
driver.get("https://ideyka.com.ua/")
driver.maximize_window()
wait = WebDriverWait(driver, 2)

print("Current title is:", driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, "//a[@data-url='https://ideyka.com.ua/en']").click()

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

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@name="user_save"]').click()

# Входим в меню
driver.find_element(By.XPATH, '//span[@class="burger"]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="menu-categories"]/ul/li[6]/a/span').click()

# Проверяем title

try:
    assert driver.title == "Action goods"
except AssertionError:
    print('Title is different. Current title is :', driver.title)


driver.find_element(By.LINK_TEXT, "Diamond mosaic - A kiss under the moon")
driver.find_element(By.XPATH, '//*[@id="fn_products_content"]/div[3]/div/div/div[1]/div[1]/a/img').click()

# Заказ товара
driver.find_element(By.XPATH,'//input[@name="amount"]').clear()

# Заказываем "0"
product_add_cart_element = driver.find_element(By.ID, "product_add_cart")
driver.execute_script("arguments[0].click();", product_add_cart_element)
wait = WebDriverWait(driver, 10)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fn_pop_up_cart_wrap"]/button')))
close_button.click()

# Заказываем "1"
driver.find_element(By.XPATH,'//input[@name="amount"]').send_keys(1)
submit_button_xpath = '//button[@type="submit"]'
submit_button = driver.find_element(By.XPATH, submit_button_xpath)
driver.execute_script("arguments[0].scrollIntoView();", submit_button)
driver.execute_script("arguments[0].click();", submit_button)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fn_callback_sent"]/button')))
close_button.click()

# Заказываем "99999"

driver.find_element(By.XPATH,'//input[@name="amount"]').clear()
driver.find_element(By.XPATH,'//input[@name="amount"]').send_keys(99999)

submit_button_xpath = '//button[@type="submit"]'
submit_button = driver.find_element(By.XPATH, submit_button_xpath)
driver.execute_script("arguments[0].scrollIntoView();", submit_button)
driver.find_element(By.ID, "product_add_cart").click()
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fn_pop_up_cart_wrap"]/button')))
close_button.click()

# проверяем корзину

driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="cart_informer"]/a/div[1]/span[1]').click()


# Закрыть браузер и завершить работу веб-драйвера

driver.quit()
#driver.close()
