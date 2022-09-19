from selenium import webdriver
from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent
from proxy_auth_data import login, password

# url = "https://www.instagram.com/"

user_agents_list = [
    "hello_world",
    "best_of_the_best",
    "21st century"
]

useragent = UserAgent()

# options
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=HelloWorld:)")

# options.add_argument(f"user-agent={random.choices(user_agents_list)}")
options.add_argument(f"user-agent={useragent.random}")

# set proxy
# options.add_argument("--proxy-server=138.128.91.65:8000")

proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@138.128.91.65:8000"
    }
}


# driver = webdriver.Chrome(
#     executable_path="C:\\Users\\Shakhzod\\PycharmProjects\\pythonIntro\\selenium_python"
#                     "\\chromedriver\\chromedriver.exe", options=options
# )
# driver = webdriver.Chrome(
#     executable_path="C:\\Users\\Shakhzod\\PycharmProjects\\pythonIntro\\selenium_python"
#                     "\\chromedriver\\chromedriver.exe", seleniumwire_options=proxy_options
# )
driver = webdriver.Chrome(
    executable_path="C:\\Users\\Shakhzod\\PycharmProjects\\pythonIntro\\selenium_python"
                    "\\chromedriver\\chromedriver.exe", seleniumwire_options=proxy_options
)
# C:\Users\Shakhzod\PycharmProjects\pythonIntro\selenium_python\chromedriver\chromedriver.exe
try:
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    # time.sleep(2)
    # driver.get(url="https://www.freepik.com/")
    # driver.save_screenshot("freepik.png")
    # time.sleep(5)

    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)
    # driver.refresh()
    # time.sleep(2)
    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # time.sleep(2)

    driver.get("https://whatismyipaddress.com/")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
