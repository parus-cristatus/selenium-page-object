from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    product_price = None
    product_name = None
    added_to_cart_product_name = None
    added_to_cart_product_price = None

    def click_add_to_cart_btn(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_CART_BTN)
        add_to_cart_btn.click()

    def get_product_name(self):
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_added_to_cart_name(self):
        self.added_to_cart_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text

    def get_product_added_to_cart_price(self):
        self.added_to_cart_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_added_to_cart_product_name_the_same(self):
        assert self.product_name == self.added_to_cart_product_name, 'The added to cart product name is different'

    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_CART_BTN), 'The add to cart button is not present'

    def should_be_added_to_cart_product_price_the_same(self):
        assert self.product_price == self.added_to_cart_product_price, 'The added to cart product price is different'

    def should_be_no_success_alert(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_ALERT), ('The add to cart success alert '
                                                                                      'is present')

    def should_success_alert_disappear_after_adding_to_cart(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_ALERT), 'The success alert did not disappear'
