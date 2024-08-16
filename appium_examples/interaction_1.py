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
    appium_server_url = 'http://localhost:4723'

    options = UiAutomator2Options()
    options.platform_version = '14'
    options.automation_name = 'uiautomator2'
    options.platform_name = 'android'
    options.device_name = 'emulator-5554'
    options.app_package = 'io.appium.android.apis'
    # options.app_activity = '.ApiDemos'
    options.app = './bundles/ApiDemos.apk'
    options.full_reset = True


    driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    return driver


server = start_server()
driver = init_driver()

title_xpath = '//android.widget.TextView[@text="API Demos"]'
title_element = driver.find_element(by=AppiumBy.XPATH, value=title_xpath)
assert title_element.text == 'API Demos'

preference_id = 'Preference'
preference_elem = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=preference_id)
assert preference_elem.text == 'Preference'
preference_elem.click()

title_2_uiautomator = 'new UiSelector().text("API Demos")'
title_2_elem = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=title_2_uiautomator)
assert title_2_elem.text == 'API Demos'

dependency_xpath = '//android.widget.ListView[@resource-id="android:id/list"]/android.widget.TextView[@text="3. Preference dependencies"]'
dependency_elem = driver.find_element(by=AppiumBy.XPATH, value=dependency_xpath)
assert dependency_elem.text == '3. Preference dependencies'
dependency_elem.click()

title_3_xpath = '//android.widget.TextView[@text="Preference/3. Preference dependencies"]'
title_3_elem = driver.find_element(by=AppiumBy.XPATH, value=title_3_xpath)
assert title_3_elem.text == 'Preference/3. Preference dependencies'

checkbox_classname = 'android.widget.CheckBox'
checkbox_elem = driver.find_element(by=AppiumBy.CLASS_NAME, value=checkbox_classname)
checkbox_elem.click()

wifi_settings_uiautomator = 'new UiSelector().className("android.widget.RelativeLayout").instance(1)'
wifi_settings_elem = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=wifi_settings_uiautomator)
wifi_settings_elem.click()

wifi_settings_title_id = 'android:id/alertTitle'
wifi_settings_title_elem = driver.find_element(by=AppiumBy.ID, value=wifi_settings_title_id)
assert wifi_settings_title_elem.text == 'WiFi settings'

alert_textbox_id = 'android:id/edit'
alert_textbox_elem = driver.find_element(by=AppiumBy.ID, value=alert_textbox_id)
alert_textbox_elem.send_keys('wifi-test')

ok_button_id = 'android:id/button1'
ok_button_elem = driver.find_element(by=AppiumBy.ID, value=ok_button_id)
ok_button_elem.click()

driver.back()
driver.back()

driver.quit()
stop_server(server)
