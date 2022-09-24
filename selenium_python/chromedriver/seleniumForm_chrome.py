from selenium import webdriver
from selenium.webdriver import Keys
import time

# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/105.0.0.0 Safari/537.36")

driver = webdriver.Chrome(
    executable_path="C:\\Users\\Shakhzod\\PycharmProjects\\pythonIntro\\selenium_python"
                    "\\chromedriver\\chromedriver.exe", options=options
)
try:
    driver.get("https://www.instagram.com/")
    time.sleep(2)

    email_input = driver.find_element("name", "username")
    email_input.clear()
    email_input.send_keys("minutejustfor1")
    time.sleep(4)

    password_input = driver.find_element("name", "password")
    password_input.send_keys("qwerty12345")
    time.sleep(4)

    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
