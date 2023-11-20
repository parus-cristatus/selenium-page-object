# run with python -m pytest
import pytest

from helpers import extract_language_path_from_url
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.get_product_name()
    page.get_product_price()
    page.click_add_to_cart_btn()
    page.get_product_added_to_cart_name()
    page.get_product_added_to_cart_price()
    page.should_be_added_to_cart_product_name_the_same()
    page.should_be_added_to_cart_product_price_the_same()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, 0)
    page.open()
    page.click_add_to_cart_btn()
    page.should_be_no_success_alert()


def test_guest_cant_see_success_message(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_be_no_success_alert()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, 0)
    page.open()
    page.click_add_to_cart_btn()
    page.should_success_alert_disappear_after_adding_to_cart()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    language = extract_language_path_from_url(browser.current_url, 1)
    basket_page.should_be_no_items()
    basket_page.should_be_basket_is_empty_text(lang=language)


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/'
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link, 0)
        page.open()
        page.should_be_no_success_alert()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/'
        page = ProductPage(browser, link)
        page.open()
        page.get_product_name()
        page.get_product_price()
        page.click_add_to_cart_btn()
        page.get_product_added_to_cart_name()
        page.get_product_added_to_cart_price()
        page.should_be_added_to_cart_product_name_the_same()
        page.should_be_added_to_cart_product_price_the_same()
