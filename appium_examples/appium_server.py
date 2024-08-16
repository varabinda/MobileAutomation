from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options

import time


def start_server():
    appium_server = AppiumService()

    args = [
        '--address', '127.0.0.1',
        '--port', '4723',
        '--base-path', '/',
    ]

    appium_server.start(args=args)

    print("Is Appium server running? ", appium_server.is_running)
    print("Is Appium server listening? ", appium_server.is_listening)

    return appium_server


def stop_server(appium_server):
    appium_server.stop()
    print("Is Appium server running? ", appium_server.is_running)
    print("Is Appium server listening? ", appium_server.is_listening)


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

time.sleep(5)

driver.quit()

stop_server(server)
