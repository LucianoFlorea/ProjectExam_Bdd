from behave import *


@given('I log in with the standard user.')
def step_impl(context):
    context.inventory_page.login()


@when('I sort products by price, high to low.')
def step_impl(context):
    context.sorting_page.sort_hi_to_low()


@then('The first price is higher than the second price.')
def step_impl(context):
    context.sorting_page.verify_first_price_higher_than_second_price()


@when('I sort products by price, low to high.')
def step_impl(context):
    context.sorting_page.sort_lo_to_hi()


@then('The first price is lower than the second price.')
def step_impl(context):
    context.sorting_page.verify_first_price_lower_than_second_price()


@when('I sort products in alphabetical order.')
def step_impl(context):
    context.sorting_page.sort_a_to_z()


@then('The sorted products are in alphabetical order.')
def step_impl(context):
    context.sorting_page.verify_products_in_alphabetical_order()


@when('I sort products in reverse alphabetical order.')
def step_impl(context):
    context.sorting_page.sort_z_to_a()


@then('The sorted products are in reverse alphabetical order.')
def step_impl(context):
    context.sorting_page.verify_products_in_reverse_alphabetical_order()
