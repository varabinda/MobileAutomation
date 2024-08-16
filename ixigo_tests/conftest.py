import pytest

from typing import Any, Dict

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options

from configuration import APPIUM_ADDRESS, APPIUM_PORT, APP_PACKAGE, SPLASH_ACTIVITY


@pytest.fixture(scope='session')
def setup_server():
    server_status, server = start_server()
    assert server_status, "Appium server did not start successfully"
    yield
    assert stop_server(server), "Appium server did not stop successfully"


@pytest.fixture(scope='session')
def setup_driver():
    driver = init_driver()
    assert driver is not None, "Driver not initialized"
    yield driver
    deinit_driver(driver)


def start_server():
    appium_server = AppiumService()
    appium_server.start(args=[
        '--address', APPIUM_ADDRESS,
        '--port', APPIUM_PORT,
        '--base-path', '/',
        '--log-level', 'info'])
    if appium_server.is_running and appium_server.is_listening:
        return True, appium_server
    else:
        return False, None


def stop_server(server : AppiumService):
    server.stop()
    return not server.is_running and not server.is_listening


def init_driver():
    appium_server_url = 'http://' + APPIUM_ADDRESS + ':' + APPIUM_PORT

    desired_caps: Dict[str, Any] = {
        'platformVersion': '13',
        'platformName': 'Android',
        'deviceName': 'RZCTA103RGD',
        # 'deviceName': 'emulator-5554',
        'automationName': 'UIAutomator2',
        'appPackage': APP_PACKAGE,
        'appium:noReset': False,
        'appActivity': SPLASH_ACTIVITY,
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)
    l_driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    l_driver.implicitly_wait(10)
    return l_driver


def deinit_driver(driver):
    driver.quit()

