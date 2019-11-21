from pages.main_page import MainPage
from pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('promo', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", "offer7", "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo={promo}"   
    page = ProductPage(browser, link)    
    page.open()    
    page.put_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message_with_correct_product_name()
    page.should_be_info_message_with_correct_price()      
    
   
    
    







