import time

from behave import *


@given("I am logged into the app")
def step_impl(context):
    context.inventory_page.login()


@when('I click Add to chart button to the item "{item}"')
def step_impl(context, item):
    time.sleep(3)
    context.inventory_page.press_add_cart_item(item)


@then('The Remove button is displayed for the item "{item}"')
def step_impl(context, item):
    context.inventory_page.check_remove_button_is_present(item)


@when('I check the basket page')
def step_impl(context):
    context.inventory_page.check_basket_page()


@then('The item "{item}" is displayed in basket')
def step_impl(context, item):
    context.inventory_page.check_item_in_basket(item)


@when('I remove the item "{item}" from the cart')
def step_impl(context, item):
    context.inventory_page.remove_item_from_cart(item)


@when('I go back to shopping list')
def step_impl(context):
    context.inventory_page.go_back_to_shopping_list()


@then('The Add to chart button is displayed for the item "{item}"')
def step_impl(context, item):
    context.inventory_page.check_add_to_cart_btn_present(item)
