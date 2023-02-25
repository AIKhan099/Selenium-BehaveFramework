from behave import *
import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from behave import *
import logging
from steps import utility, constants

logger = logging.getLogger('myLogger')

def get_browser(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    browser = context.browser
    context.browser.get(constants.urls.website_url.value)
    return browser
    
def getting_text_by_xpath(context, path):
    text_=context.browser.find_element(By.XPATH, path).text
    logger.debug(f'{text_}')
    return text_