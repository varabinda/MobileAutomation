import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import configuration as conf
import home_pom as home
import login_pom as login
import preferences_pom as pref
import wd_utils


def is_on_home(driver):
    print('Current activity: ' + driver.current_activity)
    if driver.current_activity == conf.HOME_ACTIVITY:
        wd_utils.get_handle(driver, AppiumBy.XPATH, home.XPATH_HOME_BUTTON).click()
        return True

    print('Current activity: ' + driver.current_activity)
    if wd_utils.wait_activity(driver, conf.LOGIN_ACTIVITY):
        print('Clicking back button')
        driver.back()

    return wd_utils.wait_activity(driver, conf.HOME_ACTIVITY)


def skip_notification(driver):
    if driver.current_activity == conf.HOME_ACTIVITY and wd_utils.get_handle(driver, AppiumBy.XPATH, home.XPATH_HOME_BUTTON) is not None:
        return True

    print('Checking for notification bottom sheet')
    try:
        wd_utils.get_handle(driver, AppiumBy.XPATH, home.XPATH_NOTIFICATION)
    except (NoSuchElementException, TimeoutException):
        return True

    wd_utils.get_handle(driver, AppiumBy.XPATH, home.XPATH_SKIP_NOTIFICATION_BUTTON).click()

    if driver.current_activity == conf.HOME_ACTIVITY and wd_utils.get_handle(driver, AppiumBy.XPATH, home.XPATH_HOME_BUTTON) is not None:
        return True

    return False


@pytest.fixture(scope='function')
def setup_login(setup_server, setup_driver):
    driver = setup_driver
    wd_utils.get_handle(driver, AppiumBy.XPATH, home.XPATH_MORE_BUTTON).click()
    try:
        wd_utils.get_handle(driver, AppiumBy.XPATH, home.XPATH_LOGGED_IN_NAME)
    except (NoSuchElementException, TimeoutException):
        test_login = TestLoginLogoutFlows()
        test_login.test_login(setup_server, setup_driver)

    return setup_driver


class TestLoginLogoutFlows:

    @pytest.mark.test_login
    def test_login(self, setup_server, setup_driver):
        driver = setup_driver
        assert (driver.current_package + driver.current_activity == conf.APP_PACKAGE +
                conf.SPLASH_ACTIVITY), 'Could not find splash screen'

        assert is_on_home(driver), 'Not on home screen'
        assert skip_notification(driver), 'Notification bottom sheet visible'

        time.sleep(2)

        wd_utils.get_handle(driver, AppiumBy.XPATH, home.XPATH_MORE_BUTTON).click()

        wd_utils.get_handle(driver, AppiumBy.XPATH, home.XPATH_LOGIN_BUTTON).click()

        assert wd_utils.wait_activity(driver, conf.LOGIN_ACTIVITY), 'Not on login screen'

        wd_utils.get_handle(driver, AppiumBy.ACCESSIBILITY_ID, login.ACCESSIBILITY_ID_GOOGLE).click()

        user_name = wd_utils.get_handle(driver, AppiumBy.ID, login.ID_ACCOUNT_NAME).text

        assert user_name == 'Arabinda Verma', 'User not found'
        wd_utils.get_handle(driver, AppiumBy.XPATH, login.XPATH_USER).click()

        name = wd_utils.get_handle(driver, AppiumBy.XPATH, home.XPATH_LOGGED_IN_NAME).text
        assert name == 'Arabindaverma', 'Incorrect user logged in'

    @pytest.mark.test_logout
    def test_logout(self, setup_login):
        driver = setup_login
        assert is_on_home(driver), 'Not on home screen'
        assert skip_notification(driver), 'Notification bottom sheet visible'

        wd_utils.get_handle(driver, AppiumBy.XPATH, home.XPATH_MORE_BUTTON).click()

        wd_utils.get_handle(driver, AppiumBy.XPATH, home.XPATH_SETTINGS_OPTION).click()

        wd_utils.get_handle(driver, AppiumBy.XPATH, pref.XPATH_LOGOUT_OPTION).click()

        logout_text = driver.find_element(AppiumBy.XPATH, pref.XPATH_LOGOUT_TOAST).text
        assert logout_text == 'Logged out successfully', 'Logout toast text does not match'
