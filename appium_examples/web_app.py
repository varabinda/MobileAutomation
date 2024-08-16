from typing import Any, Dict

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

import time


DEFAULT_PORT = 4723


def start_server():
    appium_server = AppiumService()
    appium_server.start(args=[
        '--address', '127.0.0.1',
        '--port', str(DEFAULT_PORT),
        '--base-path', '/',
        '--log-level', 'info'])
    assert appium_server.is_running, "Appium server did not start"
    assert appium_server.is_listening, "Appium server not listening"

    return appium_server


def stop_server(appium_server):
    appium_server.stop()
    assert not appium_server.is_running, "Appium server is still running"
    assert not appium_server.is_listening, "Appium server is still listening"


def init_driver():
    appium_server_url = 'http://127.0.0.1:4723'

    desired_caps: Dict[str, Any] = {
        'platformVersion': '14',
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'automationName': 'UIAutomator2',
        'setWebContentsDebuggingEnabled': 'True',
        'browserName': 'chrome',
        'chromedriverExecutable': '/Users/arabinda/Code/MobileAutomation/bundles/chromedriver_124.0.6367.91',
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)
    l_driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    return l_driver


server = start_server()
driver = init_driver()
driver.implicitly_wait(10)

driver.get('https://dpgraham.github.io/')

driver.find_element(AppiumBy.XPATH, "//button[@class='navbar-toggle']").click()
driver.find_element(AppiumBy.XPATH, "//a[contains(text(), 'Books & Resources')]").click()
book_elements = driver.find_elements(AppiumBy.XPATH, "//a[@class='resource-title']")
for book in book_elements:
    print(book.text)

time.sleep(10)

driver.quit()
stop_server(server)