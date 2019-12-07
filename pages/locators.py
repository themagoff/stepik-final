from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1)")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    ADD_TO_BASKET_INFO_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
    BASKET_TOTAL_IN_INFO_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")
    
    
    
    

    