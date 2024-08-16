from typing import Any, Dict

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

import  time


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
        'fullReset': False,
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)

    l_driver = webdriver.Remote(command_executor=appium_server_url, options=options)

    return l_driver


server = start_server()
driver = init_driver()

views_accessibility_id = 'Views'
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=views_accessibility_id).click()

print(driver.get_window_rect())

# Method - 1
# Reference: https://github.com/appium/appium-uiautomator2-driver/blob/master/docs/android-mobile-gestures.md
# can_scroll_down = driver.execute_script('mobile: scrollGesture', {
#     'left': 100, 'top': 100, 'width': 200, 'height': 300,
#     'direction': 'down',
#     'percent': 3.0
# })

# Method - 2
# Scroll down
wv3_script = 'new UiScrollable(new UiSelector()).scrollIntoView(text("WebView3"))'
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=wv3_script)
#
# time.sleep(2)
#
# #Scroll up
ani_script = 'new UiScrollable(new UiSelector()).scrollIntoView(text("Animation"))'
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=ani_script)

driver.quit()
stop_server(server)