from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_same_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PROD_NAME).text
        cart_name = self.browser.find_element(*ProductPageLocators.CART_NAME).text
        assert product_name in cart_name, 'Not this product in your cart'

    def should_be_same_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PROD_PRICE).text
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert product_price == cart_price, 'The price has changed'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CART_NAME), \
            "Success message is presented, but should not be"

    def should_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.CART_NAME), \
            "Success message does not disappear"
