from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.put_item_to_basket()
    page.should_be_success_message_with_correct_product_name()
    page.should_be_info_message_with_correct_price()
    
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)    
    page.open()    
    page.put_item_to_basket()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()
    
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)    
    page.open()
    page.test_guest_cant_see_success_message()
    
@pytest.mark.xfail   
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)    
    page.open()    
    page.put_item_to_basket()
    page.test_message_disappeared_after_adding_product_to_basket()
    
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_no_items_in_basket()
    page.should_be_message_basket_empty()
    
def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.put_item_to_basket()    
    page.go_to_basket_page()    
    page2 = BasketPage(browser, link)    
    page2.should_be_items_in_basket()    
    page2.should_be_no_message_basket_empty()
    
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):        
        log_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, log_link) 
        page.open()       
        email = str(time.time()) + "@fakemail.org"
        password = "gtnhj100tyuifg"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)    
        page.open()
        page.test_guest_cant_see_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)    
        page.open()    
        page.put_item_to_basket()
        page.should_be_success_message_with_correct_product_name()
        page.should_be_info_message_with_correct_price()
    