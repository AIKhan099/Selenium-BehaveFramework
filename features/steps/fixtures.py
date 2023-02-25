from behave import fixture
import logging
from steps import utility, constants

logger = logging.getLogger('myLogger')

@fixture
def browser(context):
    context.browser.quit()
