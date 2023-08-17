from browser import Browser
from pages.login_page import Login_page
from pages.inventory_page import Inventory_page
from pages.price_page import Price_page


def before_all(context):
    context.browser = Browser()
    context.login_page = Login_page()
    context.inventory_page = Inventory_page()
    context.price_page = Price_page()




def after_all(context):
    context.browser.close()
