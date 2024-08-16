from typing import Any, Dict

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from appium.webdriver.applicationstate import ApplicationState

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
        'appPackage': 'io.appium.android.apis',
        'appActivity': '.ApiDemos',

        'app': './bundles/ApiDemos.apk',
        'fullReset': True,
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)
    l_driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    return l_driver


server = start_server()
driver = init_driver()

store_package = 'com.androidsample.generalstore'
store_activity = '.MainActivity'

print("Current app: " + driver.current_package + driver.current_activity)

new_driver = driver.install_app("./bundles/General-Store.apk")
new_driver.activate_app(store_package)
new_driver.wait_activity(store_package + store_activity, 5, 1)

time.sleep(2)

new_driver.terminate_app(store_activity)

new_driver.remove_app(store_package)

if new_driver.query_app_state(store_package) == ApplicationState.NOT_INSTALLED:
    print(store_package + ' is not installed')

new_driver.quit()

stop_server(server)