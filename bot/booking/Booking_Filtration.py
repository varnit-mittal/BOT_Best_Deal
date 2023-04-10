'''This file will include a class with instance methods.
That will be responsible to interact with our website,
after we have got some results--> to apply filtration'''
from selenium.webdriver.remote.webdriver import WebDriver
class BookingFiltration:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def apply_star_rating(self,*star_values):
        driver=self.driver
        star_filter_box=driver.find_element('id','filter_group_class_:R14q:')
        star_child_ele=star_filter_box.find_elements('css selector','*')
        for star_value in star_values:
            for star_element in star_child_ele:
                if str(star_element.get_attribute('innerHTML')).strip()== star_value:
                    star_element.click()
                    break

    def sort_price(self):
        driver=self.driver
        driver.find_element('css selector','button[data-testid="sorters-dropdown-trigger"]').click()
        driver.find_element('css selector','button[data-id="price"]').click()

