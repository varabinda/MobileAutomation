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
        # 'platformVersion': 14,
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'automationName': 'UIAutomator2',

        'appPackage': 'io.appium.android.apis',
        'appActivity': '.ApiDemos',

        'app': '../bundles/ApiDemos.apk',
        'fullReset': True,
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)
    l_driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    return l_driver


server = start_server()
driver = init_driver()

time.sleep(2)

package = driver.current_package
activity = driver.current_activity

print("Package name: " + package + ", activity: " + activity)

if driver.query_app_state(package) == ApplicationState.RUNNING_IN_FOREGROUND:
    print(package, "is running in foreground")

driver.background_app(-2)

if driver.query_app_state(package) == ApplicationState.RUNNING_IN_BACKGROUND:
    print(package, "is running in background")

time.sleep(2)

driver.activate_app(package)
if driver.query_app_state(package) == ApplicationState.RUNNING_IN_FOREGROUND:
    print(package, "is brought to foreground")

time.sleep(2)

if driver.terminate_app(package):
    print(package, "is terminated")

if driver.query_app_state(package) == ApplicationState.NOT_RUNNING:
    print(package, "is not running")

time.sleep(2)

driver.quit()
stop_server(server)