from selenium.webdriver.common.by import By

class Cookie:
    AGREE_BUTTON = 'btn-agree'


class FashionBeauty:
    FASHION_SELECTION = 'utils-content-carousel-container-tile-image'
    PRODUCT_SELECTION = 'utils-product-tile-price'


class ShoppingBasket:
    PRICE = '[data-testid="pdp-buy-box-add-to-basket-price"]'
    ADD_BASKET_BUTTON = '[data-testid="pdp-buy-box-add-to-basket-add"]'
    GO_SHOPPING_BASKET_BUTTON = '[data-testid="pdp-buy-box-add-to-basket-got-to-cart"]'
    CONTINUE_DELIVERY_BUTTON = '[data-testid="co-func-header-forward"]'


class AddressDelivery:
    EMAIL = '[data-testid="co-order-process-login-guest-user-email"]'
    SALUTATION_MR_RADIO_BUTTON = \
        '[data-testid="dcp-schema-form-radios-inline_co_payment_address-salutationCode-radio-id-0-label"]'
    FIRST_NAME = '[data-testid="dcp-schema-form-default_co_payment_address-firstName"]'
    LAST_NAME = '[data-testid="dcp-schema-form-default_co_payment_address-lastName"]'
    ADDRESS_1 = '[data-testid="dcp-schema-form-default_co_payment_address-line1"]'
    ADDRESS_2 = '[data-testid="dcp-schema-form-default_co_payment_address-line2"]'
    POSTAL_CODE = '[data-testid="dcp-schema-form-default_co_payment_address-postalCode"]'
    ADDRESS_TOWN = '[data-testid="dcp-schema-form-default_co_payment_address-town"]'
    CONTINUE_PAYMENT = '[data-testid="co-func-header-forward"]'
    PLACE_ORDER_GUEST_BUTTON = '[data-testid="co-order-process-login-guest-user-cta"]'


class PaymentPage:
    PAYMENT_RADIO_BUTTON = '[data-testid="co-payment-options"]'
    CREDIT_CARD_RADIO_BUTTON = '[data-testid="dcp-co-payment-modes_options-CREDITCARD-label"]'
    VISA_RADIO_BUTTON = '[data-testid="dcp-co-payment-modes_options-visa-label"]'
    CONFIRMATION_BUTTON = '[data-testid="co-func-footer-forward"]'


class VerificationPage:
    PRICE = '[data-testid="co-orderline-total-price"]'
