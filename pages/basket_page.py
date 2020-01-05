from .base_page import BasePage
from .locators import BasketPageLocators, ProductPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    
    def should_be_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is empty, but shouldn't be"
        
    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket isn't empty, but should be"
        
    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "No message that basket is empty, but should be"
        
    def should_be_no_message_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Message that basket is empty, but shouldn't be"
        
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):    
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MESSAGE), "Success message is presented, but should be disappeared"
    
    def should_be_info_message_with_correct_price(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_INFO_MESSAGE), "Info message is not presented"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_INFO_MESSAGE).text, "Incorrect basket total is in info message"
        