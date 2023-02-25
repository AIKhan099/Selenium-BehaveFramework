from behave import *
from time import sleep
from steps import constants, utility


@given('the price of first product is "{price}"')
def step_impl(context, price):
    
    # utility.getting_text_by_xpath(context, constants.Xpaths.first_product_ptice_xpath.value)
    price_=utility.getting_text_by_xpath(context, constants.Xpaths.first_product_ptice_xpath.value)
    assert price_==price
    
    