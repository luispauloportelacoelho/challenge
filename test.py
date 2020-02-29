import time
import locators
import drivers
from selenium import webdriver
from user import User
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SITE_URL = 'https://shop.mercedes-benz.com/en-gb/collection/'
TIME_OUT_SECONDS = 10

browser = webdriver.Chrome(drivers.Drivers.CHROME_DRIVER_PATH)
browser.implicitly_wait(TIME_OUT_SECONDS)
browser.maximize_window()
browser.get(SITE_URL)


def selectItem():

    try:
        browser.find_element_by_class_name(locators.Cookie.AGREE_BUTTON).click()
        browser.get(SITE_URL)
        fashion_selection = browser.find_elements_by_class_name(locators.FashionBeauty.FASHION_SELECTION)
        woman_selection = fashion_selection[0]
        woman_selection.click()
        woman_products = browser.find_elements_by_class_name(locators.FashionBeauty.PRODUCT_SELECTION)
        woman_product = woman_products[0]
        woman_product.click()
    except:
        browser.save_screenshot('screenshots/errorSelectProduct.png')


def addBasket():
    try:
        browser.find_element_by_css_selector(locators.ShoppingBasket.ADD_BASKET_BUTTON).click()
        browser.find_element_by_css_selector(locators.ShoppingBasket.GO_SHOPPING_BASKET_BUTTON).click()
        browser.find_element_by_css_selector(locators.ShoppingBasket.CONTINUE_DELIVERY_BUTTON).click()
    except:
        browser.save_screenshot('screenshots/errorAddBasket.png')


def fillDeliveryInformation():
    try:
        browser.find_element_by_css_selector(locators.AddressDelivery.EMAIL).send_keys(User.EMAIL)
        browser.find_element_by_css_selector(locators.AddressDelivery.PLACE_ORDER_GUEST_BUTTON).click()
        browser.find_element_by_css_selector(locators.AddressDelivery.SALUTATION_MR_RADIO_BUTTON).click()
        browser.find_element_by_css_selector(locators.AddressDelivery.FIRST_NAME).send_keys(User.FIRST_NAME)
        browser.find_element_by_css_selector(locators.AddressDelivery.LAST_NAME).send_keys(User.LAST_NAME)
        browser.find_element_by_css_selector(locators.AddressDelivery.ADDRESS_1).send_keys(User.ADDRESS_1)
        browser.find_element_by_css_selector(locators.AddressDelivery.ADDRESS_2).send_keys(User.ADDRESS_2)
        browser.find_element_by_css_selector(locators.AddressDelivery.POSTAL_CODE).send_keys(User.POSTAL_CODE)
        browser.find_element_by_css_selector(locators.AddressDelivery.ADDRESS_TOWN).send_keys(User.ADDRESS_TOWN)
        time.sleep(5)
        browser.find_element_by_css_selector(locators.ShoppingBasket.CONTINUE_DELIVERY_BUTTON).click()
    except:
        browser.save_screenshot('screenshots/errorFillDeliveryInformation.png')


def payment():
    try:
        browser.find_element_by_css_selector(locators.PaymentPage.PAYMENT_RADIO_BUTTON)
        browser.find_element_by_css_selector(locators.PaymentPage.CREDIT_CARD_RADIO_BUTTON).click()
        browser.find_element_by_css_selector(locators.PaymentPage.VISA_RADIO_BUTTON).click()
        browser.find_element_by_css_selector(locators.PaymentPage.CONFIRMATION_BUTTON).click()
    except:
        browser.save_screenshot('screenshots/errorPayment.png')


def close():
    browser.close()


try:
    selectItem()
    addBasket()
    fillDeliveryInformation()
    time.sleep(2)
    payment()
    close()
except:
    print('check the errors folder screenshot')
