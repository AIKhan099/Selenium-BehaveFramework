from behave import fixture
import logging
from steps import utility, constants

logger = logging.getLogger('myLogger')

@fixture
def browserQuit(context):
    context.browser.quit()
