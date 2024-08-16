import time
from typing import Any, Dict

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


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
        # 'platformVersion': 14,
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'automationName': 'UIAutomator2',

        'appPackage': 'io.appium.android.apis',
        'appActivity': '.ApiDemos',

        'app': './bundles/ApiDemos.apk',
        'fullReset': False,
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)

    l_driver = webdriver.Remote(command_executor=appium_server_url, options=options)

    return l_driver


server = start_server()
driver = init_driver()

views_accessibility_id = 'Views'
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=views_accessibility_id).click()

list_accessibility_id = 'Expandable Lists'
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=list_accessibility_id).click()

adapter_accessibility_id = '1. Custom Adapter'
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=adapter_accessibility_id).click()

people_xpath = '//android.widget.TextView[@text="People Names"]'
driver.find_element(AppiumBy.XPATH, people_xpath).click()

david_xpath = '//android.widget.TextView[@text="David"]'
david_elem = driver.find_element(AppiumBy.XPATH, david_xpath)
print(david_elem.location, david_elem.size)

x_coordinate = david_elem.location['x'] + david_elem.size['width'] // 2
y_coordinate = david_elem.location['y'] + david_elem.size['height'] // 2
print(x_coordinate, y_coordinate)
driver.execute_script('mobile: longClickGesture',
                      {'x': x_coordinate, 'y': y_coordinate,
                       'duration': 1500})

menu_rid = 'android:id/title'
assert driver.find_element(AppiumBy.ID, menu_rid).text == 'Sample menu'

time.sleep(3)

driver.quit()
stop_server(server)

