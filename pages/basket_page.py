from pages.base_page import BasePage
from pages.locators import BasketPageLocators
from translations import BASKET_IS_EMPTY_TEXT


class BasketPage(BasePage):
    def should_be_basket_is_empty_text(self, lang='en-gb'):
        expected_empty_text = BASKET_IS_EMPTY_TEXT[lang]
        basket_is_empty_block = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY)
        assert expected_empty_text in basket_is_empty_block.text, (f'The empty basket alert text is different for '
                                                                   f'language: {lang}')

    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ADDED_ITEMS), 'There are added items in basket'
