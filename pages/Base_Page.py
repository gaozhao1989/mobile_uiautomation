import os, logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from utils.Yaml_Factory import get_test_platform

current_path = os.getcwd()
workspace_name = 'mobile_uiautomation'
workspace_path = current_path[:current_path.index(workspace_name) + len(workspace_name)]

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('Test_Demo')

class Base(object):
    def __init__(self, driver):
        self.driver = driver
        self.platform = get_test_platform()

    def find_element(self, loc):
        try:
            self.driver_wait(loc, 15)
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            log.info('no element %s was found in page' % (self, loc))

    def find_elements(self, loc):
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except NoSuchElementException:
            log.info('no element %s was found in page' % (self, loc))

    def rotate_screen(self, orientation):
        if orientation.upper() == 'PORTRAIT':
            self.driver.orientation = 'PORTRAIT'
        elif orientation.upper() == 'LANDSCAPE':
            self.driver.orientation = 'LANDSCAPE'

    def take_screen_shot(self, file_name):
        import datetime
        date_format = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.driver.get_screenshot_as_file(current_path + '\\screenshots\\' + date_format + file_name + '.png')

    def driver_wait(self, loc, secs):
        try:
            WebDriverWait(self.driver, secs).until(lambda driver: driver.find_element(*loc).is_displayed())
        except NoSuchElementException:
            log.info('no element %s was found in page' % (self, loc))

    def is_element_displayed(self, loc):
        try:
            self.driver.find_element(*loc).is_displayed()
            return True
        except NoSuchElementException:
            log.info('no element %s was found in page' % (self, loc))
            return False

    def click_element(self, loc, find_first=True):
        try:
            if find_first:
                self.is_element_displayed(loc)
            self.find_element(loc).click()
        except NoSuchElementException:
            log.info('no element %s was found in page' % (self, loc))

    def long_press_element(self, loc, find_first=True):
        try:
            if find_first:
                self.is_element_displayed(loc)
            action = TouchAction(self.driver)
            action.tap(self.find_element(loc)).long_press()
        except NoSuchElementException:
            log.info('no element %s was found in page' % (self, loc))

    def drag_and_drop_element(self, loc_original, loc_destination, find_first=True):
        try:
            if find_first:
                self.is_element_displayed(loc_original)
                self.is_element_displayed(loc_destination)
            self.driver.drag_and_drop(self.find_element(loc_original), self.find_element(loc_destination))
        except NoSuchElementException:
            log.info('not found element ')

    def tap(self, positions, duration=None):
        self.driver.tap(*positions, duration)

    def swipe_on_screen(self, start_x, start_y, end_x, end_y, duration=None):
        self.swipe_on_screen(start_x, start_y, end_x, end_y, duration)

    def swipe_on_screen_with_percent(self, start_x_per, start_y_per, end_x_per, end_y_per, duration=None):
        width = self.get_device_screen()[0]
        height = self.get_device_screen()[1]
        self.swipe_on_screen(width * start_x_per, height * start_y_per, width * end_x_per, height * end_y_per, duration)

    def scroll_up(self, start_height_per=0.2, end_height_per=0.8):
        self.swipe_on_screen_with_percent(0.5, start_height_per, 0.5, end_height_per)

    def scroll_down(self, start_height_per=0.8, end_height_per=0.2):
        self.swipe_on_screen_with_percent(0.5, start_height_per, 0.5, end_height_per)

    def scroll_left(self, start_width_per=0.2, end_width_per=0.8):
        self.swipe_on_screen_with_percent(start_width_per, 0.5, end_width_per, 0.5)

    def scroll_right(self, start_width_per=0.8, end_width_per=0.2):
        self.swipe_on_screen_with_percent(start_width_per, 0.5, end_width_per, 0.5)

    def get_device_screen(self):
        window_size = self.driver.get_window_size()
        return window_size['width'], window_size['height']

    def send_keys(self, loc, value, find_first=True, clear_first=True, click_first=True):
        try:
            if find_first:
                self.find_element(loc)
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except NoSuchElementException:
            log.info('no element %s was found in page' % (self, loc))

    def hide_keyboard(self):
        if self.platform == 'iOS':
            self.driver.hide_keyboard(key_name='return')
        elif self.platform == 'Android':
            self.driver.hide_keyboard()

    def keyevent(self, keycode, metastate=None):
        self.driver.keyevent(keycode, metastate)

    def current_activity(self):
        return self.driver.current_activity()

    def wait_activity(self, activity, timeout):
        self.driver.find_element_by_android_uiautomator()
        return self.driver.wait_activity(activity, timeout)

    def wait_seconds(self, sec=3):
        import time
        time.sleep(sec)
