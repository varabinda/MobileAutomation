from typing import Any, Dict

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey

import time


DEFAULT_PORT = 4723


def start_server():
    appium_server = AppiumService()
    appium_server.start(args=[
        '--address', '127.0.0.1',
        '--port', str(DEFAULT_PORT),], timeout=20000)
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
        # 'appPackage': 'com.androidsample.generalstore',
        # 'appActivity': '.MainActivity',
        'app': './bundles/General-Store.apk',
        # 'fullReset': False,
        # 'browser': 'Chrome',
        'chromedriverExecutable': '/Users/arabinda/Code/MobileAutomation/bundles/chromedriver_123.0.6312.122'
                                  '',
        # 'chromeOptions': {'androidPackage': 'com.android.chrome'}
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)
    l_driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    return l_driver


server = start_server()
driver = init_driver()
driver.implicitly_wait(10)

print("Current app: " + driver.current_package + driver.current_activity)
print("Context:", driver.contexts)

driver.find_element(by=AppiumBy.ID, value="android:id/text1").click()
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Andorra\")").click()
driver.find_element(by=AppiumBy.ID, value="com.androidsample.generalstore:id/nameField").send_keys("Arve")
driver.find_element(by=AppiumBy.ID, value="com.androidsample.generalstore:id/radioMale").click()
driver.find_element(by=AppiumBy.ID, value="com.androidsample.generalstore:id/btnLetsShop").click()
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"com.androidsample.generalstore:id/productAddCart\").instance(0)").click()
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"ADD TO CART\")").click()
driver.find_element(by=AppiumBy.ID, value="com.androidsample.generalstore:id/appbar_btn_cart").click()
driver.find_element(by=AppiumBy.ID, value="com.androidsample.generalstore:id/btnProceed").click()

driver.find_element(by=AppiumBy.ID, value='com.androidsample.generalstore:id/webView')
print('Contexts:', driver.contexts)

driver.switch_to.context('WEBVIEW_com.androidsample.generalstore')
search_text = 'appium python client'
search_element = driver.find_element(AppiumBy.XPATH, "//textarea[@name='q']")
search_element.send_keys(search_text)

driver.press_keycode(AndroidKey.ENTER)

time.sleep(15)

driver.quit()

stop_server(server)