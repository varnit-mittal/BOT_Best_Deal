'''This file is going to include method that will parse
the specific data that we need from each one of the deal boxes'''
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self, boxes_section_element: WebElement) -> None:
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements('class name', 'da89aeb942')

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(
                'class name',
                'a23c043802'
            ).get_attribute('innerHTML').strip()

            hotel_price = deal_box.find_element(
                'css selector',
                'span[data-testid="price-and-discounted-price"]'
            ).get_attribute('innerHTML').strip()
            try:
                hotel_score_data = deal_box.find_element(
                    'css selector',
                    '[data-testid="review-score"]'
                )

                hotel_score = hotel_score_data.find_element(By.CSS_SELECTOR, ".b5cd09854e.d10a6220b4").get_attribute(
                    'innerHTML'
                ).strip()
            except Exception as e:
                hotel_score = "No Data"

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )

        return collection
