from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.IN_BASKET), \
            "There is a product in basket, but should not be"

    def should_be_message_about_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "There is no message, or basket is not empty"

