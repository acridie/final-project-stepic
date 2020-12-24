from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_URL = (By.NAME, 'login_submit')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD_REP = (By.ID, 'id_registration-password2')
    REG_BUTTON = (By.CSS_SELECTOR, '[value="Register"]')


class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PROD_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PROD_PRICE = (By.CSS_SELECTOR, '.product_main p.price_color')
    CART_NAME = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    CART_PRICE = (By.CSS_SELECTOR, '.alert-info strong')


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    IN_BASKET = (By.CLASS_NAME, 'basket-items')
