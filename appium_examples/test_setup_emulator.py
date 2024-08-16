from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# appium_server_url = 'http://localhost:4723'
appium_server_url = 'http://127.0.0.1:4723'

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
