from selenium import webdriver
import time

url = "https://www.instagram.com/"
driver = webdriver.Firefox(executable_path="C:\\Users\\Shakhzod\\PycharmProjects\\pythonIntro\\selenium_python"
                                           "\\firefoxdriver\\geckodriver.exe")
# C:\Users\Shakhzod\PycharmProjects\pythonIntro\selenium_python\firefoxdriver\geckodriver.exe
try:
    driver.get(url="https://www.freepik.com/")
    driver.save_screenshot("freepik.png")
    time.sleep(5)
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