import unittest
import time
import locators
import drivers
from selenium import webdriver
from user import User
from POM import ProductSelection
from POM import Basket
from POM import DeliveryInformation
from POM import Payment

class Test(unittest.TestCase):

    def setUp(self):
        SITE_URL = 'https://shop.mercedes-benz.com/en-gb/collection/'
        TIME_OUT_SECONDS = 10
        self.browser = webdriver.Chrome(drivers.Drivers.CHROME_DRIVER_PATH)
        self.browser.implicitly_wait(TIME_OUT_SECONDS)
        self.browser.maximize_window()
        self.browser.get(SITE_URL)
        self.browser.find_element_by_class_name(locators.Cookie.AGREE_BUTTON).click()
        self.browser.get(SITE_URL)

    def test_buy_merchandising(self):

        productSelection = ProductSelection(self.browser)
        productSelection.select_female()
        productSelection.select_product()

        basket = Basket(self.browser)
        basket.addToBasket()
        basket.confirmItem()

        deliveryInformation = DeliveryInformation(self.browser)
        deliveryInformation.fillEmail(User.EMAIL)
        deliveryInformation.placeOrder()
        deliveryInformation.salutation()
        deliveryInformation.firstName(User.FIRST_NAME)
        deliveryInformation.lastName(User.LAST_NAME)
        deliveryInformation.address(User.ADDRESS_1, User.ADDRESS_2,
            User.POSTAL_CODE, User.ADDRESS_TOWN)
        time.sleep(5)
        deliveryInformation.continueDelivery()

        payment = Payment(self.browser);
        payment.page()
        payment.paymentVisa()
        payment.confirmation()


    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
