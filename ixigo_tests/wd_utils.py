from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_INTERVAL = 20
POLL_INTERVAL = 0.5


def get_handle(driver, loc_strategy: str, locator: str):
    print('Checking for ' + locator)
    wait = WebDriverWait(driver, WAIT_INTERVAL, POLL_INTERVAL)
    wait.until(EC.visibility_of_element_located((loc_strategy, locator)))
    return driver.find_element(loc_strategy, locator)


def wait_activity(driver, activity):
    print('Waiting for ' + activity)
    return driver.wait_activity(activity, WAIT_INTERVAL, POLL_INTERVAL)
