# from selenium import webdriver
from seleniumwire import webdriver
import time
from fake_useragent import UserAgent
from proxy_auth_data import login, password

# url = "https://www.instagram.com/"

useragent = UserAgent()
# options
options = webdriver.FirefoxOptions()

# set proxy
# proxy = "138.128.91.65:8000"
# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilities["marionette"] = True
#
# firefox_capabilities["proxy"] = {
#     "proxyType": "MANUAL",
#     "httpProxy": proxy,
#     "ftpProxy": proxy,
#     "sslProxy": proxy
# }

proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@138.128.91.65:8000"
    }
}

# change useragent
# options.set_preference("general.useragent.override", "Hello Friend")
options.set_preference("general.useragent.override", useragent.random)

# driver = webdriver.Firefox(executable_path=r"C:\Users\Shakhzod\PycharmProjects\pythonIntro\selenium_python"
#                                            r"\firefoxdriver\geckodriver.exe", options=options, proxy=proxy)

driver = webdriver.Firefox(executable_path=r"C:\Users\Shakhzod\PycharmProjects\pythonIntro\selenium_python"
                                           r"\firefoxdriver\geckodriver.exe", seleniumwire_options=proxy_options)

# C:\Users\Shakhzod\PycharmProjects\pythonIntro\selenium_python\firefoxdriver\geckodriver.exe -> \\ without r"C:...
try:
    driver.get("http://www.whatismyproxy.com/")
    time.sleep(4)

    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    # driver.get(url="https://www.freepik.com/")
    # driver.save_screenshot("freepik.png")
    # time.sleep(2)
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)
    # driver.refresh()
    # time.sleep(2)
    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()