from behave import *
from time import sleep
from pages.inventory_page import Inventory_page

@given("I am logged into the app for price")
def step_impl(context):
    context.inventory_page.login()

@when('I check the inventory page')
def step_impl(context):
    context.inventory_page.check_inventory_page()

@then('I should see the prices of all products')
def step_impl(context):
    products = context.inventory_page.get_product_names_and_prices()

    # Now, you can loop through the products dictionary and compare the prices
    for product_name, actual_price in products.items():
        # Get the expected price based on the product name
        expected_price = inventory_page.get_expected_price_by_product_name(product_name)

        # Add your price comparison logic here (assertion or verification)
        assert actual_price == expected_price, f"Price mismatch for product: {product_name}. Expected: {expected_price}, Actual: {actual_price}"
@when('I go to the product page for "{item}"')
def step_impl(context, item):
    context.item = item  # Store the item name in the context for later use
    context.inventory_page.go_to_product_page(item)


@then('I should see the price of the "{item}"')
def step_impl(context, item):

    expected_price = context.inventory_page.get_expected_price_by_product_name(context.item)

    assert expected_price is not None, f"Expected price for {context.item} was not found on the page."

