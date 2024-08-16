from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options

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


server = start_server()

appium_server_url = 'http://localhost:4723'

options = UiAutomator2Options()

options.platform_version = '14'
options.automation_name = 'uiautomator2'
options.platform_name = 'android'
options.device_name = 'emulator-5554'

options.app_package = 'com.android.settings'
options.app_activity = '.Settings'

driver = webdriver.Remote(command_executor=appium_server_url, options=options)

caps = driver.capabilities.keys()
for cap in caps:
    print(cap, ": ", driver.capabilities.get(cap))


time.sleep(5)

driver.quit()

stop_server(server)
