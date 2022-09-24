from selenium import webdriver
from selenium.webdriver import Keys
import time
from auth_data import inst_password, inst_login
import pickle

# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/105.0.0.0 Safari/537.36")

driver = webdriver.Chrome(
    executable_path="C:\\Users\\Shakhzod\\PycharmProjects\\pythonIntro\\selenium_python"
                    "\\chromedriver\\chromedriver.exe", options=options
)
try:
    # driver.get("https://www.instagram.com/")
    # time.sleep(2)
    #
    # email_input = driver.find_element("name", "username")
    # email_input.clear()
    # email_input.send_keys(inst_login)
    # time.sleep(4)
    #
    # password_input = driver.find_element("name", "password")
    # password_input.clear()
    # password_input.send_keys(inst_password)
    # time.sleep(4)
    #
    # password_input.send_keys(Keys.ENTER)
    # time.sleep(10)

    # cookies
    # pickle.dump(driver.get_cookies(), open(f"{inst_login}_cookies", "wb"))
    driver.get("https://www.instagram.com/")
    time.sleep(5)

    for cookie in pickle.load(open(f"{inst_login}_cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(6)
    driver.refresh()
    time.sleep(11)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
