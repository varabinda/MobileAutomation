import time
from typing import Any, Dict

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey


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
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)

    l_driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    l_driver.implicitly_wait(10)

    return l_driver


server = start_server()
driver = init_driver()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Preference').click()

dependency_xpath = '//android.widget.ListView[@resource-id="android:id/list"]/android.widget.TextView[@text="3. Preference dependencies"]'
driver.find_element(by=AppiumBy.XPATH, value=dependency_xpath).click()

driver.orientation = "LANDSCAPE"

checkbox_classname = 'android.widget.CheckBox'
driver.find_element(by=AppiumBy.CLASS_NAME, value=checkbox_classname).click()

wifi_settings_uiautomator = 'new UiSelector().className("android.widget.RelativeLayout").instance(1)'
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=wifi_settings_uiautomator).click()

alert_textbox_id = 'android:id/edit'
alert_textbox_elem = driver.find_element(by=AppiumBy.ID, value=alert_textbox_id)

if driver.is_keyboard_shown():
    driver.hide_keyboard()

alert_textbox_elem.send_keys('wifi-test')
driver.press_keycode(AndroidKey.DEL)
driver.press_keycode(AndroidKey.DEL)
driver.press_keycode(AndroidKey.DEL)
driver.press_keycode(AndroidKey.DEL)
alert_textbox_elem.send_keys('arve')

time.sleep(1)

ok_button_id = 'android:id/button1'
ok_button_elem = driver.find_element(by=AppiumBy.ID, value=ok_button_id)
ok_button_elem.click()

driver.orientation = "PORTRAIT"

time.sleep(1)

driver.quit()
stop_server(server)