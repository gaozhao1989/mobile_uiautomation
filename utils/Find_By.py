from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


def get_find_by(find_by):
    find_by = find_by.lower()
    if find_by == 'id':
        return By.ID
    elif find_by == 'xpath':
        return By.XPATH
    elif find_by == 'link_text':
        return By.LINK_TEXT
    elif find_by == 'partial_link_text':
        return By.PARTIAL_LINK_TEXT
    elif find_by == 'name':
        return By.NAME
    elif find_by == 'tag_name':
        return By.TAG_NAME
    elif find_by == 'class_name':
        return By.CLASS_NAME
    elif find_by == 'css_selector':
        return By.CSS_SELECTOR
    elif find_by == 'ios_uiautomation':
        return MobileBy.IOS_UIAUTOMATION
    elif find_by == 'ios_predicate':
        return MobileBy.IOS_PREDICATE
    elif find_by == 'android_uiautomator':
        return MobileBy.ANDROID_UIAUTOMATOR
    elif find_by == 'accessibility_id':
        return MobileBy.ACCESSIBILITY_ID
