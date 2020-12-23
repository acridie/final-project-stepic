from pages.product_page import ProductPage
import pytest
import time

# помечаем тест №7 (тест с набором параметров 7) как условно пройденый
@pytest.mark.parametrize('num', ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail),
                                 '8', '9'])
def test_guest_can_add_product_to_basket(browser, num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_be_same_name()
    page.should_be_same_price()
