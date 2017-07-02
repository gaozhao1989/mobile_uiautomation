import Base_Page
from utils import Yaml_Factory, Find_By


class Demo(Base_Page.Base):
    locator_file = 'demo_page'
    platform = Yaml_Factory.get_test_platform()
    find_by = Find_By.get_find_by

    data_text_accessibility = Yaml_Factory.get_locator_properties(locator_file, 'text_accessibility', platform)
    text_accessibility = (find_by(data_text_accessibility[0]), data_text_accessibility[1])

    data_text_content = Yaml_Factory.get_locator_properties(locator_file, 'text_content', platform)
    text_content = (find_by(data_text_content[0]), data_text_content[1])

    def click_text_accessibility(self):
        self.click_element(self.text_accessibility)

    def click_text_content(self):
        self.click_element(self.text_content)
    
    def is_page_present(self):
        return self.is_element_displayed(self.text_accessibility)
