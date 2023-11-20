from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_CART_BTN = (By.CSS_SELECTOR, '.basket-mini [href*="/basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ADDED_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner p')


class LoginPageLocators:
    REG_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REG_FORM_PASSWORD_FIELD_PRIMARY = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_FORM_PASSWORD_FIELD_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')
    REG_ERROR_ALERT = (By.CSS_SELECTOR, '#register_form alert-danger')


class ProductPageLocators:
    ADD_CART_BTN = (By.CSS_SELECTOR, '#add_to_basket_form .btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner strong')
    PRICE_ALERT = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) .alertinner strong')
