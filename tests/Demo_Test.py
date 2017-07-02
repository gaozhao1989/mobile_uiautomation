import logging
import time
import pytest
import allure
from utils.Base_Test import BaseTest
from pages import Demo_Page

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('Test_Demo')
time.sleep(1)


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.feature('user')
@allure.story('demo')
class Test_Demo(BaseTest):
    @allure.step(title="test_demo01_success")
    def test_demo01_success(self):
        demo_page = Demo_Page.Demo(self.driver)
        assert demo_page.is_page_present()
        demo_page.take_screen_shot('Demo_Page')
        demo_page.click_text_accessibility()
        demo_page.wait_seconds(5)
