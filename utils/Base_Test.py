import logging, time
import pytest
from appium import webdriver
from utils.Yaml_Factory import get_android_caps, get_ios_caps, get_appium_config, get_test_platform

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('BaseTest')
time.sleep(1)


class BaseTest(object):
    """Base Test for general tests.
    general setup and teardown func in bast_test
    """

    @classmethod
    @pytest.fixture(scope="session", autouse=True)
    def base_test(self):
        log.info('set up test:')
        self.driver = self.get_mobile_driver(self)
        yield
        self.driver.quit()
        log.info('tear down test:')
        time.sleep(1)

    def get_server_url(self):
        server_config = get_appium_config()
        base_url = server_config['base_url']
        port = server_config['port']
        server_url = 'http://' + base_url + ':' + port + '/wd/hub'
        return server_url

    def get_mobile_driver(self):
        "setup mobile device"
        os = get_test_platform()
        desired_caps = {}
        if os.lower() == 'ios':
            desired_caps = get_ios_caps()
        elif os.lower() == 'android':
            desired_caps = get_android_caps()
        driver = webdriver.Remote(self.get_server_url(self), desired_caps)
        return driver
