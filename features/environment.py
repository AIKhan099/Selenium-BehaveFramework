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
from steps import utility, fixtures
from behave import *
import logging
logger = logging.getLogger('myLogger')
from behave import use_fixture
# from . import utility



def before_scenario(context, scenario):
    
    logger.debug('before scenario has been started')
    utility.get_browser(context)

def after_scenario(context, scenario):
    # use_fixture(fixtures.browser,context)
    if 'browser' in scenario.tags:
        use_fixture(fixtures.browserQuit, context)
