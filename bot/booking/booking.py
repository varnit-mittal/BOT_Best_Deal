from selenium import webdriver
import booking.constants as const
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from booking.Booking_Filtration import BookingFiltration
import time
from booking.booking_report import BookingReport
from prettytable import PrettyTable

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_experimental_option("excludeSwitches", ['enable-logging'])
# driver = webdriver.Chrome(options=options)

class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"C:\Users\HP\OneDrive\Desktop\web_scrapper\web_scrapping_hacknite\chromedriver_win32",tearDown=False):
        self.tearDown=tearDown
        self.driver_path=driver_path
        os.environ['PATH']+=self.driver_path
        super(Booking,self).__init__()
        self.driver= webdriver.Chrome(options=options)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
            if(self.tearDown):
                self.driver.quit()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)
        driver=self.driver
        driver.find_element('css selector','[aria-label="Dismiss sign-in info."]').click()

    def change_currency(self,currency=None):
        driver=self.driver
        driver.find_element('css selector','button[data-testid="header-currency-picker-trigger"]').click()
        change=driver.find_element(By.XPATH,(f"//*[text()='{currency}']"));
        change.click()

    def select_place_to_go(self,place_to_go):
        driver=self.driver
        search_field=driver.find_element('id',':Ra9:')
        search_field.send_keys(Keys.CONTROL,"a",Keys.DELETE)
        search_field.send_keys(place_to_go)
        first_result=driver.find_element(By.XPATH,(f"//*[text()='{place_to_go}']"));
        first_result.click()

    #aria-label="16 April 2023"

    def select_dates(self,check_in_date,check_out_date):
        driver=self.driver
        driver.find_element('css selector',f'[aria-label="{check_in_date}"]').click()
        driver.find_element('css selector',f'[aria-label="{check_out_date}"]').click()


    # data-testid="occupancy-config"

    def select_adults(self,count=4):
        driver=self.driver
        driver.find_element('css selector','button[data-testid="occupancy-config"]').click()
        var=driver.find_elements(By.CSS_SELECTOR,("button.fc63351294.a822bdf511.e3c025e003.fa565176a8.f7db01295e.c334e6f658.e1b7cfea84.d64a4ea64d"))
        # "fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 d64a4ea64d"
        if(count >2):
            for i in var:
                for j in range(count-2):
                    i.click()
                break
        # fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 cd7aa7c891
        else:
            var=driver.find_element(By.CSS_SELECTOR,("button.fc63351294.a822bdf511.e3c025e003.fa565176a8.f7db01295e.c334e6f658.e1b7cfea84.cd7aa7c891")).click()

    def click_search(self):
        driver=self.driver
        driver.find_element(By.CSS_SELECTOR,("button.fc63351294.a822bdf511.d4b6b7a9e7.cfb238afa1.c938084447.f4605622ad.aa11d0d5cd")).click()

    def apply_filtration(self):
        filtration=BookingFiltration(self.driver)
        filtration.apply_star_rating("5 stars","3 stars", "4 stars")
        time.sleep(2.0)
        filtration.sort_price()


    # def refres(self):
    #     self.driver.refresh()

    def report_results(self):
        driver=self.driver
        hotel_boxes=driver.find_element(
            'id',
            'search_results_table'
        )
        
        report=BookingReport(hotel_boxes)
        # .find_elements('class name','c90a25d457')
        # report.pull_titles()
        table=PrettyTable(
            ["Hotel Name","Hotel Price","Hotel Score"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)
