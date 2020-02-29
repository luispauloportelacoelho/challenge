# Challenge_QA_Automation
## Project Description
The goal of this project is to automate the process of buy merchandising.
## Prerequisites
### Chromedriver
Open the command line and run the next command:
```
npm install chromedriver
```
### Python
Download Python from the link below:
```
https://www.python.org/downloads/
```
After that you should install it.
### Unittest
Open the command line and run the next command:
```
pip install unittest
```
### Selenium
Open the command line and run the next command:
```
pip install -U selenium
```
## Running the tests
To run the test, the steps are:
* open the command line
* execute the command
```
python test.py
```
*Note*: test is executed using Chromedriver
## Project Structure
### Drivers
Manage the drivers used by the Project. The drivers are in
```
drivers.py
```
Example:
```python
class Drivers:
    CHROME_DRIVER_PATH = "chromedriver.exe"
```
### Locators
Manage the locators used by the Project. The locators are divided according the importante in terms of business logic. The Locators are in
```
locators.py
```
Example:
```python
class PaymentPage:
    PAYMENT_RADIO_BUTTON = '[data-testid="co-payment-options"]'
    CREDIT_CARD_RADIO_BUTTON = '[data-testid="dcp-co-payment-modes_options-CREDITCARD-label"]'
    VISA_RADIO_BUTTON = '[data-testid="dcp-co-payment-modes_options-visa-label"]'
    CONFIRMATION_BUTTON = '[data-testid="co-func-footer-forward"]'
```
### User data
Manage the user data. The user data is in
```
user.py
```
Example:
```python
class User:
    EMAIL = 'luisportelacoelho@gmail.com'
    FIRST_NAME = 'Luis'
    LAST_NAME = 'Coelho'
```
### POM
Each class represents a page while each method represents the elements within that class.
Example:
```python
class DeliveryInformation:

    def __init__(self, browser):
        self.browser = browser

    def fillEmail(self, email):
        self.browser.find_element_by_css_selector(locators.AddressDelivery.EMAIL).clear()
        self.browser.find_element_by_css_selector(locators.AddressDelivery.EMAIL).send_keys(email)

```
### Test
The test is created in the file
```
test.py
```
In order to create new test, check the example:
```python
def test_buy_merchandising(self):

      productSelection = ProductSelection(self.browser)
      productSelection.select_female()
      productSelection.select_product()

      ...
```
