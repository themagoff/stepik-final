from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def put_item_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_btn.click()
        
    def should_be_info_message_with_correct_price(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_INFO_MESSAGE), "Info message is not presented"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_INFO_MESSAGE).text, "Incorrect basket total is in info message"
        
    def should_be_success_message_with_correct_product_name(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MESSAGE), "Success message is not presented"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text, "Incorrect product name is in success message"
    
    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MESSAGE), "Success message is presented, but should be disappeared"
        