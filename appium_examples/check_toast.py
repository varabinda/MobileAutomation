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
        'platformVersion': '14',
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'automationName': 'UIAutomator2',
        'autoGrantPermissions': True,

        'app': '../bundles/General-Store.apk',
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)

    l_driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    l_driver.implicitly_wait(10)

    return l_driver


server = start_server()
driver = init_driver()

driver.find_element(by=AppiumBy.ID, value="android:id/text1").click()
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Argentina\")").click()
driver.find_element(by=AppiumBy.ID, value="com.androidsample.generalstore:id/radioFemale").click()
driver.find_element(by=AppiumBy.ID, value="com.androidsample.generalstore:id/btnLetsShop").click()
toast_element = driver.find_element(AppiumBy.XPATH, '//android.widget.Toast')
assert toast_element.text == 'Please enter your name'

driver.quit()
stop_server(server)

