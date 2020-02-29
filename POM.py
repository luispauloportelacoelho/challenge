from selenium import webdriver
import locators


class ProductSelection:

    def __init__(self, browser):
        self.browser = browser

    def select_female(self):
        fashion_selection = self.browser.find_elements_by_class_name(locators.FashionBeauty.FASHION_SELECTION)
        female = fashion_selection[0]
        female.click()

    def select_product(self):
        products = self.browser.find_elements_by_class_name(locators.FashionBeauty.PRODUCT_SELECTION)
        product = products[0]
        product.click()


class Basket:

    def __init__(self, browser):
        self.browser = browser

    def price(self):
        price = self.browser.find_element_by_css_selector(locators.ShoppingBasket.PRICE).text
        return price

    def addToBasket(self):
        self.browser.find_element_by_css_selector(locators.ShoppingBasket.ADD_BASKET_BUTTON).click()

    def confirmItem(self):
        self.browser.find_element_by_css_selector(locators.ShoppingBasket.GO_SHOPPING_BASKET_BUTTON).click()
        self.browser.find_element_by_css_selector(locators.ShoppingBasket.CONTINUE_DELIVERY_BUTTON)
        self.browser.find_element_by_css_selector(locators.ShoppingBasket.CONTINUE_DELIVERY_BUTTON).click()


class DeliveryInformation:

    def __init__(self, browser):
        self.browser = browser

    def fillEmail(self, email):
        self.browser.find_element_by_css_selector(locators.AddressDelivery.EMAIL).clear()
        self.browser.find_element_by_css_selector(locators.AddressDelivery.EMAIL).send_keys(email)

    def placeOrder(self):
        self.browser.find_element_by_css_selector(locators.AddressDelivery.PLACE_ORDER_GUEST_BUTTON).click()

    def salutation(self):
        self.browser.find_element_by_css_selector(locators.AddressDelivery.SALUTATION_MR_RADIO_BUTTON).click()

    def firstName(self, first_name):
        self.browser.find_element_by_css_selector(locators.AddressDelivery.FIRST_NAME).clear()
        self.browser.find_element_by_css_selector(locators.AddressDelivery.FIRST_NAME).send_keys(first_name)

    def lastName(self, last_name):
        self.browser.find_element_by_css_selector(locators.AddressDelivery.LAST_NAME).clear()
        self.browser.find_element_by_css_selector(locators.AddressDelivery.LAST_NAME).send_keys(last_name)

    def address(self, address_1, address_2, postal_code, town):
        self.browser.find_element_by_css_selector(locators.AddressDelivery.ADDRESS_1).clear()
        self.browser.find_element_by_css_selector(locators.AddressDelivery.ADDRESS_1).send_keys(address_1)
        self.browser.find_element_by_css_selector(locators.AddressDelivery.ADDRESS_2).clear()
        self.browser.find_element_by_css_selector(locators.AddressDelivery.ADDRESS_2).send_keys(address_2)
        self.browser.find_element_by_css_selector(locators.AddressDelivery.POSTAL_CODE).clear()
        self.browser.find_element_by_css_selector(locators.AddressDelivery.POSTAL_CODE).send_keys(postal_code)
        self.browser.find_element_by_css_selector(locators.AddressDelivery.ADDRESS_TOWN).clear()
        self.browser.find_element_by_css_selector(locators.AddressDelivery.ADDRESS_TOWN).send_keys(town)

    def continueDelivery(self):
        self.browser.find_element_by_css_selector(locators.ShoppingBasket.CONTINUE_DELIVERY_BUTTON).click()


class Payment:

    def __init__(self, browser):
        self.browser = browser

    def page(self):
        self.browser.find_element_by_css_selector(locators.PaymentPage.PAYMENT_RADIO_BUTTON)

    def paymentVisa(self):
        self.browser.find_element_by_css_selector(locators.PaymentPage.CREDIT_CARD_RADIO_BUTTON).click()
        self.browser.find_element_by_css_selector(locators.PaymentPage.VISA_RADIO_BUTTON).click()

    def confirmation(self):
        self.browser.find_element_by_css_selector(locators.PaymentPage.CONFIRMATION_BUTTON).click()


class Verification:
    def __init__(self, browser):
        self.browser = browser

    def price(self):
        verification_price = self.browser.find_element_by_css_selector(locators.VerificationPage.PRICE).text
        return verification_price
